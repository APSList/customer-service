import logging
import os

from psycopg_pool import ConnectionPool
import hvac

logger = logging.getLogger(__name__)

HASHICORP_VAULT_ADDR = os.environ.get('HASHICORP_VAULT_ADDR')
HASHICORP_VAULT_TOKEN = os.environ.get('HASHICORP_VAULT_TOKEN')

client = hvac.Client(
    url=HASHICORP_VAULT_ADDR,
    token=HASHICORP_VAULT_TOKEN,
    namespace='admin'
)

read_response = client.secrets.kv.read_secret_version(path='/database')

CUSTOMER_DB_URL = read_response['data']['data']['CUSTOMER_DB_URL']

if not CUSTOMER_DB_URL:
    logger.warning("CUSTOMER_DB_URL is not configured in environment or Vault; ConnectionPool may fail to initialize")


pool = ConnectionPool(
    conninfo=CUSTOMER_DB_URL,
    min_size=1,
    max_size=10,
)

def get_connection():
    return pool.connection()