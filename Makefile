start:
	./start_sweep.sh
docker:
	@docker build -t exp-runner .
	@docker tag exp-runner {{cookiecutter.ecr_repo}}
	@docker push {{cookiecutter.ecr_repo}}

execute:
	@aws ecs run-task \
		--region {{cookiecutter.aws_region}} \
		--cluster {{cookiecutter.ecs_cluster}} \
		--task-definition {{cookiecutter.task_definition}} \
		--launch-type FARGATE \
		--network-configuration "awsvpcConfiguration={subnets=[{{cookiecutter.aws_subnet}}],securityGroups=[cookiecutter.aws_security_group],assignPublicIp='ENABLED'}" \
		--count 10


