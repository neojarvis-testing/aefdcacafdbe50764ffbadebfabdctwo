import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost"
        "DATABASE={db_name};"
        "UID=sa;"
        "PWD=examlyMssql@123;"
    )
    return conn
