import streamlit as st
import networkx as nx
import plotly.graph_objects as go
from datetime import datetime
import json
import pandas as pd
from agents import (
    CreativeThinker, DataAnalyst, RiskAssessor,
    Mediator, Strategist, Facilitator, Innovator
)
from simulation import CSISimulation
from utils import load_env_vars

# Load environment variables
load_env_vars()

class CSIApp:
    def __init__(self):
        self.setup_page()
        self.initialize_session_state()
        self.simulation = CSISimulation()

    def setup_page(self):
        st.set_page_config(
            page_title="CSI Platform Simulation",
            page_icon="🧠",
            layout="wide"
        )
        st.title("Conversational Swarm Intelligence Platform")

    def initialize_session_state(self):
        if 'current_session' not in st.session_state:
            st.session_state.current_session = None
        if 'simulation_running' not in st.session_state:
            st.session_state.simulation_running = False

    def render_sidebar(self):
        with st.sidebar:
            st.header("Simulation Controls")
            topic = st.text_input("Brainstorming Topic", "How can we make cities more sustainable?")
            num_participants = st.slider("Number of Participants", 15, 150, 75, step=15)
            if st.button("Start New Session"):
                self.simulation.start_new_session(topic, num_participants)
                st.session_state.simulation_running = True

    def render_main_dashboard(self):
        if not st.session_state.simulation_running:
            st.info("Start a new session using the sidebar controls.")
            return

        col1, col2 = st.columns([2, 1])
        
        with col1:
            self.render_subgroup_visualization()
        
        with col2:
            self.render_metrics()

    def render_subgroup_visualization(self):
        st.subheader("Subgroup Dynamics")
        # Create network graph visualization using plotly
        network_fig = self.simulation.get_network_visualization()
        st.plotly_chart(network_fig, use_container_width=True)

    def render_metrics(self):
        st.subheader("Session Metrics")
        metrics = self.simulation.get_current_metrics()
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Active Participants", metrics['active_participants'])
            st.metric("Total Ideas", metrics['total_ideas'])
        with col2:
            st.metric("Engagement Score", f"{metrics['engagement_score']}%")
            st.metric("Consensus Level", f"{metrics['consensus_level']}%")

    def run(self):
        self.render_sidebar()
        self.render_main_dashboard()

if __name__ == "__main__":
    app = CSIApp()
    app.run()
