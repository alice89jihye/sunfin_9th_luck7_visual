import streamlit as st
import pandas as pd
from component import divider
from component.font import customText as ct
from PIL import Image

def show_content():
    st.markdown("""
        <style>
        .reportview-container .main .block-container {
            padding-left: 10%;
            padding-right: 10%;
        }
        </style>
    """, unsafe_allow_html=True)
    
    ct.subheader("Objectives")
    divider.space(40)

    items = [
        "To learn personality traits based on facial expressions from images and audio, and<br>to analyze the personalities of well-known figures and acquaintances around us<br>using this data.",
        "To explore what personality traits we perceive and judge in real-life interactions."
    ]

    for i, item in enumerate(items, 1):
        # 첫 번째 줄과 나머지 줄 분리
        first_line, *rest_lines = item.split('<br>')
        
        st.markdown(f"""
        <div style="font-size: 20px; margin-bottom: 15px;">
            <p style="margin: 0; font-size: 20px;">
                <span style="font-weight: bold; font-size: 20px;">{i}. </span>{first_line}
            </p>
            {"".join([f'<p style="margin: 5px 0 0 30px; font-size: 20px;">{line}</p>' for line in rest_lines])}
        </div>
        """, unsafe_allow_html=True)

    # 추가적인 스타일링을 위한 CSS (선택사항)
    st.markdown("""
        <style>
            p {
                line-height: 1.5;
            }
        </style>
        """, unsafe_allow_html=True)

    divider.space(60)



show_content()




