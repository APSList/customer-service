from db.connection import get_connection

def get_customers():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, full_name, email, created_at, organization_id FROM customers")
            return cur.fetchall()

def get_customer_by_id(customer_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, full_name, email, created_at, organization_id FROM customers WHERE id = %s",
                (customer_id,)
            )
            return cur.fetchone()

def create_customer(full_name, email, organization_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO customers (full_name, email, organization_id) VALUES (%s, %s, %s)",
                (full_name, email, organization_id)
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