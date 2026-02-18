#%% 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bird_data = pd.read_csv("birds_arent_real_tweets.csv") # Placeholder

top_10_users = bird_data["user_name"].value_counts().head(10)

# Filter dataset based on the 10 most frequent users in the dataset
top_10_df = bird_data[bird_data["user_name"].isin(top_10_users.index)]

# Creates a new dataframe that displays total number of retweets for these 10 users
retweet_totals = (top_10_df
                  .groupby("user_name")["retweets"] # Groups the df together by username
                  .sum() # Sums the retweets together based upon the username
                  .reset_index() # resets index
)

# Adds another column to the dataframe that shows total number of tweets in the dataset
retweet_totals["tweet_count"] = retweet_totals["user_name"].map(top_10_users)

# Turns the retweet_totals df into a csv for visualisation in Tableau
retweet_totals.to_csv("bar_tweet_frequency.csv")
