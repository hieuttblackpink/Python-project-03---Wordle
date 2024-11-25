FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install Enchant and dependencies
RUN apt-get update && apt-get install -y \
    enchant-2 \
    libenchant-dev && \
    apt-get clean

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
