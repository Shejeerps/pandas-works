import pandas as pd

student={
    "name":["lijo","shafi","shejeer","abin"],
    "age":[22,24,24,27],
    "course":["ds","ds","dj","ms"]
}

dataframe=pd.DataFrame(student)
print(dataframe)

print(dataframe[0:1])

print(dataframe[["name","age"]])