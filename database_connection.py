import pymysql
import hashlib
from config import DB_CONFIG

def connect_to_database():
    return pymysql.connect(
        host='trolley.proxy.rlwy.net',
        port=32851,
        user='root',
        password='FGJzjbMcvDYXDFgOslZDJsHjghNTRIql',
        database='railway',
        cursorclass=pymysql.cursors.DictCursor
    )

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_password, provided_password):
    """Verify password"""
    return stored_password == hash_password(provided_password)
