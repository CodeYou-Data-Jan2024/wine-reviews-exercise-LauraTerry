import pandas as pd

reviews = pd.read_csv("data/winemag-data-130k-v2.csv/winemag-data-130k-v2.csv")
#read in csv file

mean_points = reviews.groupby('country')['points'].mean().apply(lambda point: round(point, 1))
#discover mean points per country, adjust all points to round to .1 decimal point

countries_reviewed = reviews.value_counts('country')
#discover counts of how many times a country was reviewed

new_df = [countries_reviewed, mean_points, ]
#combine dfs into one new dataframe variable 

results = pd.concat(new_df, axis = 1)
#concat df with same axis as a guide

results.to_csv("data/reviews-per-country.csv")
#export results to new CSV file in data folder