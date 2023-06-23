import streamlit
import snowflake.connector
import pandas

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("show views in SCHEMA ZENAS_ATHLEISURE_DB.products;")
my_data_rows = my_cur.fetchall()
streamlit.dataframe(my_data_rows)

my_cur.execute("select * from ZENAS_ATHLEISURE_DB.products.catalog_for_website")
my_catalog = my_cur.fetchall()
streamlit.dataframe(my_catalog)