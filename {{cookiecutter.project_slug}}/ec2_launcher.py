#%%
import boto3

region = "{{cookiecutter.aws_region}}"

ecs_client = boto3.client(
  "ecs", 
  # aws_access_key="foo",
  # aws_secrete_access_key="bar",
  region_name=region
)
ecr_client = boto3.client(
  "ecr", 
  region_name=region
)


def create_ecs_cluster(name):
  response = ecs_client.create_cluster(clusterName=name)
  return response

def create_task_definition(task_definition, repo_uri):
  response = ecs_client.register_task_definition(
    requiresCompatibilities=[
      'FARGATE'
    ],
    containerDefinitions=[
      {
        'name': '{{cookiecutter.namespace}}',
        'image': repo_uri,
      }
    ],

    networkMode='awsvpc',
    memory='1024',
    cpu='512',
    executionRoleArn='arn:aws:iam::992940520675:role/ecsTaskExecutionRole',
    family=task_definition,
    runtimePlatform={
      "operatingSystemFamily": 'LINUX'
    }
  )
  return response

def create_ecr_repo(image_name):
  response = ecr_client.create_repository(
      repositoryName=image_name
  )
  return response

def run_task(ecs_cluster, task_definition, count, subnet, security_group):
  response = ecs_client.run_task(
    cluster=ecs_cluster,
    count=count,
    taskDefinition=task_definition,
    group="auto_launch",
    launchType="FARGATE",
    networkConfiguration={
      "awsvpcConfiguration": {
        "subnets": [
          subnet
        ],
        "securityGroups": [
          security_group
        ],
        "assignPublicIp": "ENABLED"
      }
    },
  )
  return response


def main():
  response = create_ecr_repo("{{cookiecutter.ecr_repo}}")
  repo_uri = response["repository"]["repositoryUri"]

  create_task_definition("{{cookiecutter.task_definition}}", repo_uri)

  create_ecs_cluster("{{cookiecutter.ecs_cluster}}")
  run_task("{{cookiecutter.ecs_cluster}}", "{{cookiecutter.task_definition}}", 1, "subnet-06752accdfdab8204", "sg-01331015613ce0e88")

if __name__ == "__main__":
  main()
