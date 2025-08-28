import os
import pyodbc

# SQL Server connection settings (use environment variables for security)
SQL_SERVER = os.getenv("MSSQL_SERVER", "localhost")
SQL_DATABASE = os.getenv("MSSQL_DATABASE", "master")
SQL_USER = os.getenv("MSSQL_USER", "sa")
SQL_PASSWORD = os.getenv("MSSQL_PASSWORD", "yourStrong(!)Password")
SQL_DRIVER = os.getenv("MSSQL_DRIVER", "ODBC Driver 18 for SQL Server")

def get_connection():
    conn_str = (
        f"DRIVER={{{SQL_DRIVER}}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USER};"
        f"PWD={SQL_PASSWORD};"
        f"TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)
