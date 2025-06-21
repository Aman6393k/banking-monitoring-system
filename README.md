# 💳 Real-Time Banking Transaction Monitoring System

A real-time fraud detection system designed to monitor banking transactions, detect anomalies using rule-based logic, and display alerts with an interactive Streamlit dashboard.

This project simulates how modern banks flag suspicious transactions as they happen — integrating **Apache Kafka**, **PostgreSQL**, **Python**, and **Streamlit**.

---

## 🧠 Project Highlights

- ⚡ **Real-time fraud detection** via Kafka consumers
- 🧾 **Rule-based logic** to flag high-risk transactions
- 📊 **Interactive dashboard** with real-time updates
- 🛢 **PostgreSQL integration** for storing transactions
- 🔌 **Scalable architecture** for future ML integration

---

## 🚀 Tech Stack

| Tool          | Purpose                             |
|---------------|-------------------------------------|
| 🐍 Python      | Backend and logic                   |
| 🧪 Streamlit   | Real-time interactive dashboard      |
| 🐘 PostgreSQL  | Persistent transaction storage       |
| ⚙️ Kafka       | Real-time data streaming             |
| 🧠 SQLAlchemy  | Python ORM to manage DB operations   |
| 🔐 psycopg2    | PostgreSQL adapter for Python        |

---

## 📂 Folder Structure

# banking-monitoring-system
Real-time fraud detection system using Kafka, PostgreSQL, and Streamlit
banking-monitoring-system/
│
├── app.py # Streamlit dashboard
├── kafka_producer.py # Simulates & sends transactions
├── kafka_consumer.py # Consumes data & applies fraud rules
├── fraud_rules.py # Rule-based logic for fraud detection
├── db.py # PostgreSQL connection utility
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## 🔍 Fraud Detection Rules

Currently, these basic fraud rules are implemented:

- 🚨 Flag any transaction **above ₹10,000**
- 🔁 Flag if **more than 3 transactions** occur within **1 minute**
- 📍 (Upcoming) Add rules for location/IP anomaly detection

These rules are defined in `fraud_rules.py`.

---

## 🛠 Setup & Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Aman6393k/banking-monitoring-system.git
cd banking-monitoring-system

2. Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Python Dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. Ensure Kafka & PostgreSQL Are Running
Make sure Kafka and PostgreSQL services are active and credentials are updated in db.py.

5. Run the System
In 3 separate terminals:

bash
Copy
Edit
# Terminal 1: Run Kafka Producer
python kafka_producer.py

# Terminal 2: Run Kafka Consumer
python kafka_consumer.py

# Terminal 3: Launch Streamlit Dashboard
streamlit run app.py
