# Stage 1 : Builder
FROM python:3.12-slim AS builder

# Disable cache & pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependency build package
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file
COPY requirements.txt .

# Install python dependencies
RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt

# Stage 2 : Production
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install runtime dependency only
RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy installed package from builder
COPY --from=builder /install /usr/local

# Copy source code
COPY . .

# Expose flask port
EXPOSE 5001

# Run flask app
CMD ["python", "run.py"]