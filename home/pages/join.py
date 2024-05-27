import streamlit as st

# Title
st.title('회원가입을 진행해주세요')
st.markdown("")

# Information input
name = st.text_input("이름")
user_id = st.text_input("아이디")
pw = st.text_input("비밀번호", type='password')

# Save state to session
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

col1, col2 =st.columns(2)
with col1:
    if st.button("회원가입 완료"):
        st.session_state.user_data['name'] = name
        st.session_state.user_data['user_id'] = user_id
        st.session_state.user_data['pw'] = pw
        st.success("회원가입이 완료되었습니다!")
        st.rerun()  # Refresh the page to clear the inputs
        
with col2:
    st.page_link("pages/login.py", label="로그인") 

st.markdown("-------------")
st.markdown("### 결과:")
st.write(f"이름: {st.session_state.user_data.get('name', '')}")
st.write(f"ID: {st.session_state.user_data.get('user_id', '')}")
st.write(f"password: {st.session_state.user_data.get('pw', '')}")
