import streamlit
import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Client Form')
streamlit.header('Project Data Collection')

  # Connect to Snowflake
streamlit.header("Clients:")

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("select client_name from clients")
# my_data_rows = my_cur.fetchall()
# client_list = streamlit.dataframe(my_data_rows)

streamlit.text('trying chatgpt 16:30')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
cursor = my_cnx.cursor()
cursor.execute('SELECT client_name FROM clients')
client_names = [row[0] for row in cursor.fetchall()]

# Display the list of client names in a Streamlit dropdown
selected_client_name = st.selectbox('Select a client', client_names)

# Allow the user to add a new client name
new_client_name = st.text_input('Enter a new client name')
if new_client_name:
    # Check if the client name already exists in the "clients" table
    exists = False
    for name in client_names:
        if new_client_name.strip().lower() == name.strip().lower():
            exists = True
            break
    
    if exists:
        st.error('Client already exists. Please select from the list.')
    else:
        if st.button('Add client'):
            # Insert the new client name into the "clients" table
            cursor.execute("INSERT INTO clients (client_name) VALUES ('{}')".format(new_client_name))
            # Commit the changes
            conn.commit()
            st.success('Client added successfully')
            # Refresh the list of client names
            cursor.execute('SELECT client_name FROM clients')
            client_names = [row[0] for row in cursor.fetchall()]


  # Add a pick list to pick the client
# client_selected = streamlit.multiselect("Pick a client:", list(my_data_rows.index))
# client_to_show = get_client_list.loc[client_selected]


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
        
