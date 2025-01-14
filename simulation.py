import networkx as nx
import plotly.graph_objects as go
from typing import Dict, List
import random
from datetime import datetime
import json
from agents import (
    CreativeThinker, DataAnalyst, RiskAssessor,
    Mediator, Strategist, Facilitator, Innovator
)

class Subgroup:
    def __init__(self, id: int, participants: List[str]):
        self.id = id
        self.participants = participants
        self.ideas = []
        self.active_discussions = []

class CSISimulation:
    def __init__(self):
        self.agents = {
            'creative': CreativeThinker(),
            'analyst': DataAnalyst(),
            'risk': RiskAssessor(),
            'mediator': Mediator(),
            'strategist': Strategist(),
            'facilitator': Facilitator(),
            'innovator': Innovator()
        }
        self.subgroups = []
        self.network = nx.Graph()
        self.metrics = {
            'active_participants': 0,
            'total_ideas': 0,
            'engagement_score': 0,
            'consensus_level': 0
        }

    def start_new_session(self, topic: str, num_participants: int):
        self.topic = topic
        self.num_participants = num_participants
        self.initialize_subgroups()
        self.initialize_network()
        self.update_metrics()

    def initialize_subgroups(self):
        participants = [f"Participant_{i}" for i in range(self.num_participants)]
        num_subgroups = self.num_participants // 5  # 5 participants per subgroup
        
        self.subgroups = []
        for i in range(num_subgroups):
            start_idx = i * 5
            end_idx = start_idx + 5
            subgroup_participants = participants[start_idx:end_idx]
            self.subgroups.append(Subgroup(i, subgroup_participants))

    def initialize_network(self):
        self.network.clear()
        
        # Add nodes for subgroups
        for subgroup in self.subgroups:
            self.network.add_node(f"Subgroup_{subgroup.id}", 
                                type='subgroup',
                                size=len(subgroup.participants))

        # Add nodes for agents
        for agent_type, agent in self.agents.items():
            self.network.add_node(agent_type, type='agent', size=10)

        # Create connections
        for subgroup in self.subgroups:
            # Connect each subgroup to 2-3 random agents
            connected_agents = random.sample(list(self.agents.keys()), 
                                          random.randint(2, 3))
            for agent in connected_agents:
                self.network.add_edge(f"Subgroup_{subgroup.id}", agent)

    def get_network_visualization(self):
        pos = nx.spring_layout(self.network, k=1, iterations=50)
        
        edge_trace = go.Scatter(
            x=[], y=[],
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')

        for edge in self.network.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_trace['x'] += (x0, x1, None)
            edge_trace['y'] += (y0, y1, None)

        node_trace = go.Scatter(
            x=[], y=[],
            text=[],
            mode='markers+text',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='YlGnBu',
                size=[],
                color=[],
                line_width=2))

        for node in self.network.nodes():
            x, y = pos[node]
            node_trace['x'] += (x,)
            node_trace['y'] += (y,)
            node_trace['text'] += (node,)
            
            if self.network.nodes[node]['type'] == 'subgroup':
                size = 30
                color = 0
            else:
                size = 20
                color = 1
                
            node_trace['marker']['size'] += (size,)
            node_trace['marker']['color'] += (color,)

        fig = go.Figure(data=[edge_trace, node_trace],
                       layout=go.Layout(
                           showlegend=False,
                           hovermode='closest',
                           margin=dict(b=0, l=0, r=0, t=0),
                           xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                           yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                       )
        
        return fig

    def update_metrics(self):
        # Simulate metrics updates
        self.metrics.update({
            'active_participants': self.num_participants,
            'total_ideas': random.randint(20, 100),
            'engagement_score': random.randint(70, 95),
            'consensus_level': random.randint(60, 90)
        })

    def get_current_metrics(self) -> Dict:
        return self.metrics
