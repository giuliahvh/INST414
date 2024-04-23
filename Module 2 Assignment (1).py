#!/usr/bin/env python
# coding: utf-8

# In[24]:


import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# In[27]:


client_id = 'dbdbbe596bcc4986baff23591208c5d3'
client_secret = '6461245bf7524960b030e5d8e2228df7'


# In[40]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import networkx as nx

client_id = 'dbdbbe596bcc4986baff23591208c5d3'
client_secret = '6461245bf7524960b030e5d8e2228df7'

# Setting up Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Fetch artists and their top tracks
def fetch_artists_tracks(genre='pop', limit=50):
    artist_tracks = {}
    results = sp.search(q='genre:' + genre, type='artist', limit=limit)
    for item in results['artists']['items']:
        artist_id = item['id']
        artist_name = item['name']
        top_tracks = sp.artist_top_tracks(artist_id)
        for track in top_tracks['tracks']:
            for artist in track['artists']:
                if artist['name'] != artist_name:  # ensure no self-loops
                    if artist_name not in artist_tracks:
                        artist_tracks[artist_name] = set()
                    artist_tracks[artist_name].add(artist['name'])
    return artist_tracks

# Create and build the graph
def build_graph(artist_tracks):
    G = nx.Graph()
    for artist, collaborators in artist_tracks.items():
        for collaborator in collaborators:
            if G.has_edge(artist, collaborator):
                G[artist][collaborator]['weight'] += 1
            else:
                G.add_edge(artist, collaborator, weight=1)
    return G

# Count collaborations
def count_collaborations(G):
    collaboration_counts = {}
    for artist in G.nodes():
        collaboration_counts[artist] = sum(data['weight'] for _, data in G[artist].items())
    return collaboration_counts

# Main function and export Gephi File
def main():
    artist_tracks = fetch_artists_tracks()
    G = build_graph(artist_tracks)
    
    # Export the graph to a GraphML file within the main function
    nx.write_graphml(G, 'spotify_network.graphml')
    
    # Count collaborations for each artist
    collaboration_counts = count_collaborations(G)
    
    # Sort collaboration counts dictionary by value (number of collaborations)
    sorted_collaborations = sorted(collaboration_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Print top 10 influential artists
    print("Top 10 Influential Artists:")
    for artist, count in sorted_collaborations[:10]:
        print(f"{artist}:")
        print(f"  Number of Collaborations: {count}")
        print(f"  Degree Centrality: {nx.degree_centrality(G)[artist]}")
        print()

if __name__ == "__main__":
    main()

