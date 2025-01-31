FROM python:3.12-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache gcc musl-dev libffi-dev openssl-dev make

WORKDIR /app

COPY . /app/
RUN uv sync --frozen
ENV PATH="/app/.venv/bin:$PATH"
