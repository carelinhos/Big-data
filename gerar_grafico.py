import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine, text
banco_de_dados = 'Vista_Serrana.db'
engine = create_engine(f'sqlite:///{banco_de_dados}')
query = ("SELECT Nome,data_entrada,Nova_quantidade,quantidade_atual FROM Produtos")
df = pd.read_sql(query, engine)



fig = px.bar(
    df,
    x="Nome",
    y="data_entrada",
    color="quantidade_atual",

)




fig.show()