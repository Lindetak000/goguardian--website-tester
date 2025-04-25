# Use the official Python image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Install Playwright browsers (needed for Chromium, etc.)
RUN python -m playwright install --with-deps

# Expose port 8080 for the web server
EXPOSE 8080

# Run the app
CMD ["python", "main.py"]
