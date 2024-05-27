import streamlit as st

# Title
st.title('로그인')
st.markdown("")

# Information input
login_id = st.text_input("아이디")
login_pw = st.text_input("비밀번호", type='password')

col1, col2 = st.columns([3, 1])

# Validate login
if st.button("로그인", key='login_button'):
    if 'user_data' in st.session_state:
        if login_id == st.session_state.user_data.get('user_id') and login_pw == st.session_state.user_data.get('pw'):
            st.session_state.logged_in = True
            st.success("로그인 성공!")
            # Reload the app to reflect login status
            st.experimental_rerun()
        else:
            st.error("아이디 또는 비밀번호가 잘못되었습니다. 다시 입력하세요.")
    else:
        st.error("등록된 사용자가 없습니다. 회원가입을 먼저 진행해주세요.")

# Check if logged in to enable the link
if 'logged_in' in st.session_state and st.session_state.logged_in:
    with col2:
        st.page_link("pages/home_after_login_selector.py", label="홈으로 이동")
