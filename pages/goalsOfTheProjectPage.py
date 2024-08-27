import streamlit as st
import pandas as pd
from component import divider
from component.font import customText as ct
from PIL import Image

def show_content():
    ct.subheaderNoLink("Objectives")
    divider.space(40)

    items = [
    "To learn personality traits based on facial expressions from images and audio, and to analyze the personalities of well-known figures and acquaintances around us using this data.",
    "To explore what personality traits we perceive and judge in real-life interactions."
    ]

    # 순서가 있는 리스트 생성 및 표시
    for i, item in enumerate(items, 1):
        st.markdown(f"{i}. {item}")

    # 추가적인 스타일링을 위한 CSS (선택사항)
    st.markdown("""
    <style>
        ol {
            padding-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    divider.space(60)



show_content()




