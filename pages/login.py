import streamlit as st
from pymongo import MongoClient

st.set_page_config(
    page_title="노세老世",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# MongoDB Atlas 클라이언트 설정
client = MongoClient("mongodb+srv://test:1234@cluster.ct8weib.mongodb.net/o2b2data?retryWrites=true&w=majority")

db = client["o2b2data"]
collection = db["user"]

# Title
st.title('로그인')
st.markdown("")

# Information input
login_id = st.text_input("아이디")
login_pw = st.text_input("비밀번호", type='password')

col1, col2 = st.columns([3,1])

# Validate login
with col1:
    if st.button("로그인", key='login_button'):
        user_data = collection.find_one({"id": login_id, "pw": login_pw})
        if user_data:
            st.session_state.logged_in = True
            st.session_state.user_data = user_data
            st.session_state.login_id = login_id
            st.success("로그인 성공!")
            with col2:
                st.page_link("pages/home_after_login_selector.py", label="홈으로 이동")

        else:
            st.error("아이디 또는 비밀번호가 잘못되었습니다. 다시 입력하세요.")
            with col2:
                st.page_link("pages/join.py", label="회원가입")
