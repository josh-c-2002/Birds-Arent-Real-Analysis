#%% <- This formulation is a holdover from using the VSCode Jupyter Notebook extension
import pandas as pd
import matplotlib.pyplot as plt

twitter_birds = pd.read_csv("birds_arent_real_tweets.csv") # Placeholder

# Takes the date of every post, strips them of their day
twitter_birds['date'] = pd.to_datetime(twitter_birds['date'])
twitter_birds['only dates'] = twitter_birds['date'].dt.date
twitter_birds["only dates"] = pd.to_datetime(twitter_birds["only dates"], format='%Y00%m').apply(lambda x: x.strftime('%Y-%m'))

# Makes a new df from twitter_birds["only dates"].value_counts(), then sorts that by dates. 

df = twitter_birds['only dates'].value_counts().rename_axis('dates').reset_index(name='frequency')
df = df.sort_values(by=["dates"], axis=0, ascending=True)

# Attempts to plot the activity on given days and compares them to time
twit_x = df["dates"]
twit_y = df["frequency"]

# We'll do the same for Google Trends data.
google_birds = pd.read_csv("gt_activity.csv") # Placeholder

google_birds["Time"] = pd.to_datetime(google_birds["Time"], format="mixed").apply(lambda x: x.strftime('%Y-%m'))

gog_x = google_birds["Time"]
gog_y = google_birds["birds aren't real"]

# Takes all of the above and puts it in a line graph. Done to get a sense of 
plt.plot(gog_x, gog_y, color="green",label="google trends")
plt.plot(twit_x, twit_y, color="blue", label="twitter")
plt.title("Reddit Acitivty over Time versus Twitter")
plt.show()

# Takes both dataframes used in the above line chart and turns them into csv files. 
# The csv files will then be used as data sources for Tableau visualisation. 
df.to_csv("twitter_timeseriesFinal.csv")
google_birds.to_csv("google_timeseriesFinal.csv")

#%% <- This formulation is a holdover from using the VSCode Jupyter Notebook extension
import pandas as pd
import random as rnd
twt_ts = pd.read_csv("twitter_timeseriesFinal.csv")

# Force conversion to datetime (assign it back!)
twt_ts["dates"] = pd.to_datetime(twt_ts["dates"], format="%Y-%m", errors="coerce")

# Set index
twt_ts = twt_ts.set_index("dates")

# Build full monthly range
full_range = pd.date_range(
    start="2018-01-01",
    end=twt_ts.index.max(),
    freq="MS"
)
# reindexes the range into the datafram
twt_ts = twt_ts.reindex(full_range)

# Fills the empty cells in the 'frequency' column
twt_ts["frequency"] = twt_ts["frequency"].fillna(0)

# Resets index again
twt_ts = twt_ts.reset_index().rename(columns={"index": "dates"})

# Drops the unnamed column created during this process
twt_ts.drop(twt_ts.columns[twt_ts.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

twt_ts.to_csv("twitter_timeseriesFinalV3.csv")
# %%
