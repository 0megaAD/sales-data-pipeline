# Sales Data Pipeline

Pipeline de dados desenvolvido em Python para processamento, análise e visualização de dados de vendas do **Online Retail Dataset**.

O projeto realiza a preparação dos dados, validação, armazenamento em PostgreSQL, consultas analíticas e disponibilização dos resultados através de um dashboard interativo desenvolvido com Streamlit.

## Objetivo

O objetivo do projeto é simular um fluxo de dados próximo ao encontrado em um ambiente real de análise de dados:

```text
Dados brutos
     ↓
Exploração
     ↓
Limpeza e validação
     ↓
Dados processados
     ↓
PostgreSQL
     ↓
Consultas SQL
     ↓
Python / Pandas
     ↓
Dashboard Streamlit
```

O projeto também busca demonstrar conhecimentos em **ETL, SQL, análise de dados, bancos relacionais e visualização**.

---

## Tecnologias

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* psycopg2
* Streamlit
* SQL
* Git

---

## Estrutura do projeto

```text
sales-data-pipeline/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── database.py
│   ├── queries.py
│   │
│   └── pipeline/
│       ├── clean.py
│       ├── explore.py
│       └── validate.py
│
└── sql/
    ├── 01_basic_analysis.sql
    ├── 02_sales_analysis.sql
    ├── 03_customer_rfm.sql
    └── 04_dashboard.sql
```

### Principais componentes

**`app.py`**

Aplicação Streamlit responsável pelo dashboard e interação com o usuário.

**`src/database.py`**

Gerencia a conexão com o PostgreSQL e a execução das consultas.

**`src/queries.py`**

Centraliza as consultas SQL utilizadas pela aplicação.

**`src/pipeline/`**

Contém os scripts utilizados durante as etapas de exploração, limpeza e validação dos dados.

**`sql/`**

Contém consultas utilizadas para análises exploratórias e métricas do projeto.

**`data/`**

Organiza os dados utilizados pelo pipeline.

---

## Tratamento dos dados

O dataset original possui **541.909 registros**.

Durante a preparação dos dados foram realizadas etapas de:

* identificação de valores nulos;
* identificação de registros duplicados;
* análise de valores negativos;
* identificação de cancelamentos;
* remoção de registros inválidos para análise de vendas;
* validação de preços;
* cálculo da receita;
* criação de informações temporais;
* remoção de duplicatas;
* validação dos dados processados.

Após o tratamento:

```text
Registros originais:              541.909
Registros após filtros:           530.104
Registros após duplicatas:        524.878
Receita total:                    £10.642.110,80
Unidades vendidas:                5.572.420
```

---

## Banco de dados

Os dados processados são armazenados em PostgreSQL.

Banco utilizado:

```text
sales_analytics
```

Tabela principal:

```text
sales
```

Principais campos:

```text
invoice_no
stock_code
description
quantity
invoice_date
unit_price
customer_id
country
revenue
year
month
day
period
```

A aplicação utiliza SQLAlchemy para realizar a comunicação entre Python e PostgreSQL.

---

## Análises

O projeto disponibiliza diferentes análises sobre as vendas.

### KPIs

O dashboard apresenta:

* Receita total
* Unidades vendidas
* Número de pedidos

### Receita mensal

A receita é agregada por período para analisar a evolução das vendas ao longo do tempo.

### Produtos

O dashboard apresenta os 10 produtos com maior receita, além de uma tabela detalhada.

### Análise por país

É possível selecionar um país e atualizar as métricas e análises do dashboard de acordo com a seleção.

### Segmentação RFM

O projeto também utiliza uma análise simplificada de **RFM (Recency, Frequency and Monetary Value)**.

Os clientes são analisados considerando:

* **Recency:** tempo desde a última compra;
* **Frequency:** quantidade de pedidos;
* **Monetary:** receita gerada pelo cliente.

Os clientes são classificados em segmentos:

```text
Recente
Ativo
Em risco
Inativo
```

---

## Dashboard

O dashboard foi desenvolvido utilizando Streamlit e possui:

* filtro por país;
* cards de indicadores;
* gráfico de receita mensal;
* ranking dos principais produtos;
* tabela de produtos;
* segmentação de clientes;
* análise de receita por segmento.

---

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/0megaAD/sales-data-pipeline.git
cd sales-data-pipeline
```

### 2. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

Ativar no macOS/Linux:

```bash
source .venv/bin/activate
```

No Windows:

```bash
.venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o PostgreSQL

Crie um banco chamado:

```text
sales_analytics
```

Depois configure a variável `DATABASE_URL` no arquivo `.env`:

```env
DATABASE_URL=postgresql+psycopg2://usuario:senha@localhost:5432/sales_analytics
```

O arquivo `.env` não deve ser enviado para o GitHub.

### 5. Executar o dashboard

```bash
python -m streamlit run app.py
```

O Streamlit disponibilizará o dashboard localmente.

---

## Resultados

O pipeline processou o dataset e gerou uma base analítica contendo:

* **524.878 registros válidos após tratamento e remoção de duplicatas**
* **5.572.420 unidades vendidas**
* **£10,64 milhões em receita**
* dados organizados em PostgreSQL;
* consultas SQL reutilizáveis;
* dashboard interativo;
* segmentação de clientes utilizando RFM.

---

## Próximos passos

Possíveis melhorias futuras:

* adicionar filtros por período;
* criar análise de crescimento mensal;
* adicionar ticket médio ao dashboard;
* melhorar a segmentação RFM utilizando scores;
* adicionar testes automatizados;
* criar uma camada de visualização mais avançada;
* containerizar a aplicação com Docker;
* disponibilizar o dashboard em ambiente cloud.

---

## Aprendizados

Este projeto foi desenvolvido como prática de integração entre diferentes etapas de um fluxo de dados, envolvendo:

```text
Python
   ↓
Pandas
   ↓
ETL
   ↓
PostgreSQL
   ↓
SQL
   ↓
SQLAlchemy
   ↓
Streamlit
```

O projeto também serviu para praticar organização de código, separação de responsabilidades, tratamento de dados e construção de uma aplicação analítica utilizando uma base de dados relacional.
