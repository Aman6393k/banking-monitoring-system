from kafka import KafkaConsumer
import json
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="transactions",
    user="admin",
    password="admin"
)
cursor = conn.cursor()

# Define rule-based fraud detection logic
def is_fraudulent(transaction):
    # Example rule: flag transaction as fraud if amount > 1000
    return 1 if transaction['amount'] > 1000 else 0

# Create Kafka consumer
consumer = KafkaConsumer(
    'bank-transactions',  # Make sure this topic name matches your producer
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("✅ Kafka Consumer started... Listening for transactions.")

# Consume messages
for message in consumer:
    transaction = message.value

    transaction_id = transaction['transaction_id']
    timestamp = transaction['timestamp']
    amount = transaction['amount']
    sender_account = transaction['sender_account']
    receiver_account = transaction['receiver_account']
    location = transaction['location']

    # Apply fraud detection logic
    fraud = is_fraudulent(transaction)

    # Insert into PostgreSQL
    cursor.execute("""
        INSERT INTO transactions (transaction_id, timestamp, amount, sender_account, receiver_account, location, is_fraud)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (transaction_id, timestamp, amount, sender_account, receiver_account, location, fraud))

    conn.commit()
    print(f"📥 Transaction {transaction_id} inserted - Fraud: {fraud}")
from kafka import KafkaConsumer
import json
import psycopg2

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

conn = psycopg2.connect(
    host="localhost",
    database="transactions",
    user="admin",
    password="admin"
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id UUID PRIMARY KEY,
    timestamp TIMESTAMP,
    amount FLOAT,
    sender_account TEXT,
    receiver_account TEXT,
    location TEXT,
    is_fraud INT
)
""")
conn.commit()

for message in consumer:
    data = message.value
    cursor.execute("""
        INSERT INTO transactions (transaction_id, timestamp, amount, sender_account, receiver_account, location, is_fraud)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (transaction_id) DO NOTHING
    """, (
        data['transaction_id'], data['timestamp'], data['amount'],
        data['sender_account'], data['receiver_account'],
        data['location'], data['is_fraud']
    ))
    conn.commit()
    print(f"Consumed and stored: {data}")

