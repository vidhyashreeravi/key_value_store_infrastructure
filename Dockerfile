# Use a base image compatible with ARM64 architecture
FROM arm64v8/python:3.9-slim

RUN mkdir /app

WORKDIR /app

# Copy the Python dependencies file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

COPY main.py .

# Expose port 80 for the FastAPI application
EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]