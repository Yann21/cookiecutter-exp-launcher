#!/usr/bin/env python

import click
import docker
import boto3
from base64 import b64decode
from pathlib import Path
import subprocess
import time

ecs_client = boto3.client("ecs")
docker_api = docker.APIClient()
ecr = boto3.client("ecr", region_name="eu-central-1")



@click.group()
def cli():
  pass

@click.command()
def init():
  """Initialize AWS resources."""
  subprocess.run(["python", "aws/initializer.py"], check=True)


@click.command()
def docker():
  """Start new run and push Docker image."""
  # Start new sweep
  subprocess.run(["sh", "wandb/start_sweep.sh"], check=True)

  # Build image
  path = str(Path(__file__).parent)

  for line in docker_api.build(path=path, tag="exp-runner", decode=True):
    click.echo(line.get("stream"), nl=False)
  
  # Authenticate
  auth = ecr.get_authorization_token()
  token = auth["authorizationData"][0]["authorizationToken"]
  username, password = b64decode(token.encode("utf-8")).decode("utf-8").split(":")
  # endpoint = auth["authorizationData"][0]["proxyEndpoint"]
  auth_config_payload = {"username": username, "password": password}

  # Push
  docker_api.tag("exp-runner", "{ecr_uri}")
  for line in docker_api.push("{ecr_uri}", auth_config=auth_config_payload, stream=True, decode=True):
    print(line)

# import wandb
# wandb.sweep({
#   "name": "test",
#   "method": "random",
#   "parameters": {
#     "epochs": {"values": [1, 2, 3]}
#   }
# })


@click.command()
@click.argument("count", type=int)
def run(count):
  """Run experiment on count machines."""
  def run_task(count):
    # AWS built-in limitation
    assert count <= 10
    response = ecs_client.run_task(
      cluster="{{cookiecutter.ecs_cluster}}", 
      taskDefinition="{{cookiecutter.task_definition}}",
      launchType="FARGATE", 
      count=count, 
      networkConfiguration={
        "awsvpcConfiguration": {
          "subnets": ["{aws_subnet}"],
          "securityGroups": ["{security_group}"],
          "assignPublicIp": "ENABLED",
        }
      }
    )
  
  # Distribute in packs of 10
  for _ in range(count // 10):
    run_task(10)
  if (count % 10) != 0:
    run_task(count % 10)


@click.command()
def clean():
  """Remove all used resources."""
  subprocess.run(["python", "aws/clean.py"], check=True)


cli.add_command(clean)
cli.add_command(docker)
cli.add_command(init)
cli.add_command(run)

if __name__ == "__main__":
  cli()