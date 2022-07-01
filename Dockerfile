ARG AI_ACTION #predict, data_pull, train

FROM python:3.9-slim-bullseye AS base
ARG YOUR_ENV
WORKDIR /code

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0 \
  VIRTUAL_ENV=/venv


FROM base as builder
RUN pip install poetry==$POETRY_VERSION
COPY poetry.lock pyproject.toml /code/
#create and activate virtual environment
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# install dependencies
RUN poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi
COPY . /code
RUN poetry build --no-interaction

FROM base AS app
COPY ./dist/*.whl ./ FROM builder
COPY ./venv ./ FROM builder
# activate virtual environment
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#run ai script
CMD python -m deployment_practice --ai_action=$AI_ACTION