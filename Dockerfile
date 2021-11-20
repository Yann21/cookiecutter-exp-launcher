#FROM hello-world
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV WANDB_API_KEY="REPLACE_KEY"
ENV WANDB_RUN="GENERATED_BY_START_SWEEP"

CMD ["sh", "-c", "wandb agent $WANDB_RUN"]
