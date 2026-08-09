import pandas as pd
from sqlalchemy import create_engine


DATABASE_URL = "postgresql+psycopg2://0megaad@localhost:5432/sales_analytics"

engine = create_engine(DATABASE_URL)


def read_query(query, params=None):
    """
    Executa uma consulta SQL e retorna um DataFrame.
    """

    return pd.read_sql(
        query,
        engine,
        params=params
    )