# Stage 1: Build
FROM python:3.10-slim as build

# Set working directory
WORKDIR /app

# Install build dependencies
RUN pip install --upgrade pip \
    && pip install fastapi pandas duckdb

# Copy requirements file
COPY requirements.txt .

# Copy application code
COPY . .

# Stage 2: Production
FROM python:3.10-slim

# Set non-root user
RUN groupadd -r app && useradd -r -g app app
USER app

# Set working directory
WORKDIR /app

# Copy build dependencies
COPY --from=build /app .

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD curl --fail http://localhost:8000/ || exit 1

# Run command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
