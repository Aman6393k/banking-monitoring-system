# db.py

from sqlalchemy import create_engine

# ✅ Update with your actual password
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/banking"

engine = create_engine(DATABASE_URL)

