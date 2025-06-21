# kafka_producer.py

import json
import time
import random
from kafka import KafkaProducer
from datetime import datetime

KAFKA_TOPIC = "banking-transactions"
KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def generate_transaction():
    return {
        "account_id": random.randint(1000, 9999),
        "transaction_type": random.choice(["deposit", "withdrawal", "transfer"]),
        "amount": round(random.uniform(10, 1000), 2),
        "timestamp": datetime.utcnow().isoformat()
    }

print("🚀 Kafka Producer Started... Sending transactions...")

while True:
    txn = generate_transaction()
    producer.send(KAFKA_TOPIC, txn)
    print("Produced:", txn)
    time.sleep(2)  # Adjust as needed

