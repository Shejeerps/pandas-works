import pandas as pd

df=pd.read_csv("ipl-casestudy\ipl_data.csv")
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.head())
print(df.tail())
print(df.info())

df["match_id"].fillna(500,inplace=True)

df["season"].fillna(df["season"].mode()[0],inplace=True)

df["city"].fillna("kerala",inplace=True)

df["team1"].fillna("unknown",inplace=True)

df["team2"].fillna("unknown",inplace=True)

df["winning_team"].fillna("unknown",inplace=True)

df["player_of_match"].fillna("unknown",inplace=True)

df["venue"].fillna("jawaharlal nehru kochi",inplace=True)

df["runs_scored"].fillna(df["runs_scored"].mean(),inplace=True)

df["wickets"].fillna(df["wickets"].median(),inplace=True)

print(df.isnull().sum())

# matches per season

print("matches per season",df["season"].value_counts())

# top match count season

print("top match count season",df["season"].value_counts().idxmax())

# total match won by each team

print("total match won by each team",df["winning_team"].value_counts())

# average runs per season

print("average runs per season",df.groupby("season")["runs_scored"].mean())

# venue wise matchcount

print("venue wise match count",df["venue"].value_counts())

# venue wise average runs

print("venue wise average",df.groupby("venue")["runs_scored"].mean())

# city wise count

print("city wise count",df["city"].value_counts())

# city wise average runs

print("city wise average runs",df.groupby("city")["runs_scored"].mean())

# which winning team has highest AVERAGE run

print("average runs in winning team",df.groupby("winning_team")["runs_scored"].mean().idxmax())

# top 3 venue

print("top 3 venues",df["venue"].value_counts().head(3))