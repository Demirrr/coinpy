import coinpy as cp
import numpy as np
import pandas as pd

dfs = cp.DataFramesHolder(path='../Data')
dfs.drop_data_frames(key=lambda x: len(x) == 0)
dfs.preprocess({'func': 'mean', 'input': ['open', 'close'], 'output': 'price'})
dfs.select_col(['price'])
dfs.dropna()
dfs.merge_frames(['ETH', 'BTC', 'ADA', 'ETH', 'XLM', 'UNI'], how='inner')
dfs.select_interval(start="2021-03-25", end="2021-04-20")
dfs.normalize()
dfs.plot()
