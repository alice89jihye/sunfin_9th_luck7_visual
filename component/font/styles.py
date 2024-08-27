# styles.py

import streamlit as st

# 현재 Streamlit 테마 값 가져오기
primary_color = st.get_option("theme.primaryColor")
background_color = st.get_option("theme.backgroundColor")
secondary_background_color = st.get_option("theme.secondaryBackgroundColor")
text_color = st.get_option("theme.textColor")
font = st.get_option("theme.font") or "'Noto Sans', sans-serif"

# 스타일 정의
styles = {
    "title": f"""
        font-family: {font};
        color: {{color}};
        font-weight: 700;
        font-size: 32px;
        margin-bottom: {{margin_bottom}};
    """,
    "title_no_link": f"""
        font-family: {font};
        color: {{color}};
        font-weight: 700;
        font-size: 32px;
        margin-bottom: {{margin_bottom}};
        margin-top: {{margin_bottom}};
        text-decoration: none;
    """,
    "header": f"""
        font-family: {font};
        color: {{color}};
    """,
    "subheader_no_link": f"""
        font-family: {font};
        color: {{color}};
        font-weight: 500;
        font-size: 20px;
        margin-bottom: 10px;
        text-decoration: none;
    """,
    "bold_no_link": f"""
        font-family: {font};
        color: {{color}};
        font-weight: 700;
        font-size: {{font_size}};
        margin-bottom: 10px;
        text-decoration: none;
    """,
    "regular_no_link": f"""
        font-family: {font};
        color: {{color}};
        font-weight: 400;
        font-size: {{font_size}};
        margin: 0;
        text-decoration: none;
        {{italic_style}}
    """,
    "regular_link": f"""
        font-family: {font};
        color: {{color}};
        font-weight: 400;
        font-size: {{font_size}};
        margin: 0;
        text-decoration: none;
    """,
        "regular_indent_link": f"""
        font-family: {font};
        color: {{color}};
        font-weight: 400;
        font-size: {{font_size}};
        margin-left: {{marginleft}};
        text-decoration: none;
        display: inline-block;
        padding-left: {{indent}};
    """,
    "caption": f"""
        font-family: {font};
        color: {{color}};
        font-size: 12px;
        margin-bottom: {{margin_bottom}};
    """,
    "code": f"""
        font-family: {font};
        color: {{color}};
        background-color: #f5f5f5;
        padding: 10px;
    """,
    "bold_with_subtext": """
        font-family: {font};
        color: {color};
        font-weight: 700;
        font-size: {font_size};
        margin-bottom: 10px;
        text-decoration: none;
    """,
    "subtext": """
        font-family: {font};
        color: {color};
        font-weight: 400;
        font-size: {font_size};
        margin-left: 10px;
        text-decoration: none;
    """
}