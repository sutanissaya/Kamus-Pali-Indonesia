import streamlit as st
from streamlit.logger import get_logger
from streamlit.hello.utils import show_code
import altair as alt
import numpy as np
import pandas as pd

LOGGER = get_logger(__name__)

st.set_page_config(page_title="Dictionary Test", page_icon="🌴")

word_input = st.text_input(label='Search for a word:', placeholder='Type here')
    

thisdict = {
    "entry": "amsa",
    "definition": "m.  bahu (<i>aṁse karoti</i>  meletakkan di bahu, menyandang, memanggul, memikul); bagian, hal berbagi; sudut, penjuru, ujung, tepi; <b>~kūṭa</b> m. nt. pundak, bahu."
}


for x in thisdict:
  st.write(x)

thisdict2 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]

st.write(thisdict2["brand"])
st.write(type(thisdict2))


st.write(thisdict)


# Help: st.write(type(thisdict))
# Show number of entries: st.write(len(thisdict))
