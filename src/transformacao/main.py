# Vamos importar o que precisamos
import pandas as pd
import sqlite3
from datetime import datetime

# Ler os dados do arquivo JSONL

df = pd.read_json('../data/data.jsonl', lines=True)

# Setar o pandas para mostrar todas as colunas
pd.options.display.max_columns = None

# Exibir o DataFrame resultante
# print(df)

# Adicionar a coluna_source com um valor fixo
df['_source'] = "https://lista.mercadolivre.com.br/iphone-16"

# Adicionar a coluna _data_coleta com data e hora atuais
df['_data_coleta'] = datetime.now()

# Tratar os valores nulos para colunas numéricas e de texto
# df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float) Caso tenha centavos seria tratado como tipo float
# df['old_price_cent'] = df['old_price_cent'].fillna(0).astype(float) Caso tenha centavos seria tratado como tipo float
df['old_price'] = df['old_price'].fillna(0).astype(int)
df['new_price'] = df['new_price'].fillna(0).astype(int)

# Remover os parênteses das colunas 'reviews_amount' -> no meu caso não precisa, mas irei deixar comentado
# df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
# df['questions_amount'] = df['questions_amount'].fillna('0').astype(int)

# Tratar os preços como floats e calcular os valores totais
# df['old_preco'] = df['old_price_reais'] + df['old_price_cent'] / 100
# df['new_preco'] = df['new_price_reais'] + df['new_price_cent'] / 100 

# Remover as colunas antigas de preços
# df = df.drop(columns=['old_price_reais', 'old_price_cent', 'new_price_reais', 'new_price_cent'])

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect('../data/produtos.db')

# Salvar o DataFrame no banco de dados SQLite
df.to_sql('produtos', conn, if_exists='replace', index=False)


#Fechar a conexão com o banco de dados
conn.close()

print(df.head())