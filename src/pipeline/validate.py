import pandas as pd


arquivo = "data/processed/sales_clean.csv"

dados = pd.read_csv(arquivo)

print("Registros:", len(dados))
print("Colunas:", len(dados.columns))

print("\nValores nulos:")
print(dados.isnull().sum())

print("\nQuantidade mínima:")
print(dados["Quantity"].min())

print("\nPreço mínimo:")
print(dados["UnitPrice"].min())

print("\nReceita mínima:")
print(dados["Revenue"].min())

print("\nReceita total:")
print(round(dados["Revenue"].sum(), 2))