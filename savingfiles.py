import numpy as np 
import pandas as pd 

data = np.array([1,2,3,4,5])

df = pd.DataFrame(data)

df.to_csv('data.csv', index=False, header=False)

