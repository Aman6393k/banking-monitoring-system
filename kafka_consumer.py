# kafka_consumer.py

import json
from kafka import KafkaConsumer
from db import engine
from sqlalchemy import text
from fraud_rules import is_fraud
from datetime import datetime

# ✅ Kafka topic and server config
consumer = KafkaConsumer(
    'banking-transactions',  # ✅ Topic name must match producer
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("✅ Kafka Consumer Started...")

# ✅ Listen for messages and store into PostgreSQL
for message in consumer:
    txn = message.value
    fraud = is_fraud(txn)

    try:
        with engine.begin() as conn:  # ✅ Ensures transaction COMMIT
            conn.execute(text("""
                INSERT INTO transactions (account_id, transaction_type, amount, timestamp, is_fraud)
                VALUES (:account_id, :transaction_type, :amount, :timestamp, :is_fraud)
            """), {
                "account_id": txn["account_id"],
                "transaction_type": txn["transaction_type"],
                "amount": txn["amount"],
                "timestamp": datetime.fromisoformat(txn["timestamp"]),
                "is_fraud": fraud
            })
        print(f"✅ Stored transaction for account {txn['account_id']}, Fraud: {fraud}")
    except Exception as e:
        print(f"❌ Error inserting transaction: {e}")

