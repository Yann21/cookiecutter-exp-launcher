import boto3
import os
from pathlib import Path

ecr_client = boto3.client("ecr")
ecs_client = boto3.client("ecs")
ec2_client = boto3.client("ec2")

def delete_ecr(repo):
  try:
    ecr_client.delete_repository(repositoryName=repo, force=True)
  except Exception as e:
    print(e)

def delete_cluster(cluster):
  try:
    ecs_client.delete_cluster(cluster=cluster)
  except Exception as e:
    print(e)

def delete_vpcs(vpc_name):
  vpcs = ec2_client.describe_vpcs()["Vpcs"]

  for vpc in vpcs:
    try:
      tags = vpc["Tags"]
      name = [tag for tag in tags if tag["Key"] == "Name"][0]
      vpc_name = name["Value"]
      if vpc_name == vpc_name:
        delete_vpc_script = Path(__file__).parent/"delete_vpc.sh"
        region = "{{cookiecutter.aws_region}}"
        os.system(f"""sh -c "yes | {str(delete_vpc_script)} {region} {vpc['VpcId']}" """)
    except Exception as e:
      print(e)

def main():
  delete_ecr("{{cookiecutter.ecr_repo}}")
  delete_cluster("{{cookiecutter.ecs_cluster}}")
  delete_vpcs("{{cookiecutter.vpc}}")


if __name__ == "__main__":
  main()