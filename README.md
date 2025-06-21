💳 Real-Time Banking Transaction Monitoring System
A dynamic and real-time fraud detection dashboard for banking transactions built with Streamlit, Kafka, PostgreSQL, and Python. This project simulates real-time transaction streams, detects fraudulent behavior using custom rules, and visualizes everything in an interactive dashboard.

🔢 Features
* ✅ Real-time ingestion of banking transactions using Kafka
* 🤠 Fraud detection using custom rule-based logic
* 🔢 PostgreSQL database integration to persist all transactions
* 📈 Live dashboard built with Streamlit
* 📊 Visuals and charts (Altair & Matplotlib)
* 📆 Time-based transaction history
* ⚠️ Fraud detection table with alerts

📅 Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	Python
Messaging	Apache Kafka
Database	PostgreSQL
Visualization	Altair, Matplotlib
📊 Dashboard Preview

🚀 Getting Started
1. Clone the Repo
git clone https://github.com/your-username/banking-monitoring-system.git
cd banking-monitoring-system
2. Install Requirements
pip install -r requirements.txt
3. Start Kafka and PostgreSQL
* Ensure PostgreSQL is running and the database is created.
* Ensure Kafka broker is running on localhost:9092.
4. Start the Kafka Producer
python kafka_producer.py
5. Start the Kafka Consumer
python kafka_consumer.py
6. Launch the Streamlit Dashboard
streamlit run streamlit_app.py

🛋️ Fraud Rules Logic
Fraud is detected using simple conditions like:
* Large transactions (e.g., over 10,000)
* Suspicious transaction types (e.g., frequent transfers)
You can customize rules in fraud_rules.py.

🚫 Limitations (for Streamlit Cloud)
Streamlit Cloud does not support Kafka or local PostgreSQL. To deploy online:
* Replace real-time streams with static demo data
* OR deploy with full backend (Docker + VPS/Cloud DB)

🚜 Contributing
Pull requests are welcome! For major changes, please open an issue first.

🌟 Author
Aman Kashyap GitHub Profile

📄 License
This project is licensed under the MIT License.

Enjoy monitoring 🚀

