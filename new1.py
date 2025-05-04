import pandas as pd
import numpy
import matplotlib as mlt
import datetime as dt
a=pd.read_csv('data.csv')
c=a[["Date"]]=pd.to_datetime(a[["Date"]])
b=a[["Company",c,"Open","Close/Last"]]
print(b)
# print(b)