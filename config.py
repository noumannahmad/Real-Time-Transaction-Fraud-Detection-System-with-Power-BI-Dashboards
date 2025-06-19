# config.py

# Configuration for MySQL Database Connection

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',  # <-- Replace with your actual MySQL password
    'database': 'fraud',
    'port': 3310,  # Adjust port if your MySQL server uses a different one
    'auth_plugin': 'mysql_native_password'
}
