import os
from psycopg_pool import ConnectionPool

DATABASE_URL = os.getenv("DATABASE_URL")

pool = ConnectionPool(
    conninfo=DATABASE_URL,
    min_size=1,
    max_size=10,
)

def get_connection():
    return pool.connection()