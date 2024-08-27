import streamlit as st
import pandas as pd
import seaborn as sns
from component import agraph, chordDiagram, matplotlib, seaborn, altair, plotly

df = pd.read_csv('data/df3_after_cls_with_name.csv')

chordDiagram.show(df)
agraph.show(df)
