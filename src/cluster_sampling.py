import numpy as np
import pandas as pd
import random

"""
Let's assume we have a dataset representing responses from individuals spread across various regions. 
Our goal is to perform clustered sampling to analyze responses from a subset of these regions.
"""

def get_clustered_sample(df, n_per_cluster, num_select_clusters):
    # Ensure df is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")

    # Calculate the total number of clusters
    total_clusters = len(df) // n_per_cluster

    # Sample n_per_cluster items from each cluster
    sampled_data = pd.DataFrame()
    for cluster_id in range(total_clusters):
        # Sample n_per_cluster items for the current cluster
        sampled_cluster = df.sample(n_per_cluster)
        # Assign cluster ID to the sampled data
        sampled_cluster["cluster"] = cluster_id
        # Append the sampled cluster to the result
        sampled_data = pd.concat([sampled_data, sampled_cluster], ignore_index=True)
        # Drop sampled items from the original DataFrame
        df = df.drop(sampled_cluster.index)

    # Select random clusters from the sampled data
    random_selected_clusters = random.sample(range(total_clusters), num_select_clusters)
    # Filter the sampled data for selected clusters
    final_sample = sampled_data[sampled_data["cluster"].isin(random_selected_clusters)]

    return final_sample

np.random.seed(42) 
data = {
    'response': np.random.randint(1, 6, 1000), 
    'region': np.random.randint(1, 21, 1000)
}
df = pd.DataFrame(data)
n_per_cluster = 50
num_select_clusters = 3

sampled_df = get_clustered_sample(df, n_per_cluster, num_select_clusters)

print(sampled_df)