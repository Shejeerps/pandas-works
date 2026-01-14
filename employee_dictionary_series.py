import pandas as pd
 
employees={"shafi":"IT","lijo":"finance","abin":"marketing","shejeer":"accounting"}
series=pd.Series(employees)
print(series["shafi"])