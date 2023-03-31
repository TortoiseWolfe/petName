# Use the official Python image as the base
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app.py file
COPY app.py .

# Run the pet name generator
CMD ["python", "app.py"]
