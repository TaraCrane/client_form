import streamlit
import snowflake.connector
import pandas

streamlit.title('Client Form')
streamlit.header('Project Data Collection')

  # Connect to Snowflake
streamlit.header("Clients:")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select client_name from clients")
my_data_rows = my_cur.fetchall()
streamlit.dataframe(my_data_rows)
streamlit.list(my_data_rows)

  # Add a pick list to pick the client
# client_selected = streamlit.multiselect("Pick a client:", list(my_data_rows.index))
# client_to_show = get_client_list.loc[client_selected]


# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT client_name FROM clients")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# # Snowflake related functions
# def get_client_list():
#     with my_cnx.cursor() as my_cur:
#          my_cur.execute("SELECT client_name FROM clients")
#          return my_cur.fetchall()
        

        
# try:
#   client_choice = streamlit.text_input('What client would you like information about?')
#   if not client_choice:
#       streamlit.error("Please select a client to get information.")
#   else:
#     back_from_function = get_client_list(client_choice)
#     streamlit.dataframe(back_from_function)
# except URLError as e:
#     streamlit.error()
# streamlit.write('The user entered ', fruit_choice)
        
