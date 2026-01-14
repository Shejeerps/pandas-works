import pandas as pd

salary=[30000,35000,40000,45000,50000]

series=pd.Series(salary,index=["shejeer","lijo","abin","shafi","resin"])

print(series[0:4])
print(series["lijo":"shafi"])

