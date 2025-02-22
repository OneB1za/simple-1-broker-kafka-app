import os
from confluent_kafka import Consumer, KafkaException

KAFKA_BROKER =  os.getenv('KAFKA_BROKER', 'kafka:29092')
TOPIC = os.getenv("KAFKA_TOPIC", 'testtopic')
GROUP_ID = os.getenv('KAFKA_GROUP_ID', 'testgroup')

consumer_conf = {
	'bootstrap.servers': KAFKA_BROKER,
	'group.id': GROUP_ID,
	'auto.offset.reset': 'earliest',
}

consumer = Consumer(consumer_conf)
consumer.subscribe([TOPIC])

print('Waiting for messages...')


try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        print(f"Получено: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    print("Консюмер завершает работу...")
finally:
    consumer.close()
