FROM python:3.12-slim
LABEL authors="vektrius"
RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
COPY . /app
WORKDIR /app
RUN poetry install --no-root
RUN poetry run python3 manage.py migrate
RUN poetry run python3 manage.py collectstatic --noinput
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "test_task.wsgi:application"]
