import logging
import os
import pyodbc
from typing import Any
from mcp.server.fastmcp import FastMCP

# Configure logging to stderr
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-mssql")

# SQL Server connection settings (use environment variables for security)
SQL_SERVER = os.getenv("MSSQL_SERVER", "localhost")
SQL_DATABASE = os.getenv("MSSQL_DATABASE", "master")
SQL_USER = os.getenv("MSSQL_USER", "sa")
SQL_PASSWORD = os.getenv("MSSQL_PASSWORD", "yourStrong(!)Password")
SQL_DRIVER = os.getenv("MSSQL_DRIVER", "ODBC Driver 18 for SQL Server")

# MCP server instance
mcp = FastMCP("mcp-mssql")

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

@mcp.tool()
def run_query(query: str):
    """Executa uma consulta SQL no banco de dados SQL Server e retorna os resultados."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            if cursor.description:
                columns = [col[0] for col in cursor.description]
                rows = cursor.fetchall()
                result = [dict(zip(columns, row)) for row in rows]
                return result
            else:
                conn.commit()
                return "Comando executado com sucesso."
    except Exception as e:
        logger.error(f"Erro ao executar consulta: {e}")
        return f"Erro: {e}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
