# Use a specific, lightweight Python version as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install Tkinter's system dependency
RUN apt-get update && apt-get install -y tk

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code from src/zivia into the container's WORKDIR
COPY ./src/zivia/ .

# Set the command to run your application
CMD ["python", "main.py"]
