import streamlit as st
import pandas as pd

from src.database import read_query
from src.queries import (
    get_countries,
    get_kpis,
    get_monthly_sales,
    get_top_products,
    get_customer_rfm
)

# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Sales Analytics",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# TÍTULO
# ============================================================

st.title("Sales Analytics")
st.caption("Online Retail Dataset")


# ============================================================
# PAÍSES
# ============================================================

countries = read_query(
    get_countries(),
)["country"].tolist()


selected_country = st.selectbox(
    "País",
    ["Todos"] + countries
)


# ============================================================
# PARÂMETROS
# ============================================================

if selected_country == "Todos":

    country = None
    params = {}

else:

    country = selected_country
    params = {
        "country": selected_country
    }


# ============================================================
# KPIs
# ============================================================

kpis = read_query(
    get_kpis(country),
    params=params
)


total_revenue = kpis["total_revenue"].iloc[0]
total_quantity = kpis["total_quantity"].iloc[0]
total_orders = kpis["total_orders"].iloc[0]


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Receita Total",
        f"£{total_revenue:,.2f}"
    )


with col2:

    st.metric(
        "Unidades Vendidas",
        f"{total_quantity:,.0f}"
    )


with col3:

    st.metric(
        "Pedidos",
        f"{total_orders:,}"
    )


# ============================================================
# RECEITA MENSAL
# ============================================================

monthly_sales = read_query(
    get_monthly_sales(country),
    params=params
)


# ============================================================
# TOP PRODUTOS
# ============================================================

top_products = read_query(
    get_top_products(country),
    params=params
)


# ============================================================
# GRÁFICOS
# ============================================================

col1, col2 = st.columns(2)


with col1:

    st.subheader("Receita Mensal")

    st.line_chart(
        monthly_sales,
        x="period",
        y="total_revenue"
    )


with col2:

    st.subheader("Top 10 Produtos")

    st.bar_chart(
        top_products.set_index("description")["total_revenue"]
    )


# ============================================================
# PRODUTOS
# ============================================================

st.subheader("Top 10 Produtos em Detalhes")

st.dataframe(
    top_products,
    use_container_width=True
)


# ============================================================
# RFM
# ============================================================

st.subheader("Segmentação de Clientes")


customer_rfm = read_query(
    get_customer_rfm(country),
    params=params
)


# ============================================================
# RESUMO DOS SEGMENTOS
# ============================================================

segment_summary = (
    customer_rfm
    .groupby("customer_segment")
    .agg(
        customers=("customer_id", "count"),
        revenue=("monetary", "sum")
    )
    .reset_index()
    .sort_values(
        "revenue",
        ascending=False
    )
)


st.dataframe(
    segment_summary,
    use_container_width=True
)


# ============================================================
# RECEITA POR SEGMENTO
# ============================================================

st.bar_chart(
    segment_summary.set_index("customer_segment")["revenue"]
)