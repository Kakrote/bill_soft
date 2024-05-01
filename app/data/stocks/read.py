import os
import csv
import pandas as pd


itemspath=os.path.join(os.getcwd(),'app','data','stocks','items.csv')
f=pd.read_csv(itemspath)

