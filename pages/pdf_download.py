import base64
import os
from io import BytesIO

import streamlit as st
from pymongo import MongoClient
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Paragraph, SimpleDocTemplate, Spacer, Table,
                                TableStyle)

st.set_page_config(
    page_title="노세老世",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# MongoDB 클라이언트 생성
client = MongoClient("mongodb+srv://test:1234@cluster.ct8weib.mongodb.net/o2b2data?retryWrites=true&w=majority")
db = client["o2b2data"]
resume_collection = db["resume_user"]

# current_dir:현재 경로 저장 , font_path: 폰트경로지정(NanumGothic.ttf)
current_dir = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(current_dir, "..", "fonts", "NanumGothic.ttf")

# NanumGothic 폰트를 reportlab에 등록
pdfmetrics.registerFont(TTFont('NanumGothic', font_path))


# 로그인 상태 확인
if 'logged_in' in st.session_state and st.session_state.logged_in:
    user_name = st.session_state.user_data.get('name')

    # 사용자 이름과 일치하는 이력서 정보 가져오기
    resume_data = resume_collection.find_one({"name": user_name})

    if resume_data:
        st.title("PDF 다운로드")

        # PDF 생성 함수
        def create_pdf(resume_data):
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=A4)
            styles = getSampleStyleSheet()

            # 기본 스타일에 NanumGothic 폰트 적용
            normal_style = ParagraphStyle(
                name='Normal',
                parent=styles['Normal'],
                fontName='NanumGothic',
                fontSize=12
            )
            # title(이력서 제목)용 폰트
            title_style = ParagraphStyle(
                name='Title',
                parent=styles['Title'],
                fontName='NanumGothic',
                fontSize=18,
                spaceAfter=14
            )
            resume_text_style = ParagraphStyle(
                name='ResumeText',
                parent=styles['Normal'],
                fontName='NanumGothic',
                fontSize=12,
                leading=20  # 줄 간격을 약간 더 넓게 설정, 줄간격이 너무 붙어있음
            )


            content = []

            # 이력서 제목
            title = Paragraph(f"{resume_data['name']}의 이력서", title_style)
            content.append(title)
            content.append(Spacer(1, 0.2 * inch))

            # 직무
            jobs = Paragraph(f"직무: {', '.join(resume_data['jobs'])}", normal_style)
            content.append(jobs)
            content.append(Spacer(1, 0.2 * inch))

            # 경력
            experience = Paragraph(f"경력: {resume_data['start_year']} - {resume_data['end_year']}", normal_style)
            content.append(experience)
            content.append(Spacer(1, 0.2 * inch))

            # 연락처
            contact = Paragraph(f"연락처: {resume_data['contact']}", normal_style)
            content.append(contact)
            content.append(Spacer(1, 0.2 * inch))

            # 학력
            education = Paragraph(f"학력: {resume_data['education']}", normal_style)
            content.append(education)
            content.append(Spacer(1, 0.2 * inch))

            # 자격증
            cert = Paragraph(f"자격증: {resume_data['cert']}", normal_style)
            content.append(cert)
            content.append(Spacer(1, 0.2 * inch))

            # URL
            url = Paragraph(f"URL: {resume_data['url']}", normal_style)
            content.append(url)
            content.append(Spacer(1, 0.2 * inch))

            # 회사
            company = Paragraph(f"회사: {resume_data['company']}", normal_style)
            content.append(company)
            content.append(Spacer(1, 0.2 * inch))

            # 경험
            experience = Paragraph(f"경험: {resume_data['experience']}", normal_style)
            content.append(experience)
            content.append(Spacer(1, 0.2 * inch))

            # 기술
            skills = Paragraph(f"기술: {', '.join(resume_data['skills'])}", normal_style)
            content.append(skills)
            content.append(Spacer(1, 0.2 * inch))

            # 기술 수준
            skill_levels = [[Paragraph(f"{skill}", normal_style), Paragraph(f"{level}", normal_style)] for skill, level in resume_data['skill_levels'].items()]
            skill_table = Table(skill_levels, colWidths=[2 * inch, 4 * inch])
            skill_table.setStyle(TableStyle([
                #('BACKGROUND', (0, 0), (-1, 0), colors.beige),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, -1), 'NanumGothic'),
                ('FONTSIZE', (0, 0), (-1, -1), 12),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            content.append(skill_table)
            content.append(Spacer(1, 0.2 * inch))

            # 요약
            summary = Paragraph(f"요약: {resume_data['summary']}", normal_style)
            content.append(summary)
            content.append(Spacer(1, 0.2 * inch))

            # AI가 생성한 이력서 텍스트
            resume_text = Paragraph("AI가 생성한 이력서 텍스트:", normal_style)
            content.append(resume_text)
            content.append(Spacer(1, 0.2 * inch))
            text_object = Paragraph(resume_data['resume_text'].replace('\n', '<br/>'), normal_style)
            content.append(text_object)

            doc.build(content)
            buffer.seek(0)
            return buffer

        # PDF 생성 및 다운로드
        pdf_buffer = create_pdf(resume_data)
        pdf_data = pdf_buffer.read()

        st.download_button(
            label="PDF 다운로드",
            data=pdf_data,
            file_name=f"{resume_data['name']}_이력서.pdf",
            mime="application/pdf"
        )
    else:
        st.error("이력서 정보를 찾을 수 없습니다.")

else:
    st.error("로그인이 필요합니다. 로그인 해주세요.")
    st.page_link("pages/login.py", label="로그인 페이지로 이동")
