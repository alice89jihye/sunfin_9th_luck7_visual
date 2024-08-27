import streamlit as st
from component import divider, scrollFadeIn
from component.font import customText

def show_intro_content():
    customText.titleNoLink("Personality Traits", None, "0px")
    customText.titleNoLink("Predicted from One’s Face", None, "0px")
    divider.space(40)

    # customText.caption("서울대학교 빅데이터 핀테크 AI 고급 전문가 과정 9기, 시각화웹개발 Team 7")
    customText.caption("Team 7.", None, "0px")
    customText.caption("최지혜, 한규범, 최요한 이하림, 유지훈, 박동근 and 김소현")
    divider.rainbow_divider()

    customText.header("Introduction")
    customText.subheaderNoLink("Do Facial Expressions Matter with One’s Personality?")
    divider.space(40)

    customText.boldHNoLink("Abraham Lincoln")
    customText.regular4NoLink("나이 40이면 자신의 얼굴에 책임을 져야 한다.")
    divider.space(40)

    customText.boldHNoLink("첫 인상")
    customText.regular4NoLink("처음 만나는 사람의 속성에 대해서 그 사람에 대한 cue를 기반으로 판단을 내리는 것")
    customText.regular4NoLink("첫 인상 결정요인 1위 '얼굴 표정' (YTN, 2012; 잡코리아 조사, 2022)")
    customText.regular4NoLink("첫 인상 결정 뒤 잘 바뀌지 않는다 (헬스조선, 2024)")
    divider.space(40)

    customText.boldHNoLinkRight("\"사람의 내적 속성이 얼굴이라는 표면에 드러난다.\"", None, 18)


def show():
    show_intro_content()
    divider.divider("#d0d0d0")
    
    from pages.componentOfPersonalityPage import show_content as personality_content
    scrollFadeIn.scroll_fade_in(personality_content())


show()