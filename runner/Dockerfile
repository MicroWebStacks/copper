# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app

RUN pip install PyYAML==5.3.1 aiomqtt

COPY *.py /app/
COPY utils/*.py /app/utils/

ENTRYPOINT ["python", "service.py"]
