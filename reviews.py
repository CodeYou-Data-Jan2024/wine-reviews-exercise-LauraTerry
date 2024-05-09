import pandas as pd

#read in csv file
reviews = pd.read_csv("data/winemag-data-130k-v2.csv/winemag-data-130k-v2.csv")

#discover mean points per country, adjust all points to round to .1 decimal point
mean_points = reviews.groupby('country')['points'].mean().apply(lambda point: round(point, 1))

#discover counts of how many times a country was reviewed
countries_reviewed = reviews.value_counts('country')

#combine dfs into one new dataframe variable 
new_df = [countries_reviewed, mean_points]

#concat df with same axis as a guide
results = pd.concat(new_df, axis = 1)

#export results to new CSV file in data folder
results.to_csv("data/reviews-per-country.csv")


print(results)