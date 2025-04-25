# Use official Playwright image with Python and browsers preinstalled
FROM mcr.microsoft.com/playwright/python:v1.26.0-focal

# Set working directory inside the container
WORKDIR /app

# Copy everything into the container
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Run your main script
CMD ["python", "main.py"]
