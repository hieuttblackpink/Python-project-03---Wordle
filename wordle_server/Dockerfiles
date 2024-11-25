# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies and manually upgrade GLIBC
RUN apt-get update && apt-get install -y wget bzip2 && \
    wget http://ftp.gnu.org/gnu/libc/glibc-2.38.tar.gz && \
    tar -xvzf glibc-2.38.tar.gz && \
    cd glibc-2.38 && mkdir build && cd build && \
    ../configure --prefix=/opt/glibc-2.38 && make -j$(nproc) && make install && \
    rm -rf /glibc-2.38 glibc-2.38.tar.gz && \
    apt-get install -y enchant-2 libenchant-dev && apt-get clean

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
