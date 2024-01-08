import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Vrindhavan")

col1, col2 = st.columns(2)
with col1:
  st.subheader("krishna")
  st.image("./me1.jpeg", caption="Krishna ", width=300,use_column_width=True)
  st.write("krishna")
with col2:
  st.subheader("krishna")
  st.image("./me2.jpeg", caption="Krishna", width=300,use_column_width=True)
  st.write("krishna")
