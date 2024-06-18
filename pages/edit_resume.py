import streamlit as st
from pymongo import MongoClient

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
        st.title("이력서 수정하기")
        
        col1, col3 = st.columns([2, 1])
        with col1:
            name = st.text_input("이름", value=resume_data.get('name', ''))
            jobs = st.multiselect(
                "직무",
                ["DevOps/시스템 관리자", "HW/임베디드 개발자", "IOS 개발자",
                "데이터 사이언티스트", "데이터 엔지니어", "서버/백엔드 개발자",
                "안드로이드 개발자", "프론트엔드 개발자", "게임 서버 개발자",
                "게임 클라이언트 개발자"],
                default=resume_data.get('jobs', []))
            
            # Options 리스트 정의
            options = ["신입", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15년 이상"]
            
            # 기본값이 options에 있는지 확인 후 설정
            start_year = resume_data.get('start_year', '신입')
            end_year = resume_data.get('end_year', '2')
            if start_year not in options:
                start_year = '신입'
            if end_year not in options:
                end_year = '2'
            
            start_year, end_year = st.select_slider(
                "경력을 입력 해 주세요",
                options=options,
                value=(start_year, end_year))

        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            contact = st.text_input("연락처", value=resume_data.get('contact', ''))
            education = st.text_input("대학교, 학과", value=resume_data.get('education', ''))
            cert = st.text_area("자격증", value=resume_data.get('cert', ''))

        with col2:
            url = st.text_input("github 주소", value=resume_data.get('url', ''))
            company = st.text_input("(구)직장명", value=resume_data.get('company', ''))
            experience = st.text_area("경력", value=resume_data.get('experience', ''))

        skills = st.multiselect(
            "기술",
            ["Python", "JavaScript", "Java", "C#", "C++", "Ruby", "Swift", 
            "Kotlin", "Go", "Rust", "SQL", "R", "PHP", "HTML", "CSS", 
            "TypeScript", "Scala", "Perl", "Matlab", "SAS"],
            default=resume_data.get('skills', []))

        skill_levels = {}
        for skill in skills:
            level = st.radio(f"{skill} 레벨 선택", ["상", "중", "하"], key=f"level_{skill}", index=["상", "중", "하"].index(resume_data.get('skill_levels', {}).get(skill, '상')))
            skill_levels[skill] = level

        resume_text = st.text_area("AI가 생성한 이력서 텍스트", value=resume_data.get('resume_text', ''))

        if st.button("수정 완료"):
            updated_data = {
                "name": name,
                "jobs": jobs,
                "start_year": start_year,
                "end_year": end_year,
                "contact": contact,
                "education": education,
                "cert": cert,
                "url": url,
                "company": company,
                "experience": experience,
                "skills": skills,
                "skill_levels": skill_levels,
                "resume_text": resume_text
            }

            resume_collection.update_one({"name": user_name}, {"$set": updated_data})
            st.success("이력서가 성공적으로 업데이트 되었습니다.")
    else:
        st.error("이력서 정보를 찾을 수 없습니다.")
else:
    st.error("로그인이 필요합니다. 로그인 해주세요.")
    st.page_link("pages/login.py", label="로그인 페이지로 이동")