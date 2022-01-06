#%%
import boto3
import re
import datetime
from botocore.exceptions import ClientError

region = "{{cookiecutter.aws_region}}"
ecs_client = boto3.client("ecs", region_name=region)
ecr_client = boto3.client("ecr", region_name=region)
ec2_client = boto3.client("ec2", region_name=region)
logs_client = boto3.client("logs", region_name=region)


def create_ecs_cluster(name):
    response = ecs_client.create_cluster(clusterName=name)
    return response


def create_ecr_repo(image_name):
    response = ecr_client.create_repository(repositoryName=image_name)
    return response


def create_task_definition(task_definition, repo_uri):
    # The executionRole below has to include the logs:CreateLogGroup policy to be able
    # to create a log group enabled by awslogs-create-group. Instead, the log group is
    # created manually.
    try:
        logs_client.create_log_group(logGroupName="/ecs/{{cookiecutter.namespace}}")
    except ClientError as e:
        # Log group already exists
        pass
    
    response = ecs_client.register_task_definition(
        requiresCompatibilities=["FARGATE"],
        containerDefinitions=[
            {
                "name": "{{cookiecutter.namespace}}",
                "image": repo_uri,
                "logConfiguration": {
                    "logDriver": "awslogs",
                    "options": {
                        "awslogs-region": "{{cookiecutter.aws_region}}",
                        "awslogs-group": "/ecs/{{cookiecutter.namespace}}",
                        "awslogs-stream-prefix": "ecs",
                        # "awslogs-create-group": "true",
                    }
                },
            }
        ],
        # Awsvpc is required with Fargate
        networkMode="awsvpc",
        memory="1024",
        cpu="512",
        executionRoleArn="arn:aws:iam::992940520675:role/ecsTaskExecutionRole",
        family=task_definition,
        runtimePlatform={"operatingSystemFamily": "LINUX"},
    )
    return response


def create_vpc(name):
    ec2 = boto3.resource("ec2")
    vpc = ec2.create_vpc(CidrBlock="10.0.0.0/24")
    vpc.create_tags(Tags=[{"Key": "Name", "Value": name}])

    internet_gateway = ec2.create_internet_gateway()
    internet_gateway.attach_to_vpc(VpcId=vpc.id)

    route_table = ec2.create_route_table(VpcId=vpc.id)
    route_table.create_route(GatewayId=internet_gateway.id, DestinationCidrBlock="0.0.0.0/0")

    subnet = vpc.create_subnet(CidrBlock="10.0.0.0/24")
    ec2_client.associate_route_table(RouteTableId=route_table.id, SubnetId=subnet.id)

    description = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    security_group = vpc.create_security_group(Description=description, 
                                               GroupName="{{cookiecutter.namespace}}Security")

    return vpc.id, subnet.id, security_group.id


def sed(filename, word, replacement):
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(re.sub(re.escape(word), replacement, line))


def main():
    # Step 1: Create ECR repo for Docker images
    ecr_response = create_ecr_repo("{{cookiecutter.ecr_repo}}")
    repo_uri = ecr_response["repository"]["repositoryUri"]
    sed("Makefile", "$ECR_REPO", repo_uri)

    # Step 2: Define task definitions to run ML jobs
    task_definition_response = create_task_definition("{{cookiecutter.task_definition}}", repo_uri)
    print(task_definition_response)

    # Step 3: Create ECS cluster
    ecs_response = create_ecs_cluster("{{cookiecutter.ecs_cluster}}")
    print(ecs_response)

    # Step 4: Define VPC for Fargate cluster
    vpc_id, subnet_id, security_group_id = create_vpc("{{cookiecutter.vpc}}")
    print(vpc_id, subnet_id, security_group_id)
    sed("Makefile", "$AWS_SUBNET", subnet_id)
    sed("Makefile", "$SECURITY_GROUP", security_group_id)


if __name__ == "__main__":
    main()