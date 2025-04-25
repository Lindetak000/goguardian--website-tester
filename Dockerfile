# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies and any required libraries for Playwright
RUN apt-get update && apt-get install -y \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    wget

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright dependencies (this ensures that the Playwright browser binaries get installed correctly)
RUN python -m playwright install --with-deps

# Expose the port Flask will run on
EXPOSE 5000

# Set environment variable for Flask app
ENV FLASK_APP=main.py

# Run the Flask app using the flask command
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
