FROM python:3.13-slim

WORKDIR /cache-service

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ app/
COPY hue.sh .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
