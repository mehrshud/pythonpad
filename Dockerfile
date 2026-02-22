# Install dependencies for real-time collaboration
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
# Install redis for real-time collaboration
RUN pip install redis
