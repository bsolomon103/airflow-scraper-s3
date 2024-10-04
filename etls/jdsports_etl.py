import pandas as pd
from pandas import DataFrame
import os
import time

def use_pandas(file) -> DataFrame:
    df = pd.read_csv(file)
    df['price'] = df['price'].apply(lambda x : float(x[1:]))
    return df
    
    
    
    
    
    