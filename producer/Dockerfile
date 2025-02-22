FROM python:3.9-slim

RUN pip install confluent-kafka

WORKDIR /app

COPY producer.py .

ENV KAFKA_BROKER="kafka:29092"
ENV KAFKA_TOPIC="testtopic"

ENTRYPOINT ["python", "producer.py"]
