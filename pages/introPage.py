import streamlit as st
from component import divider, scrollFadeIn
from component.font import customText

def show_intro_content():
    st.markdown("""
        <style>
        .reportview-container .main .block-container {
            padding-left: 10%;
            padding-right: 10%;
        }
        </style>
    """, unsafe_allow_html=True)

    customText.titleNoLink("Personality Traits", None, "0px")
    customText.titleNoLink("Predicted from One’s Face", None, "0px")
    divider.space(40)

    # customText.caption("서울대학교 빅데이터 핀테크 AI 고급 전문가 과정 9기, 시각화웹개발 Team 7")
    customText.caption("Team 7.", None, "0px")
    customText.caption("최지혜, 한규범, 최요한 이하림, 유지훈, 박동근 and 김소현")
    divider.rainbow_divider()

    customText.header("Introduction")
    customText.subheader("Do Facial Expressions Matter with One’s Personality?")
    divider.space(40)

    customText.bold("Abraham Lincoln")
    customText.regularNoLink("나이 40이면 자신의 얼굴에 책임을 져야 한다.")
    divider.space(40)

    customText.bold("첫 인상")
    customText.regularNoLink("처음 만나는 사람의 속성에 대해서 그 사람에 대한 cue를 기반으로 판단을 내리는 것")
    customText.regularNoLink("첫 인상 결정요인 1위 '얼굴 표정' (YTN, 2012; 잡코리아 조사, 2022)")
    customText.regularNoLink("첫 인상 결정 뒤 잘 바뀌지 않는다 (헬스조선, 2024)")
    divider.space(40)

    customText.rightNoLink("\"사람의 내적 속성이 얼굴이라는 표면에 드러난다.\"", None, 18)


def show():
    show_intro_content()
    divider.divider("#d0d0d0")
    
    from pages.componentOfPersonalityPage import show_content as personality_content
    customText.title("Component of Personality")
    scrollFadeIn.scroll_fade_in(personality_content(), "Component of Personality")

    divider.divider("#d0d0d0")
    from pages.goalsOfTheProjectPage import show_content as project_content
    customText.title("Goals of the Project")
    scrollFadeIn.scroll_fade_in(project_content(), "Goals of the Project")

    divider.divider("#d0d0d0")
    from pages.methodologyPage import show_content as methodology_content
    customText.title("Methodology")
    scrollFadeIn.scroll_fade_in(methodology_content(), "Methodology")

    divider.divider("#d0d0d0")
    from pages.resultsPage import show_content as result_content
    customText.title("Results")
    scrollFadeIn.scroll_fade_in(result_content(), "Results")

    divider.divider("#d0d0d0")
    from pages.conclusionPage import show_content as conclusion_content
    customText.title("Conclusion")
    scrollFadeIn.scroll_fade_in(conclusion_content(), "Conclusion")


show()