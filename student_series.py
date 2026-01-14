import pandas as pd

student_total={"s1":450,"s2":475,"s3":490,"s4":485}

series=pd.Series(student_total)

print(series["s4"])

print("total",series.sum())
print("max",series.max())
print("min",series.min())
print("average",series.mean())