import pandas as pd


arquivo = "data/raw/Online Retail.xlsx"

dados = pd.read_excel(arquivo)

negativos = dados[dados["Quantity"] < 0]

preco_zero = dados[dados["UnitPrice"] == 0]

negativos_sem_c = dados[
    (dados["Quantity"] < 0) &
    (~dados["InvoiceNo"].astype(str).str.startswith("C"))
]

vendas = dados[
    (dados["Quantity"] > 0) &
    (dados["UnitPrice"] > 0)
]

duplicados_vendas = vendas[vendas.duplicated(keep=False)]

vendas_sem_duplicados = vendas.drop_duplicates()

unidades = vendas_sem_duplicados["Quantity"].sum()

receita = (
    vendas_sem_duplicados["Quantity"] *
    vendas_sem_duplicados["UnitPrice"]
).sum()

print("Unidades vendidas:", unidades)
print("Receita total:", receita)
round(receita, 2)
ticket_medio = receita / vendas_sem_duplicados["InvoiceNo"].nunique()

print("Ticket médio:", round(ticket_medio, 2))
print("Primeira data:", vendas_sem_duplicados["InvoiceDate"].min())
print("Última data:", vendas_sem_duplicados["InvoiceDate"].max())
print(
    "Dias no período:",
    (
        vendas_sem_duplicados["InvoiceDate"].max()
        - vendas_sem_duplicados["InvoiceDate"].min()
    ).days
)