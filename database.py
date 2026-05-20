import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """
    Connect using DATABASE_URL (provided by Neon, Supabase, Railway, etc.)
    Format: postgresql://user:password@host/dbname?sslmode=require
    """
    database_url = os.getenv("DATABASE_URL")

    if database_url:
        conn = psycopg2.connect(database_url, sslmode="require")
    else:
        # Fallback to individual variables for local development
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME", "hotel_db"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", ""),
        )

    return conn
