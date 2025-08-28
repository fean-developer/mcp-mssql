# MCP MSSQL Server

Este projeto implementa um servidor MCP (Model Context Protocol) em Python para interagir com bancos de dados SQL Server.

## Requisitos
- Python 3.10+
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- pyodbc
- SQL Server acessível

## Instalação
1. Crie e ative um ambiente virtual Python:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install mcp[cli] pyodbc
   ```

## Configuração
Defina as variáveis de ambiente para conexão com o SQL Server:
- `MSSQL_SERVER` (ex: localhost)
- `MSSQL_DATABASE` (ex: master)
- `MSSQL_USER` (ex: sa)
- `MSSQL_PASSWORD` (ex: sua_senha)
- `MSSQL_DRIVER` (ex: ODBC Driver 18 for SQL Server)

## Uso
Execute o servidor MCP:
```bash
uv run mcp_mssql_server.py
```

O servidor expõe a ferramenta `run_query`, que executa comandos SQL recebidos via MCP.

## Integração
Configure o arquivo `.vscode/mcp.json` para integração com VS Code, Claude ou outros clientes MCP.

## Segurança
- Nunca exponha credenciais em código-fonte.
- Use variáveis de ambiente para senhas e dados sensíveis.
- Siga as práticas recomendadas do MCP para logs e segurança.

## Referências
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Documentação MCP](https://modelcontextprotocol.io/)
- [Exemplo de servidores MCP](https://github.com/modelcontextprotocol/servers)
