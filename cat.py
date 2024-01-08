import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Cat1")
  st.image("./me1.jpeg", caption="Persian Cat", width=300,use_column_width=True)
  st.write("krishna")
with col2:
  st.subheader("Cat2")
  st.image("./me2.jpeg", caption="Ragdoll Cat", width=300,use_column_width=True)
  st.write("krishna")
