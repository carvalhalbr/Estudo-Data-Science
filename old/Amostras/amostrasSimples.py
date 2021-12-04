
import pandas as pd
import numpy as np

base = pd.read_csv('E:\DATA_SCIENCE\Python\src\iris.csv')

print(base)
print(base.shape)

np.random.seed(2345)
amostra =np.random.choice(a= [0, 1], size= 150, replace= True, p= [0.5, 0.5])

print(amostra)
print(len(amostra))
print(len(amostra[amostra==1]))
print(len(amostra[amostra==0]))
