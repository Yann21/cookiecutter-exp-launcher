start:
	python ./aws/initializer.py
	./wandb/start_sweep.sh

docker:
	@docker build -t exp-runner .
	@docker tag exp-runner $ECR_REPO
	@docker push $ECR_REPO

execute:
	@aws ecs run-task \
		--region {{cookiecutter.aws_region}} \
		--cluster {{cookiecutter.ecs_cluster}} \
		--task-definition {{cookiecutter.task_definition}} \
		--launch-type FARGATE \
		--network-configuration "awsvpcConfiguration={subnets=[$AWS_SUBNET],securityGroups=[$SECURITY_GROUP],assignPublicIp='ENABLED'}" \
		--count 10


