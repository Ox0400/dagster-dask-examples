FROM python:3.9
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /app/runtime/
COPY dagster.yaml /app/runtime/dagster.yaml

