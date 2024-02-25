import pandas as pd
import numpy as np

def stratified_sample_df(df, stratify_colname, n_samples):
    """
    Generates a stratified sample from a DataFrame.
    """
    # Combine the stratification columns if there are more than one
    if isinstance(stratify_colname, list):
        df['_stratify_comb'] = df[stratify_colname].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
        stratify_colname = '_stratify_comb'
    
    # Proceed with stratification
    n_by_group = df.groupby(stratify_colname, group_keys=False).apply(lambda x: int(np.rint(n_samples * len(x) / len(df)))).to_dict()
    n_by_group = {k: min(v, df[df[stratify_colname] == k].shape[0]) for k, v in n_by_group.items()}
    
    stratified_sample = pd.concat(
        [df_group.sample(n=n_by_group[group_name], replace=False) for group_name, df_group in df.groupby(stratify_colname)]
    ).reset_index(drop=True)
    
    # Clean up if temporary stratification column was created
    if '_stratify_comb' in df:
        df.drop('_stratify_comb', axis=1, inplace=True)
    
    return stratified_sample

# Example usage
if __name__ == "__main__":
    np.random.seed(0)

    # Mock dataset generation
    data = {
        'Product': np.random.choice(['Product A', 'Product B', 'Product C'], size=1000),
        'Feedback': np.random.choice(['Positive', 'Neutral', 'Negative'], size=1000, p=[0.5, 0.3, 0.2]),
        'Detail': np.random.rand(1000)
    }

    df = pd.DataFrame(data)
    # Create a stratified sample
    stratified_colnames = ['Product', 'Feedback']  # Columns to stratify by
    sample_size = 150  # Sample size
    stratified_sample = stratified_sample_df(df, stratified_colnames, sample_size)

    print(f"Sample size: {len(stratified_sample)}")
    print(stratified_sample)