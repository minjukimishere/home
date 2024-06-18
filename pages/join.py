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
st.title('회원가입을 진행해주세요')
st.markdown("")

# Information input
name = st.text_input("이름")
user_id = st.text_input("아이디")
pw = st.text_input("비밀번호", type='password')

# Save state to session
#if 'user_data' not in st.session_state:
#    st.session_state.user_data = {}

col1, col2 =st.columns(2)
with col1:
    if st.button("회원가입 완료"):
        if not name or not user_id or not pw:
            st.warning("모든 정보를 빠짐없이 입력해 주세요.")
        #st.session_state.user_data['name'] = name
        #st.session_state.user_data['user_id'] = user_id
        #st.session_state.user_data['pw'] = pw
        else:
            user_data = {
                "name": name,
                "id": user_id,
                "pw": pw
            }
            collection.insert_one(user_data)
        
with col2:
    st.page_link("pages/login.py", label="로그인") 
        

#st.markdown("-------------")
#st.markdown("### 결과:")
#st.write(f"이름: {st.session_state.user_data.get('name', '')}")
#st.write(f"ID: {st.session_state.user_data.get('user_id', '')}")
#st.write(f"password: {st.session_state.user_data.get('pw', '')}")
