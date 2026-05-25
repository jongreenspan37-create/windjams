FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable real-time logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Install system tools needed for the Postgres driver (psycopg2)
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Install Python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application
COPY . .

# EXPOSE is optional but serves as good documentation for developers
EXPOSE 8000

# Defaults to localhost/8000 for the Tailscale shared network namespace
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]