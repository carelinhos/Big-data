import sqlite3
import pandas as pd


conn = sqlite3.connect('Vista_Serrana.db')


df = pd.read_sql("""
    SELECT
  data_entrada
        
    FROM Produtos;
""", conn)

print(df)



conn.close()