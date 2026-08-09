import pandas as pd


arquivo = "data/raw/Online Retail.xlsx"

dados = pd.read_excel(arquivo)

dados = dados[dados["Quantity"] > 0]

dados = dados[dados["UnitPrice"] > 0]


dados = dados.drop_duplicates()

dados["CustomerID"] = dados["CustomerID"].astype("Int64")

dados["Revenue"] = dados["Quantity"] * dados["UnitPrice"]

dados["Year"] = dados["InvoiceDate"].dt.year
dados["Month"] = dados["InvoiceDate"].dt.month
dados["Day"] = dados["InvoiceDate"].dt.day

dados["Period"] = dados["InvoiceDate"].dt.to_period("M")


saida = "data/processed/sales_clean.csv"

dados.to_csv(saida, index=False)

print("Arquivo salvo em:", saida)