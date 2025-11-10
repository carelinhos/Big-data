import sqlite3

conn = sqlite3.connect('Vista_Serrana.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT,
    unidade_medida TEXT,
    Nova_quantidade INTEGER,
    Custo_unitario REAL,
    quantidade_atual REAL,
    data_entrada TEXT,
    quantidade_minima REAL,
    Custo_Total REAL,
    TOTAL_CMV REAL
);
""")







conn.commit()
conn.close()