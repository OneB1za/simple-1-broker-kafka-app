import os
from confluent_kafka import Producer
import time

KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'kafka:29092')
TOPIC = os.getenv('KAFKA_TOPIC', 'testtopic')

# Конфигурация продюсера
producer_conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'client.id': 'python-producer'
}

producer = Producer(producer_conf)
i = 0

while True:
    i += 1
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    message = f'Msg: {i}, {current_time}'
    
    try:
        producer.produce(TOPIC, value=message)  # Отправка сообщения
        print(f'Sent: {message}')
    except Exception as e:
        print(f'Error: {e}')
    
    producer.flush()  # Очистка буфера
    time.sleep(3)

print('Producer has finished work.')

