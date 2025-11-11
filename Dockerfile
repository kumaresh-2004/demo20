# Use Python as base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy code
COPY . .

# Install dependencies (optional)
RUN pip install -r requirements.txt || true

# Run app
CMD ["python3", "app.py"]
