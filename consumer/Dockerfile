FROM python:3.9-slim

RUN pip install confluent-kafka

WORKDIR /app

COPY consumer.py .

ENV KAFKA_BROKER="kafka:29092"
ENV KAFKA_TOPIC="testtopic"
ENV KAFKA_GROUP_ID="testgroup"

ENTRYPOINT ["python", "consumer.py"]
