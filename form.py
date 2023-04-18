import streamlit
import snowflake.connector

streamlit.title('Client Form')
streamlit.header('Project Data Collection')

  # Connect to Snowflake
streamlit.header("Clients:")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT client_name FROM clients")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

# # Snowflake related functions
# def get_client_list():
#     with my_cnx.cursor() as my_cur:
#          my_cur.execute("SELECT client_name FROM clients")
#          return my_cur.fetchall()
        
#   # Add a pick list to pick the client
# client_selected = streamlit.select("Pick a client:", list(get_client_list.index))
# client_to_show = get_client_list.loc[client_selected]
        
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
        
