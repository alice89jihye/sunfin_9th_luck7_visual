import streamlit as st
import pandas as pd
from component import divider
from component.font import customText as ct
from PIL import Image

def show_content():
    ct.subheaderNoLink("Data: ChaLearn First Impression V2 (CVPR’17)")
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



    ct.boldNoLink("")
    ct.regularNoLink("")
    ct.regularNoLink("")
    ct.regularNoLink("")
    divider.space(60)



show_content()




