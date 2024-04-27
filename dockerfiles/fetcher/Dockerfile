# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
RUN pip install pyyaml requests Flask

# Copy the Python script into the container at /app
COPY *.py /app/

# Command to run the fetch script
CMD ["python", "server.py"]
