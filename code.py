# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_data.csv")

movies = netflix_df[netflix_df["type"] == "Movie"]
sub1 = movies[(movies["release_year"] >= 1990)]
sub = sub1[(sub1["release_year"] < 2000)]
plt.hist(sub["duration"])
plt.title('Distribution of movie duration in 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of movies')
plt.show()

duration = 100
action = sub[sub["genre"] == "Action"]
short_movie_count = 0

for label, row in action.iterrows():
    if row["duration"] < 90:
        short_movie_count += 1

print(short_movie_count)
