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
python mcp_mssql_server.py
```

## Tools expostas pelo MCP

O servidor expõe as seguintes ferramentas (tools) para interação ativa com o SQL Server:

- **run_query_tool**: Executa uma query SQL arbitrária e retorna os resultados.
   - Parâmetros: `{ "query": "SELECT * FROM usuarios" }`

- **insert_record_tool**: Insere um novo registro em uma tabela.
   - Parâmetros: `{ "table": "usuarios", "values": { "nome": "João", "email": "joao@email.com" } }`

- **list_tables_tool**: Lista todas as tabelas do banco de dados.
   - Parâmetros: nenhum

Você pode adicionar facilmente outras tools, como update, delete, get_record, describe_table, execute_stored_procedure, etc.

## Resources expostos pelo MCP

O servidor também expõe resources (fontes de contexto) que podem ser consultados por LLMs e agentes:

- **db_schema_resource**: Retorna o esquema atual do banco de dados (tabelas e colunas) em formato JSON.
   - URI: `mcp://sqlserver/schema`
   - MIME type: `application/json`

Outros resources podem ser implementados, como histórico de queries, documentação de stored procedures, regras de acesso, etc.

## O que o MCP pode fazer

- Executar queries SQL arbitrárias
- Inserir registros em qualquer tabela
- Listar tabelas do banco
- Expor o esquema do banco para consulta dinâmica
- Permitir extensão fácil para CRUD, procedures, transações, etc.
- Proteger tabelas críticas contra deleção/alteração

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
