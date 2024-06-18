import os

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="노세老世",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 현재 파일의 절대 경로를 얻습니다.
current_dir = os.path.dirname(__file__)
# 이미지 파일의 절대 경로를 생성합니다.
image_path = os.path.join(current_dir, '..', 'images', 'sundayafternoon.jpg')

# 파일 경로가 올바른지 확인합니다.
if not os.path.isfile(image_path):
    st.error(f"Image file not found: {image_path}")
else:
    st.header("노세老世", divider='orange')

    col1,col2,col3=st.columns([7,2,1])
    with col1:
        st.markdown(''':rainbow[slogan, 노년을 행복하게]''')
    with col2:
        st.write(f"{st.session_state.user_data.get('name', '')}님, 환영합니다.")
    with col3:
        st.page_link("pages/mypage.py", label="마이페이지", icon="🏠")

    col1, col2 =st.columns(2)
    with col1:
        st.button("일자리를 구하고 계신가요?")
        #st.link_button("일자리를 구하고 계신가요?","웹주소")
        st.markdown("")
        st.markdown("**AIHR**")
        st.markdown("원하는 인재를 AI가 자동으로 추천해드려요")
        st.markdown("**이력서 자동 생성**")
        st.markdown("이력서 작성에 스트레스 받지 마세요. 이력서를 자동으로 생성해드려요")
        st.markdown("**AI 기술면접**")
        st.markdown("나의 이력서로 AI와 모의면접을 진행해요")
    with col2:    
        st.image("images/sundayafternoon.jpg")

    st.markdown(''':rainbow[From cradle to grave service]''')
    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
        st.link_button("두뇌개발","https://64ydyb2dcrz4dxbxknxonu.streamlit.app/")
    with col2:
        st.link_button("복지관","https://senior-8eoe8jhllgdvchmyz8whc8.streamlit.app/")
        st.markdown('''	:spider_web: 	:computer:''')
    with col3:
        st.link_button("자료조사","https://researcher-ar65crrai4zwh82ilf3ytn.streamlit.app/")
        st.markdown('''	:school: 	:eyes:''')
    with col4:
        st.link_button("데일리 리포트","https://company-bhmgtrlduo726xhv9ialbm.streamlit.app/")
        st.markdown('''	:newspaper: 	:envelope_with_arrow:''')
    with col5:
        st.link_button("오늘의 운세","https://soldier-esscnr5vz33mrnzxraj4bj.streamlit.app/")
        st.markdown('''	:male_mage: :fortune_cookie:''')



