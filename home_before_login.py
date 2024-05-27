import streamlit as st
import streamlit.components.v1 as components

st.header("노세노세", divider='orange')
st.text("slogan, 노년을 행복하게")

col1, col2 =st.columns(2)
with col1: 
    st.header("일자리를 구하고 신가요?")
    st.text("discription")
with col2:    
    st.image("images/sundayafternoon.jpg")

st.text("From cradle to grave service")
col1,col2,col3,col4,col5= st.columns(5)
with col1:
    st.header("어린이")
    st.text("description")
with col2:
    st.header("노인")
    st.text("description")
with col3:
    st.header("연구소")
    st.text("description")
with col4:
    st.header("기업")
    st.text("description")
with col5:
    st.header("군인")
    st.text("description")

st.markdown("""---""")

col1, col2 =st. columns(2)
with col1:
    st.text("join with us")
with col2:
    st.text("have you ever login?")

col1, col2 =st. columns(2)
with col1: 
    st.page_link("pages/join.py", label="회원가입")
with col2:
    st.page_link("pages/login.py", label="로그인")