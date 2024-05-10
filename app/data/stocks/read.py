import os
import csv
import pandas as pd


lis=list()

itemspath=os.path.join(os.getcwd(),'app','data','stocks','items.csv')
f=pd.read_csv(itemspath)
row=f.shape[0]
column=f.shape[1]
# print(f)
# print(f.head())
print(f.iloc[0].id)