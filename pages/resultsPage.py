import streamlit as st
import pandas as pd
from component import divider
from component.font import customText as ct
from PIL import Image
import time
import streamlit.components.v1 as components
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import NearestNeighbors
from component import agraph, chordDiagram
import requests

def show_content():
    st.markdown("""
        <style>
        .reportview-container .main .block-container {
            padding-left: 10%;
            padding-right: 10%;
        }
        </style>
    """, unsafe_allow_html=True)
    
    ct.subheader("Predicted Results for Each Individual")
    divider.space(20)
    
    def get_image_size(image, width):
        # 이미지 열기 및 크기 계산
        img = Image.open(BytesIO(image))
        img_width, img_height = img.size
        aspect_ratio = img_height / img_width
        img_height = int(width * aspect_ratio)
        return img_width, img_height

    def resize_image(image, width):
        # 이미지 열기
        img = Image.open(BytesIO(image))
        img_width, img_height = img.size
        aspect_ratio = img_height / img_width
        new_height = int(width * aspect_ratio)
        img = img.resize((width, new_height), Image.LANCZOS)
        
        # 이미지를 base64로 인코딩
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()
        return img_base64

    def show_profile(name, image_url, traits, width=300):
        col1, col2 = st.columns([1, 1])
        
        # 성격 특성 정보 표시
        with col2:
            for trait, value in traits.items():
                st.markdown(f"● {trait}: {value:.3f}")
        
        time.sleep(1)
        with col1:
            try:
                # 이미지 다운로드
                response = requests.get(image_url)
                response.raise_for_status()
                
                # 이미지가 성공적으로 다운로드되었는지 확인
                if response.status_code == 200:
                    img_base64 = resize_image(response.content, width)
                    img_width, img_height = get_image_size(response.content, width)
                    
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
                else:
                    st.error("Failed to download image from Google Drive.")
            except Exception as e:
                st.error(f"이미지를 불러오는 데 문제가 발생했습니다: {e}")

    name = "박현우 교수님"
    file_id = '1umHddegTEOEeNwolh8XH7Qo0gu0ppE0r'
    download_url = f'https://drive.google.com/uc?id={file_id}'

    traits = {
        "Openness": 0.002,
        "Conscientiousness": 0.000,
        "Extraversion": 0.000,
        "Agreeableness": 0.726,
        "Neuroticism": 0.002
    }
    show_profile(name, download_url, traits)
    divider.divider("#d0d0d0")
    divider.space(40)

    image_paths = [
        "https://drive.google.com/uc?id=16xsCvAmN326XdNgQUVUw-3yyC44IF6zM",
        "https://drive.google.com/uc?id=1hRlbpYfMaqZrgRaX7nM8bBEufH4iT7Ip",
        "https://drive.google.com/uc?id=19CpzVV8sXsNn0X7EexIU65fHOiFXwvxB",
    ]
    
    data = {
        'Trait': ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism'],
        '박동근 1': [0.001, 0.000, 0.000, 0.861, 0.026],
        '박동근 2': [0.008, 0.000, 0.001, 0.834, 0.021],
        '박동근 3': [0.015, 0.001, 0.000, 0.850, 0.011]
    }

    def show_images_and_table(image_urls, data):
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
        cols = st.columns(len(image_urls) + 1)

        keys_list = list(data.keys())

        # Display images in columns, skipping the first column
        for i, image_url in enumerate(image_urls, 1):
            with cols[i]:  # Use cols[i] to skip the first column
                try:
                    # Download image
                    response = requests.get(image_url)
                    response.raise_for_status()
                    
                    # Open image
                    img = Image.open(BytesIO(response.content))
                    st.image(img, use_column_width=True, caption=f"{keys_list[i]}")
                except Exception as e:
                    st.error(f"Failed to load image from {image_url}: {e}")

        # Table display
        df = pd.DataFrame(data).set_index('Trait')
        st.dataframe(df.style.format("{:.3f}"), use_container_width=True)

    show_images_and_table(image_paths, data)
    dfs = pd.read_excel('data/stu_trait.xlsx', sheet_name=None)
    df_a = dfs['박동근']
    df_b = dfs['김병현']
    df_c = dfs['김소현']

    dfa = df_a

    # 그래프 설정
    plt.rcParams['axes.unicode_minus'] = False
    light_sky_blue = "#87CEFA"  # 연하늘색

    fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(20, 5))

    # 각 Trait별로 그래프 생성
    traits = dfa['Trait']
    for i, trait in enumerate(traits):
        ax = axes[i]
        # Trait에 해당하는 행을 필터링
        trait_data = dfa[dfa['Trait'] == trait].iloc[0, 1:]  # Trait에 해당하는 데이터
        ax.bar(dfa.columns[1:], trait_data, color=light_sky_blue)
        ax.set_ylim(0, trait_data.max() * 1.1)  # y축 범위 설정
        ax.set_title(trait)

        # 각 막대 위에 수치 표시
        for j, value in enumerate(trait_data):
            ax.text(j, value + (trait_data.max() * 0.02), f'{value:.3f}', ha='center')

    # 레이아웃 조정
    plt.tight_layout()

    # Streamlit에서 그래프 표시
    st.pyplot(fig)
    divider.space(60)

    image_paths = [
        "https://drive.google.com/uc?id=10DLLv_vf9PHGIoxDpkd95ps_-zonDKUb",
        "https://drive.google.com/uc?id=1RcZwZn3XPNY6CZ7Y_AKYeG4VP9uR03r1",
    ]
    
    data = {
        'Trait': ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism'],
        '김병현 1': [0.002, 0.008, 0.000, 0.159, 0.000],
        '김병현 2': [0.003, 0.013, 0.002, 0.596, 0.000],
    }
    show_images_and_table(image_paths, data)
    dfb = df_b
    fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(20, 5))
    # 각 Trait별로 그래프 생성
    traits = dfb['Trait']
    for i, trait in enumerate(traits):
        ax = axes[i]
        # Trait에 해당하는 데이터 필터링
        trait_data = dfb[dfb['Trait'] == trait].iloc[0, 1:]
        ax.bar(dfb.columns[1:], trait_data, color=light_sky_blue)
        ax.set_ylim(0, trait_data.max() * 1.1)  # y축 범위 설정
        ax.set_title(trait)

        # 각 막대 위에 수치 표시
        for j, value in enumerate(trait_data):
            ax.text(j, value + (trait_data.max() * 0.02), f'{value:.3f}', ha='center')

    # 레이아웃 조정
    plt.tight_layout()

    # Streamlit에서 그래프 표시
    st.pyplot(fig)
    divider.space(60)

    image_paths = [
        "https://drive.google.com/uc?id=1cIoNDsHQJaLY9_hGFclnXcjTLwJma5zh",
        "https://drive.google.com/uc?id=1iIef2ILe5XlH7F6su-ebTg6Hr-BEqqK-",
    ]
    
    data = {
        'Trait': ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism'],
        '김소현 1': [0.005, 0.000, 0.001, 0.155, 0.002],
        '김소현 2': [0.024, 0.000, 0.000, 0.178, 0.002],
    }
    show_images_and_table(image_paths, data)
    dfc = df_c
    fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(20, 5))
    # 각 Trait별로 그래프 생성
    traits = dfc['Trait']
    for i, trait in enumerate(traits):
        ax = axes[i]
        # Trait에 해당하는 데이터 필터링
        trait_data = dfc[dfc['Trait'] == trait].iloc[0, 1:]
        ax.bar(dfc.columns[1:], trait_data, color=light_sky_blue)
        ax.set_ylim(0, trait_data.max() * 1.1)  # y축 범위 설정
        ax.set_title(trait)

        # 각 막대 위에 수치 표시
        for j, value in enumerate(trait_data):
            ax.text(j, value + (trait_data.max() * 0.02), f'{value:.3f}', ha='center')

    # 레이아웃 조정
    plt.tight_layout()

    # Streamlit에서 그래프 표시
    st.pyplot(fig)
    divider.space(80)

    ct.subheader("Descriptive Statistics")
    df = pd.read_csv('data/df3_after_cls_with_name.csv')
    
    describe_traits = df[['Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness']].describe()
    st.dataframe(describe_traits, use_container_width=True)
    divider.space(60)

    ct.subheader("Distribution of Personality Traits per Job")
    job_list = df['job'].unique()
    # 각 직군별로 데이터를 출력하는 for 루프
    for job in job_list:
        ct.bold(f"* {job}")

        # 해당 직군에 해당하는 데이터 필터링
        filtered_df = df[df['job'] == job]

        # 선택된 직군에 대한 요약 통계 구하기
        describe_by_job = filtered_df[['Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness']].describe()

        # 1행: 요약 통계 출력
        st.dataframe(describe_by_job, use_container_width=True)

        # 히스토그램 그리기
        traits = ['Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness']
        
        # 모든 히스토그램에 대한 공통 설정
        fig_width, fig_height = 10, 6  # 히스토그램 크기 설정

        # 첫 번째 행: 3개의 히스토그램
        col1, col2, col3 = st.columns(3)
        
        with col1:
            plt.figure(figsize=(fig_width, fig_height))
            sns.histplot(filtered_df[traits[0]], kde=True, bins=10)
            plt.title(f'{traits[0]} Distribution', fontsize=20)
            plt.xlabel(traits[0], fontsize=16)
            plt.ylabel('Frequency', fontsize=16)
            st.pyplot(plt)
            plt.clf()

        with col2:
            plt.figure(figsize=(fig_width, fig_height))
            sns.histplot(filtered_df[traits[1]], kde=True, bins=10)
            plt.title(f'{traits[1]} Distribution', fontsize=20)
            plt.xlabel(traits[1], fontsize=16)
            plt.ylabel('Frequency', fontsize=16)
            st.pyplot(plt)
            plt.clf()

        with col3:
            plt.figure(figsize=(fig_width, fig_height))
            sns.histplot(filtered_df[traits[2]], kde=True, bins=10)
            plt.title(f'{traits[2]} Distribution', fontsize=20)
            plt.xlabel(traits[2], fontsize=16)
            plt.ylabel('Frequency', fontsize=16)
            st.pyplot(plt)
            plt.clf()

        # 두 번째 행: 2개의 히스토그램 (중앙 정렬)
        col1, col2, col3, col4 = st.columns([1, 3, 3, 1])
        
        with col2:
            plt.figure(figsize=(fig_width, fig_height))
            sns.histplot(filtered_df[traits[3]], kde=True, bins=10)
            plt.title(f'{traits[3]} Distribution', fontsize=20)
            plt.xlabel(traits[3], fontsize=16)
            plt.ylabel('Frequency', fontsize=16)
            st.pyplot(plt)
            plt.clf()

        with col3:
            plt.figure(figsize=(fig_width, fig_height))
            sns.histplot(filtered_df[traits[4]], kde=True, bins=10)
            plt.title(f'{traits[4]} Distribution', fontsize=20)
            plt.xlabel(traits[4], fontsize=16)
            plt.ylabel('Frequency', fontsize=16)
            st.pyplot(plt)
            plt.clf()

        st.write("<br>", unsafe_allow_html=True)  # 간격 추가
    divider.space(80)

    ct.subheader("Dominant Personality Traits per Job")
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

    ct.subheader("Who is Close to Whom?")
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

    ct.caption("Knn (k=4)")
    st.dataframe(value1, use_container_width=True, hide_index=True)
    divider.space(20)

    ct.caption("Knn (k=4)")
    st.dataframe(value2, use_container_width=True, hide_index=True)
    divider.space(60)

    ct.bold("Network Graph")
    ct.caption("(* the edge weights in the graph: Euclidean distance)")
    agraph.show(df)
    divider.space(60)
    
    ct.bold("Chord Diagram")
    chordDiagram.show(df)
    divider.space(60)
    


show_content()




