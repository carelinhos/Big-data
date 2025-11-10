import pandas as pd
arquivo = ('Fevereiro.xlsx')
df = pd.read_excel(arquivo)
print(df)
df2=df.copy()



from sqlalchemy import create_engine
banco_de_dados = 'Vista_Serrana.db'
engine = create_engine(f'sqlite:///{banco_de_dados}')


df2.columns = df2.columns.str.strip()
df2 = df2.rename(columns={
    'Custo Total (R$)': 'Custo_Total',
    'TOTAL':'TOTAL'
})
df2.insert(0, 'id_produto', range(1, len(df2) + 1))
df2.to_sql('Produtos', engine, if_exists='replace', index=False)