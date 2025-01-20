from psycopg2 import connect
from psycopg2.extras import register_default_jsonb
from os import getenv
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = getenv("DATABASE_URL")

def get_db_connection():
    conn = connect(DATABASE_URL)
    conn.autocommit = True
    return conn