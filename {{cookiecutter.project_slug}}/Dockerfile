FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV WANDB_API_KEY="{{cookiecutter.wandb_key}}"
ENV WANDB_RUN="yann21/repo-src/q6amhwrz"

CMD ["sh", "-c", "wandb agent $WANDB_RUN"]
