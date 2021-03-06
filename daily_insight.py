import streamlit as st
import os, sys
from streamlit import caching
st.set_page_config(layout="wide")

def home_page():
  st.markdown("""# HK Daily/Hourly Weather Insight
  ---
  Relevant Link:

  HK Weather Summary Web App: https://share.streamlit.io/tions-icu/hk_rain_report/main/hk_rain.py
  
  """)
@st.cache
def installff():
  os.system('sbase install geckodriver')
  os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

try:
  from daily_weather import daily_weather
  from regional_rain import region_rain
  from selenium import webdriver
  from selenium.webdriver import FirefoxOptions
  opts = FirefoxOptions()
  opts.add_argument("--headless")
  import matplotlib.pyplot as plt
  import pandas as pd
  from bs4 import BeautifulSoup
  import time
  import matplotlib.dates as mdates
  to_func = {
    "Home": home_page,
    "Daily Weather": daily_weather,  
    "Hourly Regional Rainfall":region_rain,
  }

  with st.sidebar:
    demo_name = st.selectbox("Applications", to_func.keys())
  to_func[demo_name]()

except Exception as e:
  st.title("Error Encountered")
  st.write(e)
  if st.button('Try Resolving by resetting the Web Driver'):
    _ = installff()
    st.experimental_rerun()
