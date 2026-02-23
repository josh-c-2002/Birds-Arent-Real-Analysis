#%%
import pandas as pd

birds_data = pd.read_csv("birds_arent_real_tweets.csv") # Placeholder

# Separates out the text in the dataset into individual things
birds_data2 = birds_data["text"].str.split(" ", n=-1, expand=True)

# Drops all null values from the dataset
split_birds = (pd.melt(birds_data2)).dropna()

# Counts all of the unique instances of a word and converts that value count to a CSV file
(split_birds["value"].value_counts()).to_csv("splitbirds.csv")

#%%
import pandas as pd
fresh_birds = pd.read_csv("splitbirds.csv") # Placeholder 

# Goes through the split birds dataset, removing useless words
word_list = [" ", "a", "the", "of", "with", "for", "The",
             "by", "with", "they", "I", "is", "to", "are", "all",
             "about", "have", "but", "not", "aren't", "This", "out", 
             "your", "know", "as", "from", "don't", "I'm", "on", "in",
             "that","up", "we", "so", "at", "has", "We", "me", "get",
             "They", "will", "-", "our", "A", "Aren't","Aren’t"
             "us", "see", "If", "do", "their", "them", "one",
             "if", "some", "how","&amp;", "Are", "It's", "because",
             "would", "when", "don't", "now", "more", "don’t",
             "really", "it.", "it's", "need", "those", "What", "there",
             "were", "these", "It's", "I’m", "here", "way", "his", "hers",
             "actually", "he", "she", "did", "theirs", "yes", "no", 
             "My", "Just", "@USCPSC", "should", "take", "\n#birdsarentreal", "Aren't",
             "It", "They?", "i", "So","You", "you", "you.", "this", "and", 
             "\n\n#birdsarentreal", "it", "my", "after", "be", "Be", "That", "Make",
             "make", "just", "was", "like", "or", "an", "can", "Aren’t","It’s", "New", 
             "And","who", "been", "why", "#birdsarentreal...", "via", "back",
             "still", "going", "into","got", "even", "am",
             "In", "also", "No", "always", "taking", "being",
             "does", "trying", "Oh", "Also", "dropped:", "#aiartwork",
             "own", "other",'"Birds', "can’t",",", "over", "up.",
             "Why", "Yeah,", "There", "then", "had", "Also,", "But", "Some",
             "How","I've", "@DroniesNFT", ]

# Saves a new version of the dataset, now cleaned.
bdf = ((fresh_birds[fresh_birds.value.isin(word_list) == False]).dropna()).head(200)

# Cheeky for loop applies a further layer of word filtering 
for word in bdf["value"]:
    if word == (bdf["value"].str.contains(str(STOPWORDS)).any()):
        word.drop(index=0, inplace=True)

# Saves the new dataframe bdf to csv
bdf.to_csv("filterbirb_final.csv")

# Final adjustments are made in Tableau, in case this initial round of cleaning still misses one or 
# two stray values. 
# %%
