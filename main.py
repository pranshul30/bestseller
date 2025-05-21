import pandas as pd

df=pd.read_csv('bestsellers.csv')

print(df.head())

print(df.shape)

print(df.columns)

print(df.describe)


df.drop_duplicates(inplace=True)

df.rename(columns={"Name":"Title","Year":"Publication Year","User Rating":"Rating"},inplace=True)

df["Price"]=df["Price"].astype(float)

author_counts=df["Author"].value_counts()
print(author_counts)

avg_rating=df.groupby("Genre")["Rating"].mean()
print (avg_rating)

author_counts.head(10).to_csv("top_authors.csv")

avg_rating.to_csv("avg_rating_by_genre.csv")

