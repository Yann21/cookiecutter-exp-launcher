start:
	./start_sweep.sh
docker:
	@docker build -t exp-runner .
	@docker tag exp-runner 992940520675.dkr.ecr.eu-central-1.amazonaws.com/wandb-exp
	@docker push 992940520675.dkr.ecr.eu-central-1.amazonaws.com/wandb-exp

execute:
	@aws ecs run-task \
		--region eu-central-1 \
		--cluster MLJobs \
		--task-definition VOCWandb:3 \
		--launch-type FARGATE \
		--network-configuration "awsvpcConfiguration={subnets=[subnet-06752accdfdab8204],securityGroups=[sg-01331015613ce0e88],assignPublicIp='ENABLED'}" \
		--count 10


