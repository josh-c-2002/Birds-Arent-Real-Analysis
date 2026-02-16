#%%
import pandas as pd
import matplotlib.pyplot as plt

twitter_birds = pd.read_csv("C:\\Users\\joshu\Desktop\\DA Coursework\\birds_arent_real_tweets.csv")

# Takes the date of every post, strips them of their day
twitter_birds['date'] = pd.to_datetime(twitter_birds['date'])
twitter_birds['only dates'] = twitter_birds['date'].dt.date
twitter_birds["only dates"] = pd.to_datetime(twitter_birds["only dates"], format='%Y00%m').apply(lambda x: x.strftime('%Y-%m'))


# Makes a new df from twitter_birds["only dates"].value_counts(), then sorts that by 

df = twitter_birds['only dates'].value_counts().rename_axis('dates').reset_index(name='frequency')
df = df.sort_values(by=["dates"], axis=0, ascending=True)

print(df)
# Attempts to plot the activity on given days and compares them to time
twit_x = df["dates"]
twit_y = df["frequency"]

# We'll do the same for Google Trends data.
google_birds = pd.read_csv("C:\\Users\\joshu\Desktop\\DA Coursework\\gt_activity.csv")

# google_birds["Time"] = pd.to_datetime(google_birds["Time"], format="mixed").apply(lambda x: x.strftime('%Y-%m'))

gog_x = google_birds["Time"]
gog_y = google_birds["birds aren't real"]

# Takes all of the above and puts it in a line graph. Done to get a sense of 
plt.plot(gog_x, gog_y, color="green",label="google trends")
plt.plot(twit_x, twit_y, color="blue", label="twitter")
plt.title("Reddit Acitivty over Time versus Twitter")
plt.show()
# %%
