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
