FROM python:3.9 as builder

WORKDIR /usr/src/app

RUN pip install --upgrade pip && pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt > requirements.txt


FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY --from=builder /usr/src/app/requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/