import os
from psycopg_pool import ConnectionPool

CUSTOMER_DB_URL = os.getenv("CUSTOMER_DB_URL")

pool = ConnectionPool(
    conninfo=CUSTOMER_DB_URL,
    min_size=1,
    max_size=10,
)

def get_connection():
    return pool.connection()