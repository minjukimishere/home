# pages/mypage.py
import streamlit as st
from pymongo import MongoClient

st.set_page_config(
    page_title="노세老世",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.header("노세老世 | Mypage :house:", divider='orange')

# MongoDB Atlas 클라이언트 설정
client = MongoClient("mongodb+srv://test:1234@cluster.ct8weib.mongodb.net/o2b2data?retryWrites=true&w=majority")

db = client["o2b2data"]
resume_collection = db["resume_user"]

# 로그인 상태 확인
if 'logged_in' in st.session_state and st.session_state.logged_in:
    login_id = st.session_state.login_id
    user_name = st.session_state.user_data.get('name')

    # 사용자 이름과 일치하는 이력서 정보 가져오기
    resume_data = resume_collection.find_one({"name": user_name})

    if resume_data:
        st.header(f"안녕하세요, {user_name}님! :smile:")
        # 채용 연락 확인
        employ_count = resume_collection.count_documents({"name": user_name, "employ": True})
        if employ_count > 0:
            st.success(f"현재 채용 연락을 {employ_count}건 받았습니다!")
            if st.button("확인하기"):
                employ_info = list(resume_collection.find({"name": user_name, "employ": True}, {"_id": 0, "company_name": 1, "company_contact": 1, "message": 1}))
                for info in employ_info:
                    st.write(f"회사 이름: {info.get('company_name', '정보가 없습니다.')}")
                    st.write(f"연락처: {info.get('company_contact', '정보가 없습니다.')}")
                    st.write(f"메세지: {info.get('message', '정보가 없습니다.')}")
        st.markdown("---")
        st.subheader("나의 이력서")
        with st.expander("이력서 확인하기"):
            st.text(f"이름: {resume_data.get('name', 'N/A')}")
            st.text(f"직업: {resume_data.get('jobs', 'N/A')}")
            st.text(f"경력 시작 연도: {resume_data.get('start_year', 'N/A')}")
            st.text(f"경력 종료 연도: {resume_data.get('end_year', 'N/A')}")
            st.text(f"연락처: {resume_data.get('contact', 'N/A')}")
            st.text(f"학력: {resume_data.get('education', 'N/A')}")
            st.text(f"자격증: {resume_data.get('cert', 'N/A')}")
            st.text(f"URL: {resume_data.get('url', 'N/A')}")
            st.text(f"회사: {resume_data.get('company', 'N/A')}")
            st.text(f"경험: {resume_data.get('experience', 'N/A')}")
            st.text(f"기술: {resume_data.get('skills', 'N/A')}")
            st.text(f"기술 수준: {resume_data.get('skill_levels', 'N/A')}")
            st.text(f"요약: {resume_data.get('summary', 'N/A')}")
            st.text(f"AI가 생성한 이력서 텍스트: {resume_data.get('resume_text', 'N/A')}")

            st.markdown("---")
            col1, col2 = st.columns(2)
            with col1:
                st.page_link("pages/pdf_download.py", label="PDF 다운로드")
            with col2:
                st.page_link("pages/edit_resume.py", label="이력서 수정하기")

    else:
        st.error("이력서 정보를 찾을 수 없습니다.")
else:
    st.error("로그인이 필요합니다. 로그인 해주세요.")
    st.page_link("pages/login.py", label="로그인 페이지로 이동")
