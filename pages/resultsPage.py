import streamlit as st
import pandas as pd
from component import divider
from component.font import customText as ct
from PIL import Image
import time
import streamlit.components.v1 as components
import os
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import NearestNeighbors
from component import agraph, chordDiagram


def show_content():
    ct.subheaderNoLink("Predicted Results for Each Individual")
    divider.space(20)

    def get_image_size(image_path, width):
        with Image.open(image_path) as img:
            w, h = img.size
            aspect_ratio = h / w
            new_height = int(width * aspect_ratio)
            return width, new_height

    def resize_image(image_path, width):
        with Image.open(image_path) as img:
            w, h = img.size
            aspect_ratio = h / w
            new_height = int(width * aspect_ratio)
            img_resized = img.resize((width, new_height), Image.LANCZOS)
            buffered = BytesIO()
            img_resized.save(buffered, format="PNG")
            return base64.b64encode(buffered.getvalue()).decode()

    # 현재 파일의 위치를 기준으로 상대 경로 설정
    current_dir = os.path.dirname(__file__)

    def show_profile(name, image_path, traits, width=300):
        col1, col2 = st.columns([1, 1])
        
        # 성격 특성 정보 표시
        with col2:
            divider.space(120)
            for trait, value in traits.items():
                st.markdown(f"● {trait}: {value:.3f}")
        
        imgPath = os.path.join(current_dir, image_path)
        time.sleep(1)
        with col1:
            # 이미지 파일 존재 확인
            if os.path.exists():
                try:
                    # 이미지 크기 계산 및 리사이즈
                    img_width, img_height = get_image_size(imgPath, width)
                    img_base64 = resize_image(imgPath, width)
                    
                    # HTML로 이미지와 캡션 표시
                    html_content = f"""
                    <style>
                        .image-container {{
                            text-align: center;
                        }}
                        .profile-image {{
                            width: {img_width}px;
                            height: {img_height}px;
                            object-fit: cover;
                        }}
                        .image-caption {{
                            margin-top: 10px;
                            font-style: italic;
                            color: #666;
                        }}
                    </style>
                    <div class="image-container">
                        <img src="data:image/png;base64,{img_base64}" class="profile-image" alt="{name}">
                        <div class="image-caption">{name}</div>
                    </div>
                    """
                    components.html(html_content, height=img_height+50)  # 캡션을 위해 추가 공간 확보
                except Exception as e:
                    st.error(f"이미지를 불러오는 데 문제가 발생했습니다: {e}")
            else:
                st.error(f"이미지 파일을 찾을 수 없습니다: {imgPath}")


    name = "박현우 교수님"
    image_path = "./data/images_for_prediction/09_박현우교수님.png"
    traits = {
        "Openness": 0.002,
        "Conscientiousness": 0.000,
        "Extraversion": 0.000,
        "Agreeableness": 0.726,
        "Neuroticism": 0.002
    }
    show_profile(name, image_path, traits)
    divider.space(60)

    image_paths = [
        "./data/images_for_prediction/04_동근1.png",
        "./data/images_for_prediction/05_동근2.png",
        "./data/images_for_prediction/06_동근3.png"
    ]
    
    data = {
        'Trait': ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism'],
        '박동근 1': [0.001, 0.000, 0.000, 0.861, 0.026],
        '박동근 2': [0.008, 0.000, 0.001, 0.834, 0.021],
        '박동근 3': [0.015, 0.001, 0.000, 0.850, 0.011]
    }

    def show_images_and_table(image_paths, data):
        # CSS for layout
        st.markdown("""
        <style>
        .dataframe {
            font-size: 12px;
            text-align: center;
        }
        .dataframe th, .dataframe td {
            text-align: center !important;
        }
        </style>
        """, unsafe_allow_html=True)

        # Create columns for images plus one empty column
        cols = st.columns(len(image_paths) + 1)

        keys_list = list(data.keys())
        # Display images in columns, skipping the first column
        for i, img_path in enumerate(image_paths, 1):
            with cols[i]:  # Use cols[i] to skip the first column
                img = Image.open(os.path.join(current_dir, img_path))
                st.image(img, use_column_width=True, caption=f"{keys_list[i]}")

        # Table display
        df = pd.DataFrame(data).set_index('Trait')
        st.dataframe(df.style.format("{:.3f}"), use_container_width=True)


    show_images_and_table(image_paths, data)
    divider.space(60)

    image_paths = [
        "./data/images_for_prediction/10_병현님1.png",
        "./data/images_for_prediction/11_병현님2.png",
    ]
    
    data = {
        'Trait': ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism'],
        '김병현 1': [0.002, 0.008, 0.000, 0.159, 0.000],
        '김병현 2': [0.003, 0.013, 0.002, 0.596, 0.000],
    }
    show_images_and_table(image_paths, data)
    divider.space(60)

    image_paths = [
        "./data/images_for_prediction/25_김소현1.png",
        "./data/images_for_prediction/26_김소현2.png",
    ]
    
    data = {
        'Trait': ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism'],
        '김소현 1': [0.005, 0.000, 0.001, 0.155, 0.002],
        '김소현 2': [0.024, 0.000, 0.000, 0.178, 0.002],
    }
    show_images_and_table(image_paths, data)
    divider.space(60)

    ct.subheaderNoLink("Descriptive Statistics")
    df = pd.read_csv('data/df3_after_cls_with_name.csv')
    describe_traits = df[['Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness']].describe()
    st.dataframe(describe_traits)
    divider.space(60)

    ct.subheaderNoLink("Distribution of Personality Traits per Job")
    job_list = df['job'].unique()
    # 각 직군별로 데이터를 출력하는 for 루프
    for job in job_list:
        ct.boldNoLink(f"Traits Summary and Distribution for Job: {job}")

        # 해당 직군에 해당하는 데이터 필터링
        filtered_df = df[df['job'] == job]

        # 선택된 직군에 대한 요약 통계 구하기
        describe_by_job = filtered_df[['Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness']].describe()

        # 1행: 요약 통계 출력
        # st.write("### Summary Statistics")
        st.dataframe(describe_by_job)

        # 2행: 히스토그램 그리기
        # st.write("### Histogram of Traits")

        # 2행에 3개의 열 생성
        col1, col2, col3 = st.columns(3)

        # 각 열에 히스토그램 추가
        with col1:
            plt.figure(figsize=(15, 10))
            sns.histplot(filtered_df['Neuroticism'], kde=True, bins=10)
            plt.title('Neuroticism Distribution')
            plt.xlabel('Neuroticism')
            plt.ylabel('Frequency')
            st.pyplot(plt)
            plt.clf()  # 그래프 초기화

        with col2:
            plt.figure(figsize=(15, 10))
            sns.histplot(filtered_df['Extraversion'], kde=True, bins=10)
            plt.title('Extraversion Distribution')
            plt.xlabel('Extraversion')
            plt.ylabel('Frequency')
            st.pyplot(plt)
            plt.clf()  # 그래프 초기화

        with col3:
            plt.figure(figsize=(15, 10))
            sns.histplot(filtered_df['Agreeableness'], kde=True, bins=10)
            plt.title('Agreeableness Distribution')
            plt.xlabel('Agreeableness')
            plt.ylabel('Frequency')
            st.pyplot(plt)
            plt.clf()  # 그래프 초기화

        # 두 번째 행에 2개의 열 생성
        col4, col5 = st.columns(2)

        # 각 열에 히스토그램 추가
        with col4:
            plt.figure(figsize=(15, 10))
            sns.histplot(filtered_df['Conscientiousness'], kde=True, bins=10)
            plt.title('Conscientiousness Distribution')
            plt.xlabel('Conscientiousness')
            plt.ylabel('Frequency')
            st.pyplot(plt)
            plt.clf()  # 그래프 초기화

        with col5:
            plt.figure(figsize=(15, 10))
            sns.histplot(filtered_df['Openness'], kde=True, bins=10)
            plt.title('Openness Distribution')
            plt.xlabel('Openness')
            plt.ylabel('Frequency')
            st.pyplot(plt)
            plt.clf()  # 그래프 초기화
    divider.space(80)

    ct.subheaderNoLink("Dominant Personality Traits per Job")
    # 직군별 평균 점수를 계산하여 주요 성격 특성 구하기
    traits = ['Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness']

    # 각 직군별로 평균 점수를 계산
    mean_scores = df.groupby('job')[traits].mean()

    # 각 직군별로 주된 성격 특성 찾기
    dominant_traits = mean_scores.idxmax(axis=1)
    dominant_scores = mean_scores.max(axis=1)

    # Dominant traits 데이터프레임 생성
    dominant_df = pd.DataFrame({
        'Job': mean_scores.index,
        'Dominant_Trait': dominant_traits,
        'Mean_Score': dominant_scores
    })

    plt.figure(figsize=(10, 8))
    plt.barh(dominant_df['Job'], dominant_df['Mean_Score'], color='skyblue')
    for index, value in enumerate(dominant_df['Mean_Score']):
        plt.text(value, index, f'{dominant_df["Dominant_Trait"].iloc[index]} ({value:.2f})', va='center')

    plt.xlabel('Mean Score')
    plt.title('Dominant Personality Trait by Job')
    st.pyplot(plt)
    plt.clf()  # 그래프 초기화
    divider.space(60)

    ct.subheaderNoLink("Who is Close to Whom?")
    # Define a function to get nearest neighbors
    def get_nearest_neighbors_with_distances(df, person_idx, n_neighbors=4):
        X = df[['Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness']]
        knn = NearestNeighbors(n_neighbors=n_neighbors, algorithm='auto').fit(X)
        sample_point = X.iloc[person_idx].values.reshape(1, -1)
        distances, indices = knn.kneighbors(sample_point)
        nearest_neighbors = df.iloc[indices[0]]
        # Add distances as a new column
        nearest_neighbors['Distance'] = distances[0]
        return nearest_neighbors

    # Get nearest neighbors with distances for both indices
    value1 = get_nearest_neighbors_with_distances(df, person_idx=11)
    value2 = get_nearest_neighbors_with_distances(df, person_idx=13)

    # Select specific columns to include (excluding the first column)
    value1 = value1.iloc[:, [value1.columns.get_loc(c) for c in ['Name', 'Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness', 'Distance']]]
    value2 = value2.iloc[:, [value2.columns.get_loc(c) for c in ['Name', 'Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness', 'Distance']]]

    # Combine the two dataframes
    combined_df = pd.concat([value1, value2], ignore_index=True)
    ct.caption("Knn (k=4)")
    st.dataframe(combined_df)
    divider.space(60)

    agraph.show(df)
    divider.space(60)
    
    chordDiagram.show(df)
    


show_content()




