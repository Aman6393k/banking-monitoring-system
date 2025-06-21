from kafka import KafkaProducer
import json
import time
from faker import Faker
import uuid
import random

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    transaction = {
        'transaction_id': str(uuid.uuid4()),
        'timestamp': fake.date_time_this_century().isoformat(),
        'amount': round(random.uniform(10.0, 1000.0), 2),
        'sender_account': fake.iban(),
        'receiver_account': fake.iban(),
        'location': fake.city(),
        'is_fraud': random.choice([0, 1])
    }
    producer.send('transactions', transaction)
    print(f"Produced: {transaction}")
    time.sleep(1)

