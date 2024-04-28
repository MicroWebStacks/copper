# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app

RUN pip install PyYAML==5.3.1 requests Flask gunicorn

# Copy the Python script into the container at /app
COPY *.py /app/

ENV NAME FetcherService

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8001", "-t", "300", "web_server:app"]
