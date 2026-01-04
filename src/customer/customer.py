from db.connection import get_connection

def get_customers():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, full_name, email, created_at FROM customers")
            return cur.fetchall()

def get_customer_by_id(customer_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, full_name, email, created_at FROM customers WHERE id = %s",
                (customer_id,)
            )
            return cur.fetchone()

def create_customer(full_name, email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO customers (full_name, email) VALUES (%s, %s)",
                (full_name, email)
            )
        conn.commit()

def delete_customer(customer_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM customers WHERE id = %s",
                (customer_id,)
            )
        conn.commit()