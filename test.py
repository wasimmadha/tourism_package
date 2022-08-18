import numpy as np
import pandas as pd

np.random.seed(20)
df= pd.DataFrame(np.random.randn(10,4), index=pd.date_range("2021-07-18", periods=10), columns=["a","b","c","d"])

df['date_new'] = pd.date_range("2021-07-18", periods=10)
df['date_new']= df['date_new'].apply(pd.to_datetime)

df['date_new'] = pd.to_datetime(df['date_new'], errors='coerce')


print(df.info())