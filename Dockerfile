FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app/app
COPY ./app/main.py /app/main.py
COPY ./app/models.py /app/models.py
COPY ./app/schemas.py /app/schemas.py
COPY ./app/crud.py /app/crud.py
COPY ./app/db.py /app/db.py

COPY pyproject.toml poetry.lock /app/
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

EXPOSE 80