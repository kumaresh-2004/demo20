# Use Python 3.10 as base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask app port
EXPOSE 5000

# Start the app
CMD ["python3", "app.py"]
