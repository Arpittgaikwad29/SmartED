import pymysql
import hashlib

def connect_to_database():
    return pymysql.connect(
        MYSQL_HOST="mysql-jxde.railway.internal.app",
        MYSQL_USER= "root",
        MYSQL_PASSWORD="FGJzjbMcvDYXDFgOslZDJsHjghNTRIql",
        MYSQL_DATABASE="railway",
        MYSQL_PORT=3306 ,
        cursorclass=pymysql.cursors.DictCursor
    )

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_password, provided_password):
    """Verify password"""
    return stored_password == hash_password(provided_password)