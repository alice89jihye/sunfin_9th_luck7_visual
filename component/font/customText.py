import streamlit as st

# 현재 Streamlit 테마 값 가져오기
primary_color = st.get_option("theme.primaryColor")
background_color = st.get_option("theme.backgroundColor")
secondary_background_color = st.get_option("theme.secondaryBackgroundColor")
text_color = st.get_option("theme.textColor")
font = st.get_option("theme.font") or "'Noto Sans', sans-serif"  # 폰트가 없을 경우 기본 폰트 설정

# Google Fonts 링크 추가
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&display=swap');
</style>
""", unsafe_allow_html=True)

def title(text, color=None, margin_bottom="10px", font_size="32px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-title {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
        }}
        </style>
        <p class="custom-title">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def header(text, color=None, margin_bottom="12px", font_size="28px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-header {{
            font-family: {font};
            color: {color};
            font-weight: 600;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
        }}
        </style>
        <p class="custom-header">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def subheader(text, color=None, margin_bottom="10px", font_size="22px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-subheader {{
            font-family: {font};
            color: {color};
            font-weight: 500;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
        }}
        </style>
        <p class="custom-subheader">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def bold(text, color=None, margin_bottom="8px", font_size="18px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-bold {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
        }}
        </style>
        <p class="custom-bold">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def regular(text, color=None, margin_bottom="8px", font_size="18px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-regular {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
        }}
        </style>
        <p class="custom-regular">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def caption(text, color=None, margin_bottom="6px", font_size="14px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-caption {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
        }}
        </style>
        <p class="custom-caption">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def code(text, background_color="#1e1e1e", text_color="#ffffff", margin_bottom="10px", font_size="14px"):
    st.markdown(
        f"""
        <style>
        .custom-code {{
            font-family: monospace;
            background-color: {background_color};
            color: {text_color};
            padding: 4px 8px;
            border-radius: 4px;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
            display: block;
            white-space: pre-wrap;
        }}
        </style>
        <code class="custom-code">{text}</code>
        """, 
        unsafe_allow_html=True
    )

def right(text, color=None, margin_right="40%", font_size="18px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-right {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: {font_size};
            text-align: right;
            margin-right: {margin_right};
        }}
        </style>
        <p class="custom-right">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def marginleft(text, margin_left="20px", color=None, margin_bottom="8px", font_size="16px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-marginleft {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-size: {font_size};
            margin-left: {margin_left};
            margin-bottom: {margin_bottom};
        }}
        </style>
        <p class="custom-marginleft">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def marginleftNoLink(text, margin_left="20px", color=None, margin_bottom="8px", font_size="16px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-marginleft-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-size: {font_size};
            margin-left: {margin_left};
            margin-bottom: {margin_bottom};
            text-decoration: none;
        }}
        .custom-marginleft-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <p class="custom-marginleft-no-link">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def link(text, url, color="#0000FF", margin_bottom="8px", font_size="16px", margin_left="0px"):
    st.markdown(
        f"""
        <style>
        .custom-link {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-size: {font_size};
            text-decoration: underline;
            margin-bottom: {margin_bottom};
            margin-left: {margin_left};
        }}
        </style>
        <a href="{url}" class="custom-link">{text}</a>
        """, 
        unsafe_allow_html=True
    )

def link2(text, url, color=None, margin_bottom="8px", font_size="16px", margin_left="0px"):
    st.markdown(
        f"""
        <style>
        .custom-link2 {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-size: {font_size};
            text-decoration: underline;
            margin-bottom: {margin_bottom};
            margin-left: {margin_left};
        }}
        </style>
        <a href="{url}" class="custom-link2">{text}</a>
        """, 
        unsafe_allow_html=True
    )

def italic(text, color=None, margin_bottom="8px", font_size="16px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-italic {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-style: italic;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
            margin-left: 40px;
        }}
        </style>
        <p class="custom-italic">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def mixed_style_text(bold_text, regular_text, color=None, margin_bottom="8px", font_size="16px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .mixed-style-text {{
            font-family: {font};
            color: {color};
            font-size: {font_size};
            margin-bottom: {margin_bottom};
            white-space: nowrap;
            display: inline-block;
            text-decoration: none;
        }}
        .mixed-style-text-bold {{
            font-weight: 700;
            text-decoration: none;
        }}
        .mixed-style-text-regular {{
            font-weight: 400;
            text-decoration: none;
        }}
        </style>
        <span class="mixed-style-text">
            <span class="mixed-style-text-bold">{bold_text}</span><span class="mixed-style-text-regular">{regular_text}</span>
        </span>
        """, 
        unsafe_allow_html=True
    )
