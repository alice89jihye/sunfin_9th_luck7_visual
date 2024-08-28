import pandas as pd
import networkx as nx
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import streamlit as st
from streamlit_agraph import agraph, Config, Node, Edge

def show(df: pd.DataFrame):
    # 특성 벡터 준비
    features = df[['Neuroticism', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness']]
    
    # NearestNeighbors 모델 생성
    n_neighbors = min(len(df), 5)
    nbrs = NearestNeighbors(n_neighbors=n_neighbors, algorithm='auto').fit(features)
    distances, indices = nbrs.kneighbors(features)
    
    # 그래프 생성
    G = nx.Graph()
    
    # job 열의 고유 값과 색상 매핑 설정
    job_unique = df['job'].unique()
    colors = plt.get_cmap('tab20', len(job_unique))
    job_colors = {job: mcolors.to_hex(colors(i)) for i, job in enumerate(job_unique)}
    
    # 노드 추가
    for _, row in df.iterrows():
        G.add_node(row['FullName'], job=row['job'])
    
    # 엣지 추가
    for i, node in enumerate(df['FullName']):
        for j in indices[i][1:]:
            neighbor = df['FullName'].iloc[j]
            if not G.has_edge(node, neighbor):
                G.add_edge(node, neighbor, weight=distances[i][list(indices[i]).index(j)])
    
    # NetworkX 그래프를 streamlit_agraph에 맞게 변환
    nodes = []
    edges = []
    
    # 노드 색상 설정
    for node in G.nodes(data=True):
        job = node[1].get('job', 'unknown')
        color = job_colors.get(job, '#808080')
        nodes.append(Node(id=node[0], label=node[0], color=color))
    
    # 엣지 색상 설정
    for edge in G.edges(data=True):
        edge_weight = edge[2]['weight']
        source_job = df[df['FullName'] == edge[0]]['job'].values[0]
        target_job = df[df['FullName'] == edge[1]]['job'].values[0]
        color = job_colors.get(source_job, '#808080') if source_job == target_job else '#808080'
        edges.append(Edge(source=edge[0], target=edge[1], label=f"{edge_weight:.2f}", color=color))
    
    # 그래프 시각화
    config = Config(
        width="100%",
        height=600,
        directed=False,
        nodeHighlightBehavior=True,
        highlightColor="#F7A7A6",
        collapsible=False,
    )
    
    # 2열 레이아웃 생성
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # 그래프 생성
        graph_component = agraph(nodes=nodes, edges=edges, config=config)
    
    with col2:
        # 범례 생성
        st.markdown("<h4 style='text-align: center; font-size: 12px;'>Job Categories</h4>", unsafe_allow_html=True)
        legend_html = '<div style="font-size: 0.8em;">'
        for job, color in job_colors.items():
            legend_html += f'<div style="display: flex; align-items: center; margin-bottom: 3px;">'
            legend_html += f'<div style="width: 15px; height: 15px; background-color: {color}; margin-right: 5px;"></div>'
            legend_html += f'<span>{job}</span>'
            legend_html += '</div>'
        legend_html += '</div>'
        
        st.markdown(legend_html, unsafe_allow_html=True)
