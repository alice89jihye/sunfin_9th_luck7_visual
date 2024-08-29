import streamlit as st
import pandas as pd
from component import divider
from component.font import customText as ct
from PIL import Image
import base64
from io import BytesIO

def show_content():
    image1 = Image.open("./data/img/bg2.png")

    # 이미지를 base64로 인코딩
    buffered = BytesIO()
    image1.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # CSS 스타일 정의
    css = f"""
    <style>
    .stApp {{
        background-image: url(data:image/png;base64,{img_str});
        background-size: 50% auto;
        background-position: bottom right;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    st.markdown("""
        <style>
        .reportview-container .main .block-container {
            padding-left: 10%;
            padding-right: 10%;
        }
        </style>
    """, unsafe_allow_html=True)

    ct.subheader("Big Five Personalit")
    divider.space(40)

    ct.bold("What is PERSONALITY?")
    ct.regular("Allport, G. W. (1937). Personality: a psychological interpretation. Holt.")
    ct.link("https://archive.org/details/in.ernet.dli.2015.155561/page/n45/mode/2up", "https://archive.org/details/in.ernet.dli.2015.155561/page/n45/mode/2up", "#0000FF", "8px", "16px", "40px")
    divider.space(40)

    ct.mixed_style_text("“Persona”","_ the theatrical mask first used in Greek drama")
    ct.italic("peri sô ma (around the body)")
    ct.italic("persum (head or face; the Etruscan and Old Latin).",)
    ct.italic("per se una (self-containing; the Latin).®")
    divider.space(60)

    ct.bold("MBTI vs. FFM (Five-Factor-Model)")
    st.markdown("""
        <style>
        .stImage > img {
            display: block;
            margin: auto;
        }
        .image-caption {
            text-align: center;
            margin-top: 10px;
            font-size: 16px;
        }
        </style>
        """, unsafe_allow_html=True)

    # 이미지 로드
    image1 = Image.open("./data/img/mbti.png")
    image2 = Image.open("./data/img/bigFive.png")

    # 두 개의 컬럼 생성
    col1, col2 = st.columns(2)

    # 첫 번째 컬럼에 MBTI 이미지 표시
    with col1:
        st.image(image1)
        st.markdown('<p class="image-caption">MBTI</p>', unsafe_allow_html=True)

    # 두 번째 컬럼에 Big Five 이미지 표시
    with col2:
        st.image(image2)
        st.markdown('<p class="image-caption">Big Five</p>', unsafe_allow_html=True)
    divider.space(60)
    
    ct.bold("MBTI vs. FFM (Five-Factor-Model)")
    data = {
        "Aspect": [
            "Foundation", "Core Concept", "Number of Dimensions", "Measurement Approach", 
            "Outcome", "Nuance in Results", "Perspective on Self-Improvement", 
            "View on Personality Dynamics", "Optimism/Positivity", "Use in Professional Settings", 
            "Basis of Evaluation", "Correlation with Each Other"
        ],
        "Myers-Briggs personality typing system (MBTI)": [
            "Personality types", "Identifies you as belonging to one of 16 personality types", 
            "Four pairs of opposing traits (e.g., Introversion vs. Extraversion)", 
            "Either/or choices that categorize into one side of each dichotomy", 
            "Four-letter personality type (e.g., INTJ, ESTP)", 
            "Limited use of spectrum, focuses on dominant preferences", 
            "All types are equally valid, no type is better than another", 
            "Preferences are not absolute; traits can shift depending on circumstances", 
            "Neutral stance; focuses on managing emotions and maximizing personal potential", 
            "Less common, mainly for personal insight", 
            "Theoretical psychological concepts", 
            "Some correlation; for example, INTJs often score high on Openness and Conscientiousness in Big Five"
        ],
        "Five-Factor Model (FFM) / Big Five": [
            "Personality traits", "Measures personality on five broad dimensions", 
            "Five dimensions (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism)", 
            "Spectrum or continuum approach, giving a percentage score for each trait", 
            "High, low, or average scores in each of the five traits, no specific 'type'", 
            "High nuance, as traits are measured along a continuum", 
            "Some traits are viewed as healthier or more desirable than others", 
            "Continuum allows for more nuanced self-assessment and potential for growth", 
            "More critical; identifies areas where improvement is necessary for better adjustment", 
            "Widely used in hiring and professional development, considered more scientifically valid", 
            "Empirical data from personality research", 
            "Distinct systems, but with some complementary"
        ]
    }
    df = pd.DataFrame(data).reset_index(drop=True)
    st.markdown("""
        <style>
        .table {
            width: 100%;
            border-collapse: collapse;
        }
        .table th, .table td {
            border: 1px solid #ddd;
            padding: 8px;
            word-wrap: break-word;
            white-space: normal;
            text-align: left;
        }
        .table th {
            background-color: #f2f2f2;
            text-align: center;
        }
        .table tr {
            height: 80px; /* 행 높이 조정 */
        }
        </style>
    """, unsafe_allow_html=True)

    # 데이터프레임을 HTML로 렌더링
    st.markdown(df.to_html(classes='table', index=False), unsafe_allow_html=True)
    divider.space(60)

    ct.bold("FFM (Five-Factor-Model)")
    divider.space(20)
    ct.regular("Lexical hypothesis")
    ct.regular("  1. Those personality characteristics that are important to a group of people will eventually become a part of that group's language.")
    ct.regular("  2. More important personality characteristics are more likely to be encoded into language as a single word.")
    divider.space(20)
    ct.regular("Clustering words / Factor Analysis")
    divider.space(60)

    ct.bold("MBTI (Myers-Briggs personality typing system)")
    st.markdown("""
        <style>
            .mbti-question {
                font-size: 16px;
                margin-bottom: 10px;
            }
            .mbti-question-title {
                font-weight: bold;
            }
            .mbti-question-option {
                margin-left: 20px;
            }
        </style>
        """, unsafe_allow_html=True)

    # MBTI 질문 표시 함수
    def display_mbti_question(number, question, options):
        st.markdown(f"""
        <div class="mbti-question">
            <span class="mbti-question-title">{number}. {question}</span><br>
            <span class="mbti-question-option">a. {options[0]}</span><br>
            <span class="mbti-question-option">b. {options[1]}</span>
        </div>
        """, unsafe_allow_html=True)

    # MBTI 질문 리스트
    mbti_questions = [
        ("At a party do you:", ["Interact with many, including strangers", "Interact with a few, known to you"]),
        ("Are you more:", ["Realistic than speculative", "Speculative than realistic"]),
        ("Is it worse to:", ["Have your \"head in the clouds\"", "Be \"in a rut\""]),
        ("Are you more impressed by:", ["Principles", "Emotions"]),
        ("Are more drawn toward the:", ["Convincing", "Touching"]),
        ("Do you prefer to work:", ["To deadlines", "Just \"whenever\""]),
        ("Do you tend to choose:", ["Rather carefully", "Somewhat impulsively"]),
        ("At parties do you:", ["Stay late, with increasing energy", "Leave early with decreased energy"]),
        ("Are you more attracted to:", ["Sensible people", "Imaginative people"]),
        ("Are you more interested in:", ["What is actual", "What is possible"]),
        ("In judging others are you more swayed by:", ["Laws than circumstances", "Circumstances than laws"]),
        ("In approaching others is your inclination to be somewhat:", ["Objective", "Personal"]),
        ("Are you more:", ["Punctual", "Leisurely"]),
        ("Does it bother you more having things:", ["Incomplete", "Completed"]),
        ("In your social groups do you:", ["Keep abreast of other's happenings", "Get behind on the news"]),
        ("In doing ordinary things are you more likely to:", ["Do it the usual way", "Do it your own way"]),
        ("Writers should:", ["\"Say what they mean and mean what they say\"", "Express things more by use of analogy"]),
        ("Which appeals to you more:", ["Consistency of thought", "Harmonious human relationships"]),
        ("Are you more comfortable in making:", ["Logical judgments", "Value judgments"]),
        ("Do you want things:", ["Settled and decided", "Unsettled and undecided"])
    ]

    col1, col2, col3 = st.columns(3)

    for i, (question, options) in enumerate(mbti_questions, start=1):
        if i <= 7:
            with col1:
                display_mbti_question(i, question, options)
        elif i <= 14:
            with col2:
                display_mbti_question(i, question, options)
        else:
            with col3:
                display_mbti_question(i, question, options)
    ct.link2("http://www.lrjj.cn/encrm1.0/public/upload/MBTI-personality-test.pdf", "http://www.lrjj.cn/encrm1.0/public/upload/MBTI-personality-test.pdf")
    divider.space(80)

    ct.bold("FFM (Five-Factor-Model)")
    image1 = Image.open("./data/img/ffm1.png")
    image2 = Image.open("./data/img/ffm2.png")
    # 두 개의 컬럼 생성
    col1, col2 = st.columns(2)

    # 첫 번째 컬럼에 MBTI 이미지 표시
    with col1:
        st.markdown('<div class="bottom-aligned-image-container">', unsafe_allow_html=True)
        st.markdown('<div class="bottom-aligned-image">', unsafe_allow_html=True)
        st.image(image1, use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 두 번째 컬럼에 Big Five 이미지 표시
    with col2:
        st.markdown('<div class="bottom-aligned-image-container">', unsafe_allow_html=True)
        st.markdown('<div class="bottom-aligned-image">', unsafe_allow_html=True)
        st.image(image2, use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    ct.link2("https://test2.thepersonalitylab.org/version-test/v2_mobile_big", "https://test2.thepersonalitylab.org/version-test/v2_mobile_big")
    divider.space(60)

    ct.bold("Personality traits")
    ct.regular("Patterns of thought, feeling, and behaviour that are relatively enduring across an individual’s life span.")
    divider.space(40)
    ct.bold("Openness to Experience")
    ct.regular("This trait reflects how open-minded, imaginative, and willing to try new things a person is.")
    ct.regular("Individuals high in openness are curious, creative, and enjoy exploring new ideas and experiences.")
    ct.regular("Those low in openness tend to be more traditional, prefer routine, and are less comfortable with change.")
    divider.space(40)

    ct.bold("Conscientiousness")
    ct.regular("This trait measures a person’s degree of organization, dependability, and discipline.")
    ct.regular("High conscientiousness is associated with being thorough, careful, and efficient, often linked to strong work ethic and reliability.")
    ct.regular("Low conscientiousness may manifest as being more spontaneous, less organized, and sometimes more easy-going.")
    divider.space(40)
    ct.bold("Extraversion")
    ct.regular("This trait describes the extent to which a person is sociable, outgoing, and enjoys interacting with others. ")
    ct.regular("High extraversion is linked to being energetic, talkative, and assertive.")
    ct.regular("Those low in extraversion (introverts) tend to be more reserved, quiet, and enjoy solitary activities or smaller, more intimate social settings.")
    divider.space(40)

    ct.bold("Agreeableness")
    ct.regular("This trait reflects a person’s tendency to be compassionate, cooperative, and willing to help others.")
    ct.regular("People high in agreeableness are often kind, empathetic, and good-natured,")
    ct.regular("whereas those low in agreeableness may be more competitive, skeptical, or even confrontational.")
    divider.space(40)
    ct.bold("Neuroticism")
    ct.regular("This trait indicates how prone a person is to experiencing negative emotions like anxiety, anger, or depression.")
    ct.regular("High neuroticism is associated with emotional instability and vulnerability to stress.")
    ct.regular("Conversely, low neuroticism is linked to emotional resilience, calmness, and stability")
    divider.space(60)



show_content()




