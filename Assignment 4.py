#!/usr/bin/env python
# coding: utf-8

# In[5]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# In[6]:


# Spotify API credentials
client_id = 'dbdbbe596bcc4986baff23591208c5d3'
client_secret = '6461245bf7524960b030e5d8e2228df7'
redirect_uri = 'http://localhost:8889/callback/'
scope = 'user-top-read'


# In[4]:


# Set up Spotipy client with increased timeout
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret, requests_timeout=20)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to search for tracks based on a query
def search_tracks(query, limit=50):
    tracks = sp.search(q=query, limit=limit, type='track')['tracks']['items']
    track_ids = [track['id'] for track in tracks]
    return track_ids

# Example search query (e.g., genre, artist, mood)
search_query = 'genre:"rock"'

# Collect track IDs based on the search query
track_ids = search_tracks(search_query)

# Function to collect audio features for a list of tracks
def get_audio_features(track_ids):
    audio_features = [sp.audio_features(track_id) for track_id in track_ids]
    return [track for track_list in audio_features for track in track_list if track]

# Collect audio features for the retrieved tracks
audio_features = get_audio_features(track_ids)

# Create DataFrame from collected features
df = pd.DataFrame(audio_features)

# Select relevant features for clustering
selected_features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
X = df[selected_features]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Choose optimal k value (number of clusters)
# Example: Using the elbow method
distortions = []
K = range(1, 10)
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(X_scaled)
    distortions.append(kmeanModel.inertia_)

# Plotting the elbow curve
plt.figure(figsize=(10, 6))
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

# Selecting k based on elbow curve or other criteria
k = 3

# Perform K-means clustering
kmeans = KMeans(n_clusters=k)
kmeans.fit(X_scaled)
df['cluster'] = kmeans.labels_

# Display cluster centroids (representative feature values)
centroids = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=selected_features)
print("Cluster Centroids:")
print(centroids)

# Analyze clusters
cluster_counts = df['cluster'].value_counts()
print("\nCluster Counts:")
print(cluster_counts)

# Visualize clusters (example: scatter plot of two features)
plt.figure(figsize=(10, 6))
plt.scatter(df['danceability'], df['energy'], c=df['cluster'], cmap='viridis')
plt.xlabel('Danceability')
plt.ylabel('Energy')
plt.title('Cluster Analysis of Musical Preferences')
plt.colorbar(label='Cluster')
plt.show()


# In[ ]:




