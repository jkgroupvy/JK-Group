# Use the official Python image from the Alpine-based parent image
FROM python:3.11-alpine

# Install necessary dependencies and GNU gettext tools
RUN apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers \
    postgresql-dev \
    libffi-dev \
    gettext

# Install Gunicorn
RUN pip install gunicorn

# Set the working directory
WORKDIR /code

# Copy the requirements file and install the Python dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /code/
