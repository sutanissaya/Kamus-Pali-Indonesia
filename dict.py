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
print(thisdict)
