import re

# Clean the text 

# Create function to clean the tweets 
def cleanTxt(text):

    # get rid of @ mentions --> works similar to grepl from R
    text = re.sub(r'@[A-Za-z0-9]+', '', text)

    # remove hashtags
    text = re.sub(r'#', '', text)
    
    # remove retweets
    text = re.sub(r'RT[\s]+','', text)

    # remove urls/hyperlinks
    text = re.sub(r'https?:\/\/\S+','',text)

    return text

