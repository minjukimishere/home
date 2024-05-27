import streamlit as st
import streamlit.components.v1 as components

st.header("노세노세", divider='orange')

col1, col2=st.columns(2)
with col1:
    st.text("slogan, 노년을 행복하게")
with col2:
    st.write(f"{st.session_state.user_data.get('name', '')}님, 환영합니다.")

col1, col2 =st.columns(2)
with col1: 
    st.button("일자리를 구하고 신가요?")
    st.text("description")
with col2:    
    st.image("images/sundayafternoon.jpg")

st.text("From cradle to grave service")
col1,col2,col3,col4,col5= st.columns(5)
with col1:
    st.button("어린이")
    st.text("description")
with col2:
    st.button("노인")
    st.text("description")
with col3:
    st.button("연구소")
    st.text("description")
with col4:
    st.button("기업")
    st.text("description")
with col5:
    st.button("군인")
    st.text("description")