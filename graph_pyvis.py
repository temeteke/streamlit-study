from pathlib import Path

import networkx as nx
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network

st.write("# 磯野家")

df = pd.DataFrame([
    {'name': '波平', 'child': 'サザエ'},
    {'name': '波平', 'child': 'カツオ'},
    {'name': '波平', 'child': 'ワカメ'},
    {'name': 'フネ', 'child': 'サザエ'},
    {'name': 'フネ', 'child': 'カツオ'},
    {'name': 'フネ', 'child': 'ワカメ'},
    {'name': 'マスオ', 'child': 'タラオ'},
    {'name': 'サザエ', 'child': 'タラオ'},
])
graph = nx.from_pandas_edgelist(df, source='name', target='child', create_using=nx.DiGraph())

height = 400
html_file_name = 'graph.html'

network = Network(height=f"{height}px", directed=True)
network.from_nx(graph)
network.show_buttons()
network.save_graph(html_file_name)

with Path(html_file_name).open('r') as f:
    components.html(f.read(), height=height + 500, scrolling=True)