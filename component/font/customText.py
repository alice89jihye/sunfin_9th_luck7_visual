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

# 커스텀 텍스트 스타일 함수들
def title(text, color=None, marginBottom="10px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-title {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: 32px;
            margin-bottom: {marginBottom};
        }}
        </style>
        <p class="custom-title">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def titleNoLink(text, color=None, marginBottom="10px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-title-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: 32px;
            margin-bottom: {marginBottom};
            margin-top: {marginBottom}:
            text-decoration: none;
        }}
        .custom-title-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <p class="custom-title-no-link">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def header(text, color=None):
    color = color or text_color
    st.markdown(f'<h2 style="font-family: {font}; color: {color};">{text}</h2>', unsafe_allow_html=True)

def subheaderNoLink(text, color=None):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .subheader-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 500;
            font-size: 20px;
            margin-bottom: 10px;
            text-decoration: none;
        }}
        .subheader-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <p class="subheader-no-link">{text}</p>
        """, unsafe_allow_html=True
    )

def boldHNoLink(text, color=None, font_size="16px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .bold-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: {font_size};
            margin-bottom: 10px;
            text-decoration: none;
        }}
        .bold-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <p class="bold-no-link">{text}</p>
        """, unsafe_allow_html=True
    )

def boldHwithSubtextNoLink(text, subtext, color=None, subtext_color=None, font_size="16px", subtext_size="14px"):
    color = color or text_color
    subtext_color = subtext_color or color
    st.markdown(
        f"""
        <style>
        .bold-with-subtext {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: {font_size};
            margin-bottom: 10px;
            text-decoration: none;
        }}
        .subtext {{
            font-family: {font};
            color: {subtext_color};
            font-weight: 400;
            font-size: {subtext_size};
            margin-left: 10px;
        }}
        .bold-with-subtext:hover, .subtext:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <span class="bold-with-subtext">{text}<span class="subtext">{subtext}</span></span>
        """, unsafe_allow_html=True
    )

def boldHNoLinkRight(text, color=None, font_size="16px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .bold-no-link-right {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: {font_size};
            margin-bottom: 10px;
            text-decoration: none;
            text-align: right;
        }}
        .bold-no-link-right:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <p class="bold-no-link-right">{text}</p>
        """, unsafe_allow_html=True
    )

def regular4NoLink(text, color=None, font_size="16px", italic=False):
    color = color or text_color
    italic_style = "font-style: italic;" if italic else ""
    st.markdown(
        f"""
        <style>
        .no-link {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-size: {font_size};
            margin: 0;
            text-decoration: none;
            {italic_style}
        }}
        .no-link:hover {{
            text-decoration: none;
            cursor: default; 
        }}
        </style>
        <p class="no-link">{text}</p>
        """, unsafe_allow_html=True
    )

def regular4Link(text, url, color="#0000FF", font_size="16px", indent="0px"):
    st.markdown(
        f"""
        <style>
        .custom-link {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-size: {font_size};
            margin: 0;
            text-decoration: none;
            display: inline-block;
            padding-left: {indent};
        }}
        .custom-link:hover {{
            text-decoration: underline;
            cursor: pointer;
        }}
        </style>
        <a href="{url}" target="_blank" class="custom-link">{text}</a>
        """, unsafe_allow_html=True
    )

def caption(text, color=None, marginBottom="10px"):
    color = color or text_color
    st.markdown(f'<p style="font-family: {font}; color: {color}; font-size: 12px; margin-bottom: {marginBottom}">{text}</p>', unsafe_allow_html=True)

def markdown(text, color=None):
    color = color or text_color
    st.markdown(f'<p style="font-family: {font}; color: {color};">{text}</p>', unsafe_allow_html=True)

def code(text, color=None):
    color = color or text_color
    st.markdown(f'<pre style="font-family: {font}; color: {color}; background-color: #f5f5f5; padding: 10px;">{text}</pre>', unsafe_allow_html=True)