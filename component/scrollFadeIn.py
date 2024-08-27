import streamlit as st
import streamlit.components.v1 as components

def scroll_fade_in(content_or_func, title, duration=1000):
    # 세션 상태 초기화
    if 'shown_titles' not in st.session_state:
        st.session_state.shown_titles = set()

    # 이미 표시된 타이틀인지 확인
    if title in st.session_state.shown_titles:
        return

    # 타이틀을 표시된 목록에 추가
    st.session_state.shown_titles.add(title)

    # 콘텐츠 처리
    try:
        if callable(content_or_func):
            content = content_or_func()
        else:
            content = str(content_or_func)
    except Exception as e:
        st.error(f"Error generating content: {str(e)}")
        return

    if not content:
        st.warning(f"No content available for {title}")
        return

    # HTML, CSS, JavaScript를 포함한 문자열
    component = f"""
    <style>
    .fade-in {{
        opacity: 0;
        transition: opacity {duration}ms ease-in-out;
    }}
    .fade-in.visible {{
        opacity: 1;
    }}
    </style>
    <div id="fade-content-{title}" class="fade-in">{content}</div>
    <script>
    function setContentHeight() {{
        const content = document.getElementById('fade-content-{title}');
        if (content) {{
            content.parentElement.style.height = content.offsetHeight + 'px';
        }}
    }}

    function showContent() {{
        const content = document.getElementById('fade-content-{title}');
        if (content) {{
            content.classList.add('visible');
            setContentHeight();
        }}
    }}

    // 문서 로드 후 콘텐츠 표시 및 높이 설정
    document.addEventListener('DOMContentLoaded', () => {{
        setContentHeight();
        setTimeout(showContent, 100); // 약간의 지연 후 페이드인 시작
    }});

    // 창 크기 변경 시 높이 재조정
    window.addEventListener('resize', setContentHeight);
    </script>
    """
    # HTML을 렌더링
    components.html(component, height=0)  # 초기 높이를 0으로 설정

