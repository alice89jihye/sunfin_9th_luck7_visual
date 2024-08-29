import streamlit as st
from component import divider
from component.font import customText as ct
from PIL import Image
import base64
from io import BytesIO

def show_intro_content():
    image1 = Image.open("./data/img/bg1.png")

    # 이미지를 base64로 인코딩
    buffered = BytesIO()
    image1.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # CSS 스타일 정의
    css = f"""
    <style>
    .stApp {{
        background-image: url(data:image/png;base64,{img_str});
        background-size: 50% auto;
        background-position: bottom right;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    st.markdown("""
        <style>
        .reportview-container .main .block-container {
            padding-left: 10%;
            padding-right: 10%;
        }
        </style>
    """, unsafe_allow_html=True)

    ct.title("Personality Traits", None, "0px")
    ct.title("Predicted from One’s Face", None, "0px")
    divider.space(40)

    # ct.caption("서울대학교 빅데이터 핀테크 AI 고급 전문가 과정 9기, 시각화웹개발 Team 7")
    ct.caption("Team 7.", None, "0px")
    ct.caption("최지혜, 한규범, 최요한 이하림, 유지훈, 박동근 and 김소현")
    divider.rainbow_divider()

    ct.header("Introduction")
    ct.subheader("Do Facial Expressions Matter with One’s Personality?")
    divider.space(40)

    ct.bold("Abraham Lincoln")
    ct.regular("나이 40이면 자신의 얼굴에 책임을 져야 한다.")
    divider.space(40)

    ct.bold("첫 인상")
    ct.regular("처음 만나는 사람의 속성에 대해서 그 사람에 대한 cue를 기반으로 판단을 내리는 것")
    ct.regular("첫 인상 결정요인 1위 '얼굴 표정' (YTN, 2012; 잡코리아 조사, 2022)")
    ct.regular("첫 인상 결정 뒤 잘 바뀌지 않는다 (헬스조선, 2024)")
    divider.space(40)

    ct.right("\"사람의 내적 속성이 얼굴이라는 표면에 드러난다.\"")


def show():
    show_intro_content()
    # divider.divider("#d0d0d0")
    
    # ct.title("Component of Personality")
    # from pages.componentOfPersonalityPage import show_content as personality_content
    # personality_content()

    # divider.divider("#d0d0d0")
    # from pages.goalsOfTheProjectPage import show_content as project_content
    # ct.title("Goals of the Project")
    # project_content()

    # divider.divider("#d0d0d0")
    # from pages.methodologyPage import show_content as methodology_content
    # ct.title("Methodology")
    # methodology_content()

    # divider.divider("#d0d0d0")
    # from pages.resultsPage import show_content as result_content
    # ct.title("Results")
    # result_content()

    # divider.divider("#d0d0d0")
    # from pages.conclusionPage import show_content as conclusion_content
    # ct.title("Conclusion")
    # conclusion_content()


show()