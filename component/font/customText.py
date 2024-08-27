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
def h1(text, color=None, margin_bottom="20px", font_size="36px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-h1 {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
        }}
        </style>
        <h1 class="custom-h1">{text}</h1>
        """, 
        unsafe_allow_html=True
    )

def h1NoLink(text, color=None, margin_bottom="20px", font_size="36px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-h1-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
            text-decoration: none;
        }}
        .custom-h1-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <h1 class="custom-h1-no-link">{text}</h1>
        """, 
        unsafe_allow_html=True
    )

def h2(text, color=None, margin_bottom="16px", font_size="30px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-h2 {{
            font-family: {font};
            color: {color};
            font-weight: 600;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
        }}
        </style>
        <h2 class="custom-h2">{text}</h2>
        """, 
        unsafe_allow_html=True
    )

def h2NoLink(text, color=None, margin_bottom="16px", font_size="30px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-h2-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 600;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
            text-decoration: none;
        }}
        .custom-h2-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <h2 class="custom-h2-no-link">{text}</h2>
        """, 
        unsafe_allow_html=True
    )

def h3(text, color=None, margin_bottom="14px", font_size="24px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-h3 {{
            font-family: {font};
            color: {color};
            font-weight: 500;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
        }}
        </style>
        <h3 class="custom-h3">{text}</h3>
        """, 
        unsafe_allow_html=True
    )

def h3NoLink(text, color=None, margin_bottom="14px", font_size="24px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-h3-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 500;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
            text-decoration: none;
        }}
        .custom-h3-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <h3 class="custom-h3-no-link">{text}</h3>
        """, 
        unsafe_allow_html=True
    )

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

def titleNoLink(text, color=None, margin_bottom="10px", font_size="32px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-title-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
            margin-top: {margin_bottom};
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

def headerNoLink(text, color=None, margin_bottom="12px", font_size="28px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-header-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 600;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
            text-decoration: none;
        }}
        .custom-header-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <p class="custom-header-no-link">{text}</p>
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

def subheaderNoLink(text, color=None, margin_bottom="10px", font_size="22px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-subheader-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 500;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
            text-decoration: none;
        }}
        .custom-subheader-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <p class="custom-subheader-no-link">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def bold(text, color=None, margin_bottom="8px", font_size="16px"):
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

def boldNoLink(text, color=None, margin_bottom="8px", font_size="16px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-bold-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
            text-decoration: none;
        }}
        .custom-bold-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <p class="custom-bold-no-link">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def regular(text, color=None, margin_bottom="8px", font_size="16px"):
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

def regularNoLink(text, color=None, margin_bottom="8px", font_size="16px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-regular-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
            text-decoration: none;
        }}
        .custom-regular-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <p class="custom-regular-no-link">{text}</p>
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

def captionNoLink(text, color=None, margin_bottom="6px", font_size="14px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-caption-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-size: {font_size};
            font-style: italic;
            margin-bottom: {margin_bottom};
            text-decoration: none;
        }}
        .custom-caption-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <p class="custom-caption-no-link">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def code(text, background_color="#f0f0f0", margin_bottom="10px", font_size="14px"):
    st.markdown(
        f"""
        <style>
        .custom-code {{
            font-family: monospace;
            background-color: {background_color};
            padding: 4px 8px;
            border-radius: 4px;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
        }}
        </style>
        <code class="custom-code">{text}</code>
        """, 
        unsafe_allow_html=True
    )

def right(text, color=None, margin_bottom="8px", font_size="16px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-right {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-size: {font_size};
            text-align: right;
            margin-bottom: {margin_bottom};
        }}
        </style>
        <p class="custom-right">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def rightNoLink(text, color=None, margin_bottom="8px", font_size="16px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-right-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 700;
            font-size: {font_size};
            text-align: right;
            margin-bottom: {margin_bottom};
            text-decoration: none;
        }}
        .custom-right-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <p class="custom-right-no-link">{text}</p>
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
        }}
        </style>
        <p class="custom-italic">{text}</p>
        """, 
        unsafe_allow_html=True
    )

def italicNoLink(text, color=None, margin_bottom="8px", font_size="16px", margin_left="0px"):
    color = color or text_color
    st.markdown(
        f"""
        <style>
        .custom-italic-no-link {{
            font-family: {font};
            color: {color};
            font-weight: 400;
            font-style: italic;
            font-size: {font_size};
            margin-bottom: {margin_bottom};
            margin-left: {margin_left};
            text-decoration: none;
        }}
        .custom-italic-no-link:hover {{
            text-decoration: none;
            cursor: default;
        }}
        </style>
        <p class="custom-italic-no-link">{text}</p>
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
