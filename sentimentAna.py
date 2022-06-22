# import libraries
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression 
import re
import matplotlib.pyplot as plt
from cleanTxt import cleanTxt
from sentfunc import getAnalysis,getPolarity,getSubjectivity

def sentA(csvs):
    '''
    csvs: Given paths to the csv files containing twitter text, perform a sentiment anlaysis.
    Outputs bar plot containing number of positive, neutral, and negative tweets, scatter plot of subjectivity
    vs polarity, and a word cloud

    the csv files I used contain the tweets I scraped from twitter using rtweet search_tweets function 
    '''
    x = input("Enter name of company: ")
    i = 0 
    j = 0 
    med_pol = []
    fig, axs = plt.subplots(3, 3, figsize = (18,16))

    # first while loop where we do all of the analysis 
    while i <= 2:
    
        # load files
        df = pd.read_csv(csvs[i])
        
        # clean the text 
        df['Tweets'] = df['d$text'].apply(cleanTxt)

        # create two new columns (one for subjectivity and polarity)
        df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
        df['Polarity'] = df['Tweets'].apply(getPolarity)

        # assign Positive, Neutral, or Negative to each tweet
        df['Analysis'] = df['Polarity'].apply(getAnalysis)

        # second while loop where we begin plotting 
        while j <= 2:
            
            # Plot a Word Cloud
            allWords = ' '.join( [twts for twts in df['Tweets']] )
            wordCloud = WordCloud(width = 500, height = 300, random_state = 21, max_font_size = 120).generate(allWords)

            axs[i,j].imshow(wordCloud, interpolation = "bilinear")
            axs[i,j].axis('off')

            j = j + 1
            plt.figure(figsize=(8,6)) 
            for k in range(0, df.shape[0]):
                axs[i,j].scatter(df['Polarity'][k], df['Subjectivity'][k], color = 'blue')
            axs[i,j].grid()

            axs[i,j].set_title("Sentiment Analysis")
            axs[i,j].set_xlabel("Polarity")
            axs[i,j].set_ylabel("Subjectivity")
            
            j = j + 1
            # plot and visualize the counts 
            axs[i,j].set_ylabel("Counts")
            df['Analysis'].value_counts().plot(kind='bar', ax=axs[i,j])
            j = j + 1

        j = 0 
        i = i + 1
    fig.suptitle(x, fontsize = 25)

