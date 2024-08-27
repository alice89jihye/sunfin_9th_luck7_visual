import streamlit as st

# 테마 색상 값을 가져오기
divider_color = st.get_option("theme.primaryColor")

def divider(color=None):
    # 색상이 지정되지 않으면 기본 테마 색상 사용
    color = color or divider_color
    st.markdown(f"""
        <style>
        .custom-divider {{
            border: 0;
            border-top: 2px solid {color};
            margin: 40px 0; 
        }}
        </style>
        <hr class="custom-divider">
    """, unsafe_allow_html=True)

def rainbow_divider():
    # 무지개 색상의 구분선 생성
    st.markdown("""
        <style>
        .rainbow-divider {
            border: 0;
            height: 5px; /* 구분선 높이 설정 */
            margin: 20px 0; /* 위아래 여백 설정 */
            background: linear-gradient(to right, 
                red, orange, yellow, green, blue, indigo, violet);
            background-size: 100% 100%; /* 배경 사이즈 설정 */
            background-repeat: no-repeat; /* 배경 반복 방지 */
        }
        </style>
        <hr class="rainbow-divider">
    """, unsafe_allow_html=True)

def space(space_px=20):
    st.markdown(
        f"""
        <div style="margin-bottom: {space_px}px;"></div>
        """, 
        unsafe_allow_html=True
    )