import streamlit as st
import pandas as pd
from component import divider
from component.font import customText as ct
from PIL import Image

def show_content():
    ct.subheaderNoLink("Different Types of Self")
    ct.regularNoLink("Who I really am vs. The one I want to be vs. The one I have to be")
    divider.space(60)
    ct.regularNoLink("What does the image data tell us about people?")
    ct.regularNoLink("Social Personality")
    divider.space(60)
    ct.subheaderNoLink("Further questions")
    st.markdown("""
    <style>
        .custom-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .custom-list-item {
            display: flex;
            margin-bottom: 10px;
        }
        .custom-list-item .bullet {
            font-size: 24px;
            margin-right: 10px;
        }
        .custom-list-item .content {
            font-size: 16px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <ul class="custom-list">
        <li class="custom-list-item">
            <span class="bullet">●</span>
            <span class="content">What if images are sourced from platforms like Instagram that contain conspicuous elements?</span>
        </li>
        <li class="custom-list-item">
            <span class="bullet">●</span>
            <span class="content">Are there differences across different cultures or countries?</span>
        </li>
        <li class="custom-list-item">
            <span class="bullet">●</span>
            <span class="content">Are there differences in various contexts, such as consumption or employment contexts?</span>
        </li>
    </ul>
    """, unsafe_allow_html=True)
    divider.space(60)



show_content()




