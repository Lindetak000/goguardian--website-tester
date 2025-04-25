# Use Playwright's official image with Python 3.8 and all browser dependencies
FROM mcr.microsoft.com/playwright/python:v1.32.0-focal

# Set the working directory
WORKDIR /app

# Copy requirements and install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose the app's port
EXPOSE 8080

# Start the server
CMD ["python", "main.py"]
