import streamlit as st
from streamlit.logger import get_logger
from streamlit.hello.utils import show_code
import altair as alt
import numpy as np
import pandas as pd

LOGGER = get_logger(__name__)

st.set_page_config(page_title="Dictionary Test", page_icon="🌴")

word_input = st.text_input(label='Search for a word:', placeholder='Type here')

palidict = { "amsa" :{
    "definition": "m.  bahu (<i>aṁse karoti</i>  meletakkan di bahu, menyandang, memanggul, memikul); bagian, hal berbagi; sudut, penjuru, ujung, tepi; <b>~kūṭa</b> m. nt. pundak, bahu."
  },
  "akal" :{
    "definition": "a.  sakit, tak sehat."
  }}
# st.write(palidict[word_input]["definition"])

for n, info in palidict.items():
    st.write("\nword:", n)
    
    for key in info:
        st.write(key + ':', info[key])
        


# using setdefault() when key is non-existing 
word_not_found = palidict.setdefault('Definition', "Word not in the dictionary") 
st.write("Definition:", word_not_found) 





#y = palidict["entry"]
#st.write(y)

#st.write(palidict["entry"])
#st.write(type(palidict))


# x = car.keys()

# st.write(x) #before the change

# car["year"] = 2020

# st.write(x) #after the change 
# st.write(car['brand'])




# Help: st.write(type(thisdict))
# Show number of entries: st.write(len(thisdict))
