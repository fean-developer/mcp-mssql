import logging
from db import get_connection
from instructions import PROTECTED_TABLES, PROHIBITED_CMDS

def run_query(query: str):
    """Executa uma consulta SQL no banco de dados SQL Server e retorna os resultados."""
    logger = logging.getLogger("mcp-mssql")
    upper_query = query.upper()
    for cmd in PROHIBITED_CMDS:
        if cmd in upper_query:
            for table in PROTECTED_TABLES:
                if table.upper() in upper_query:
                    return f"Operação proibida: não é permitido {cmd} na tabela protegida '{table}'."
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
