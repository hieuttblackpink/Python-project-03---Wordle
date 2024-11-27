FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies and Enchant
RUN apt-get update && apt-get install -y --no-install-recommends \
    libenchant-2-2 \
    build-essential \
    gcc \
    libffi-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --no-input

# Start the application
CMD ["gunicorn", "wordle_server.wsgi:application", "--bind", "0.0.0.0:8000"]
