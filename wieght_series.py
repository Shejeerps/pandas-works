import pandas as pd

wieght=[60,65,70,75,80,85,90,95,100,105]

series=pd.Series(wieght)
print(series)

print(series.head())
print(series.tail())
print(series.shape)