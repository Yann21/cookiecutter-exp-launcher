FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV WANDB_API_KEY="{{cookiecutter.wandb_key}}"
ENV WANDB_RUN=""

CMD ["sh", "-c", "wandb agent $WANDB_RUN"]
