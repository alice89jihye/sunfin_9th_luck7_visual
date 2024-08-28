import streamlit as st
import pandas as pd
from component import divider
from component.font import customText as ct
from PIL import Image

def show_content():
    ct.subheaderNoLink("Predicted Results for Each Individual")
    st.image("./data/img/chaLearn.png", use_column_width=True)
    ct.link2("https://chalearnlap.cvc.uab.cat/dataset/24/description/","https://chalearnlap.cvc.uab.cat/dataset/24/description/")
    divider.space(60)

    st.image("./data/img/chaLearn2.png", use_column_width=True)
    ct.link2("https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8999746","https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8999746")
    divider.space(60)

    ct.subheaderNoLink("Summary of Procedures")
    """
    1. Train the original model
       * 5999 Training set, 1997 Validation set, 240 Test set
       * MobileNet V2 architecture

    2. Use the original model as a Pre-Trained model

    3. Prediction

    4. Visualization
    """
    divider.space(60)

    ct.subheaderNoLink("1. Training the original model")
    ct.boldNoLink("3 video samples from train, validation and test sets")
    divider.space(10)
    st.image("./data/img/videoSamplesTest1.png", use_column_width=True)
    divider.space(20)
    st.image("./data/img/videoSamplesTest2.png", use_column_width=True)

    image1 = Image.open("./data/img/videoSamplesTest3.png")
    image2 = Image.open("./data/img/videoSamplesTest4.png")
    image3 = Image.open("./data/img/videoSamplesTest5.png")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(image1, use_column_width=True)
    with col2:
        st.image(image2, use_column_width=True)
    with col3:
        st.image(image3, use_column_width=True)
    divider.space(80)

    ct.boldNoLink("Creating a Model")
    ct.regularNoLink("Audio Subnetwork + Visual Subnetwork")
    ct.regularNoLink("☞ Combined Network")
    st.image("./data/img/model.png", use_column_width=True)
    ct.regularNoLink("Early Stopping (monitor=’val_loss’, patience = 3), Epoch = 20")
    ct.regularNoLink("Train input")
    html_content = """
    <style>
        .container {
            font-family: serif;
            line-height: 1.2;
        }
        .input {
            margin-left: 40px;
        }
        .large-text {
            font-size: 14px;
        }
        .medium-text {
            font-size: 14px;
        }
    </style>

    <div class="container">
        <div class="input">
            <div class="large-text">X: Audio data and image data</div>
            <div class="medium-text">y: Personality traits annotation</div>
        </div>
    </div>
    """

    st.markdown(html_content, unsafe_allow_html=True)
    divider.space(20)
    st.image("./data/img/model1.png", use_column_width=True)
    st.image("./data/img/model2.png", use_column_width=True)
    st.image("./data/img/model3.png", use_column_width=True)
    divider.space(60)
    
    ct.subheader("2. Use the Original Model as a Pre-Trained Model")
    st.image("./data/img/model4.png", use_column_width=True)
    st.image("./data/img/model5.png", use_column_width=True)
    st.image("./data/img/model6.png", use_column_width=True)
    divider.space(60)

    ct.subheader("3. Prediction")
    ct.boldNoLink("Preprocessing")
    ct.regularNoLink("Resize the images (target size = 128 * 128)")
    """
    Augmentation
    (Original Image, Slight Rotation, Horizontal Flip, Slight Shift, Slight brightness adjustment, Gaussian blur)
    """
    ct.boldNoLink("Load Images")
    ct.boldNoLink("Prediction and Make a dataset")

    data = {
    'Name': ['최지혜', '박동근3', '박동근2', '박동근1', '신주환', '박홍석', '유지훈'],
    'FullName': ['Choi Ji-hye', 'Park Dong-keun 3', 'Park Dong-keun 2', 'Park Dong-keun 1', 'Shin Joo-hwan', 'Park Hong-seok', 'Yoo Ji-hoon'],
    'Neuroticism': [0.001, 0.011, 0.021, 0.026, 0.2, 0.003, 0.0],
    'Extraversion': [0.014, 0.0, 0.001, 0.0, 0.005, 0.025, 0.187],
    'Agreeableness': [0.155, 0.85, 0.834, 0.861, 0.17, 0.483, 0.071],
    'Conscientiousness': [0.0, 0.001, 0.0, 0.0, 0.005, 0.0, 0.0],
    'Openness': [0.221, 0.015, 0.008, 0.001, 0.001, 0.0, 0.0],
    'job': ['student', 'student', 'student', 'student', 'student', 'student', 'student']
    }

    # DataFrame 생성
    df = pd.DataFrame(data)

    # 데이터프레임 표시
    st.dataframe(
        df.style
        .set_table_styles([
            {'selector': 'th', 'props': [('background-color', '#f0f0f0'), ('color', 'black'), ('font-weight', 'bold')]},
            {'selector': 'td', 'props': [('background-color', 'white'), ('color', 'black')]},
            {'selector': '', 'props': [('border', '1px solid black')]}
        ])
        .format({
            'Neuroticism': '{:.3f}',
            'Extraversion': '{:.3f}',
            'Agreeableness': '{:.3f}',
            'Conscientiousness': '{:.3f}',
            'Openness': '{:.3f}'
        }),
        height=300,
        use_container_width=True
    )

    # CSS를 사용한 추가 스타일링
    st.markdown("""
    <style>
        .dataframe {
            font-family: Arial, sans-serif;
        }
        .dataframe th {
            text-align: center !important;
        }
        .dataframe td {
            text-align: center !important;
        }
    </style>
    """, unsafe_allow_html=True)
    divider.space(60)

    ct.subheader("4. Visualization")
    ct.regularNoLink("Distribution of Personality Traits per Job")
    ct.regularNoLink("Dominant Personality Traits per Job")
    
    html_content = """
    <style>
        .container {
            font-family: serif;
            text-align: left;
            line-height: 1.2;
        }
        .title {
            margin-top: 4px;
            font-size: 16px;
        }
        .subtitle {
            font-size: 16px;
            margin-left: 40px;
        }
        .italic {
            font-style: italic;
        }
    </style>

    <div class="container">
        <div class="title">Who is Close to Whom?</div>
        <div class="subtitle"><span class="italic">knn (k=4)</span> → Network Graph</div>
    </div>
    """

    # HTML 내용 렌더링
    st.markdown(html_content, unsafe_allow_html=True)
    divider.space(20)
    ct.caption("Software: Python, Streamlit")
    divider.space(60)

    ct.boldNoLink("")
    ct.regularNoLink("")
    ct.regularNoLink("")
    ct.regularNoLink("")
    divider.space(60)



show_content()




