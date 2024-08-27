import streamlit as st
import pandas as pd
from streamlit_agraph import agraph, Node, Edge, Config
from sklearn.neighbors import NearestNeighbors
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def show(df: pd.DataFrame):
    # 특성 벡터 준비
    features = df[['Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness']]
    
    # NearestNeighbors 모델 생성 (데이터 포인트 수보다 작은 n_neighbors 설정)
    n_neighbors = min(len(df), 5)  # 데이터 포인트 수보다 작게 설정
    nbrs = NearestNeighbors(n_neighbors=n_neighbors, algorithm='auto').fit(features)
    distances, indices = nbrs.kneighbors(features)
    
    # 그래프 생성
    G = nx.Graph()
    
    # job 열의 고유 값과 색상 매핑 설정
    job_unique = df['job'].unique()
    colors = plt.get_cmap('tab20', len(job_unique))  # 색상 맵 생성
    job_colors = {job: mcolors.to_hex(colors(i)) for i, job in enumerate(job_unique)}
    
    # 노드 추가 (FullName 사용)
    for _, row in df.iterrows():
        G.add_node(row['FullName'], job=row['job'])
    
    # 엣지 추가 (가장 가까운 이웃을 연결)
    for i, node in enumerate(df['FullName']):
        if len(indices[i]) > 1:
            for j in indices[i][1:]:
                neighbor = df['FullName'].iloc[j]
                if j < len(df) and not G.has_edge(node, neighbor):
                    G.add_edge(node, neighbor, weight=distances[i][list(indices[i]).index(j)])
    
    # NetworkX 그래프를 streamlit_agraph에 맞게 변환
    nodes = []
    edges = []
    
    # 노드 색상 설정
    for node in G.nodes(data=True):
        job = node[1].get('job', 'unknown')  # 'unknown'으로 기본값 설정
        color = job_colors.get(job, '#808080')  # 기본 색상은 회색
        nodes.append(Node(id=node[0], color=color))
    
    # 엣지 색상 설정
    for edge in G.edges(data=True):
        edge_weight = edge[2]['weight']
        nodes_source = edge[0]
        nodes_target = edge[1]
        
        # 노드의 job 정보 조회
        job_source = df[df['FullName'] == nodes_source]['job'].values
        job_target = df[df['FullName'] == nodes_target]['job'].values
        
        # job 정보가 존재하는지 확인
        color_source = job_colors.get(job_source[0] if len(job_source) > 0 else 'unknown', '#808080') if len(job_source) > 0 else '#808080'
        color_target = job_colors.get(job_target[0] if len(job_target) > 0 else 'unknown', '#808080') if len(job_target) > 0 else '#808080'
        
        # 엣지 색상 결정
        color = color_source if color_source == color_target else '#808080'
        
        edges.append(Edge(source=nodes_source, target=nodes_target, label=f"{edge_weight:.2f}", color=color))
    
    # 그래프 시각화
    config = Config(
        width=800,
        height=600,
        directed=False,
        nodeHighlightBehavior=True,
        highlightColor="#F7A7A6",
    )
    
    st.title('Full Name Network Graph with Nearest Neighbors and Job Colors')
    agraph(nodes=nodes, edges=edges, config=config)
    
    # 범례 생성
    st.subheader('Job Categories and Colors')
    legend_html = '<div style="display: flex; flex-direction: column;">'
    for job, color in job_colors.items():
        legend_html += f'<div style="display: flex; align-items: center; margin-bottom: 5px;">'
        legend_html += f'<div style="width: 20px; height: 20px; background-color: {color}; margin-right: 10px;"></div>'
        legend_html += f'<span>{job}</span>'
        legend_html += '</div>'
    legend_html += '</div>'
    
    st.markdown(legend_html, unsafe_allow_html=True)






