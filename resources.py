from db import get_connection

def list_tables():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        return [row[0] for row in cursor.fetchall()]

def insert_record(table: str, values: dict):
    cols = ', '.join(values.keys())
    placeholders = ', '.join(['?' for _ in values])
    sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, list(values.values()))
        conn.commit()
        return "Registro inserido com sucesso."

def update_record(table: str, values: dict, where: dict):
    set_clause = ', '.join([f"{k} = ?" for k in values.keys()])
    where_clause = ' AND '.join([f"{k} = ?" for k in where.keys()])
    sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, list(values.values()) + list(where.values()))
        conn.commit()
        return "Registro atualizado com sucesso."

def db_schema():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS")
        rows = cursor.fetchall()
        schema = {}
        for table, column, dtype in rows:
            schema.setdefault(table, []).append({'column': column, 'type': dtype})
        return schema
