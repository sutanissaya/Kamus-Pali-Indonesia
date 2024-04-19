import streamlit as st
from streamlit.logger import get_logger
from streamlit.hello.utils import show_code
import altair as alt
import numpy as np
import pandas as pd

LOGGER = get_logger(__name__)

st.set_page_config(page_title="Dictionary Test", page_icon="🌴")


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict2 = dict(name = "John", age = 36, country = "Norway")


#
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

st.write(x) #before the change

car["year"] = 2020

st.write(x) #after the change 


#

st.write(thisdict)

st.write(thisdict2)
# Help: st.write(type(thisdict))
# Show number of entries: st.write(len(thisdict))
