import streamlit
import snowflake.connector

streamlit.title('Client Form')
streamlit.header('Project Data Collection')

  # Connect to Snowflake
streamlit.header("Clients:")
# Snowflake related functions
def get_client_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT client_name FROM clients")
         return my_cur.fetchall()
