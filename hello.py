import streamlit as st

st.write("""
# Hello
hello *world*!
""")

number = st.slider('number')
st.write(number)

col1, col2 = st.columns(2)

with col1:
    st.write('## col1')
    checkbox = st.checkbox('checkbox')
    st.write(checkbox)

with col2:
    st.write('## col2')
    option = st.radio('option', ('a', 'b'))
    st.write(option)
