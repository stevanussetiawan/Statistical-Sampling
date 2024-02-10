import numpy as np
import pandas as pd
import random

"""
Let's say you want to draw a sample of 500 observations from the population_df without replacement, 
and then another sample of 500 observations with replacement. Here's how you could do it:
"""

# Population parameters
N = 10000
mu = 10
std = 2
# Creating the population
population_df = np.random.normal(mu, std, N)

# Function for random sampling
def random_sampling(df, n, resampling=False):
    random_sample = np.random.choice(df, replace=resampling, size=n)
    return random_sample

# Sampling without replacement
sample_without_replacement = random_sampling(population_df, 500, resampling=False)
print("Sample without replacement mean:", np.mean(sample_without_replacement))

# Sampling with replacement
sample_with_replacement = random_sampling(population_df, 500, resampling=True)
print("Sample with replacement mean:", np.mean(sample_with_replacement))