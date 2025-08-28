# Instruções e listas de proteção para o MCP
instructions = """
NUNCA execute comandos que deletem, alterem ou esvaziem tabelas protegidas como 'customers', 'MSreplication_options' ou 'usuarios'.
Bloqueie qualquer comando DROP, DELETE ou TRUNCATE nessas tabelas.
"""

PROTECTED_TABLES = ["customers", "MSreplication_options", "usuarios"]
PROHIBITED_CMDS = ["DROP TABLE", "DELETE FROM", "TRUNCATE TABLE"]
 