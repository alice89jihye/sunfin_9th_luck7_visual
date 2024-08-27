import streamlit as st
import streamlit.components.v1 as components

def scroll_fade_in(content, duration=1000):
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
    <div id="fade-content" class="fade-in">{content}</div>
    <script>
    const observer = new IntersectionObserver((entries) => {{
        entries.forEach(entry => {{
            if (entry.isIntersecting) {{
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }}
        }});
    }}, {{ threshold: 0.1 }});

    const fadeContent = document.getElementById('fade-content');
    observer.observe(fadeContent);
    </script>
    """
    # HTML을 렌더링
    components.html(component, height=600)  # 높이는 콘텐츠에 따라 조정 필요