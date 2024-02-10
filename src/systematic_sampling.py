import numpy as np
import pandas as pd

"""
Imagine you have a dataset of responses from a survey conducted in a large company with 1,000 employees. 
You want to perform a systematic sampling to select a subset of these responses for detailed analysis.
We'll simulate this situation with numpy by creating a dataset of 1,000 survey responses, 
represented by random numbers (just for the sake of illustration), and then apply the systematic sampling function to select a sample.
"""

def systematic_sampling(df, step):
    if isinstance(df, np.ndarray):
        df = pd.Series(df)
    
    start = np.random.randint(0, step)
    selected_indices = np.arange(start, len(df), step)
    systematic_sample = df.iloc[selected_indices]
    return systematic_sample

# Example usage:
if __name__ == "__main__":
    # Simulate 1000 survey responses with random scores from 1 to 5
    np.random.seed(42)  # For reproducible results
    data = np.random.randint(1, 6, size=1000)  # Random integers between 1 and 5
    # Apply systematic sampling to our dataset
    sample = systematic_sampling(data, 10)
    # Calculate and print sample mean
    sample_mean = sample.mean()
    print(f"Sample Mean: {sample_mean}")

    # Compare with the population mean
    population_mean = np.mean(data)
    print(f"Population Mean: {population_mean}")