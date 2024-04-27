# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the Python script into the container at /app
COPY *.py /app/

ENV NAME FetcherService

# Command to run the fetch script
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8001", "-t", "300", "server:app"]
