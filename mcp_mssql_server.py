from typing import Any
from mcp.server.fastmcp import FastMCP

from mcp.server.fastmcp import FastMCP
from instructions import instructions

# Import absoluto para evitar problemas de importação
from tools import run_query
from resources import list_tables, insert_record, update_record, db_schema

# MCP server instance com instruções
mcp = FastMCP(name="mcp-mssql", instructions=instructions)


# Tool: executar query arbitrária
@mcp.tool()
def run_query_tool(query: str):
    """Executa uma consulta SQL no banco de dados SQL Server."""
    return run_query(query)

# Tool: inserir registro
@mcp.tool()
def insert_record_tool(table: str, values: dict):
    """Insere um novo registro em uma tabela do SQL Server."""
    return insert_record(table, values)

# Tool: atualizar registro
@mcp.tool()
def update_record_tool(table: str, values: dict, where: dict):
    """Atualiza um registro em uma tabela do SQL Server."""
    return update_record(table, values, where)

# Tool: listar tabelas
@mcp.tool()
def list_tables_tool():
    """Lista todas as tabelas do banco de dados SQL Server."""
    return list_tables()

# Resource: esquema do banco
@mcp.resource(name="db_schema", mime_type="application/json", uri="mcp://sqlserver/schema")
def db_schema_resource():
    """Retorna o esquema atual do banco de dados (tabelas e colunas)."""
    return db_schema()

if __name__ == "__main__":
    mcp.run(transport="stdio")
