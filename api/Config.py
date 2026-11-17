import os
from dotenv import load_dotenv
from MySQLdb.constants import CLIENT
load_dotenv()

class Config:

    MYSQL_HOST      = os.getenv('MYSQL_HOST')
    MYSQL_USER      = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD  = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB        = os.getenv('MYSQL_DB')
    MYSQL_PORT      = int(os.getenv('MYSQL_PORT', 3306))
    # FOUND_ROWS: en un UPDATE, rowcount cuenta las filas encontradas y no solo
    # las modificadas. Sin esto, guardar un registro sin cambios daba 404.
    MYSQL_CUSTOM_OPTIONS = {"client_flag": CLIENT.FOUND_ROWS}
    MYSQL_SSL = {
        "ca": "/etc/secrets/aiven-ca.pem"
    }
