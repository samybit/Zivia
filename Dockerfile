# Use a specific, lightweight Python version as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Tkinter requires a display, so we need to install some dependencies.
# This is for Debian-based systems like the python:slim image.
RUN apt-get update && apt-get install -y tk

# Copy requirements.txt from the root of the project
COPY requirements.txt .
# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and assets from src/zivia/ into the container's WORKDIR
COPY ./src/zivia/ .

# Set the command to run your application
CMD ["python", "main.py"]
