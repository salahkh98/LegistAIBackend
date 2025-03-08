import os
import sqlalchemy as sa
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = sa.engine.URL.create(
        "mssql+pyodbc",
        username=os.getenv("DB_USERNAME"),  # Get from .env file
        password=os.getenv("DB_PASSWORD"),  # Get from .env file
        host=os.getenv("DB_HOST"),  # Get from .env file
        database=os.getenv("DB_DATABASE"),  # Get from .env file
        query={
            "driver": os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server"),  # Default to ODBC Driver 18
            "Encrypt": os.getenv("DB_ENCRYPT", "no"),
            "TrustServerCertificate": os.getenv("DB_TRUST_CERT", "no"),
            "Connection Timeout": os.getenv("DB_TIMEOUT", "30")  # Default to 30 if not set
        }
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")  # For session security
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # For JWT
