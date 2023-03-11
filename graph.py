import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config, ConfigBuilder

st.write("# 磯野家")

nodes = []
edges = []
nodes.append(Node(id='namihei', label='波平'))
nodes.append(Node(id='fune', label='フネ'))
nodes.append(Node(id='sazae', label='サザエ'))
nodes.append(Node(id='katsuo', label='カツオ'))
nodes.append(Node(id='wakame', label='ワカメ'))
nodes.append(Node(id='masuo', label='マスオ'))
nodes.append(Node(id='tarao', label='タラオ'))

edges.append(Edge(source='namihei', target='sazae'))
edges.append(Edge(source='fune', target='sazae'))
edges.append(Edge(source='namihei', target='katsuo'))
edges.append(Edge(source='fune', target='katsuo'))
edges.append(Edge(source='namihei', target='wakame'))
edges.append(Edge(source='fune', target='wakame'))
edges.append(Edge(source='masuo', target='tarao'))
edges.append(Edge(source='sazae', target='tarao'))

config_builder = ConfigBuilder()
config = config_builder.build()

agraph(nodes=nodes, edges=edges, config=config)