import pandas as pd
from mergestock_tweet import mergeData
from cleanTxt import cleanTxt
from sentfunc import getAnalysis,getPolarity,getSubjectivity
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np 

def regress(csvs,name,urls):
    '''
    csvs: list of paths to 3 csvs with the tweet data as extracted from 
    twitter api
    name: name of company as defined in directory 
    urls: 3 urls from yahoo finance csvs 
    Given the above arguments, regress performs a linear regression using statsmodel library;
    performs linear regression on stock price and sentiment score on a given day for a given company --
    displays auxilary statistical metrics and master dataframe
    '''
    i = 0 
    first = pd.read_csv(mergeData(csvs[i],name,urls[i]))
    stock1 = list(first['Stock'])
    text1 = list(first['text'])
    date1 = list(first['Date'])

    i = i + 1
    sec = pd.read_csv(mergeData(csvs[i],name,urls[i]))
    stock2 = list(sec['Stock'])
    text2 = list(sec['text'])
    date2 = list(sec['Date'])

    i = i + 1
    thi = pd.read_csv(mergeData(csvs[i],name,urls[i]))
    stock3 = list(thi['Stock'])
    text3 = list(thi['text'])
    date3 = list(thi['Date'])

    all_stock = stock1+stock2+stock3
    all_text = text1+text2+text3
    all_time = date1+date2+date3

    dict = {'d$text': all_text, 'All Stock': all_stock, 'Date': all_time}
    df = pd.DataFrame(dict)
    df['Tweets'] = df['d$text'].apply(cleanTxt)

    # create two new columns (one for subjectivity and polarity)
    df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
    df['Polarity'] = df['Tweets'].apply(getPolarity)

    # assign Positive, Neutral, or Negative to each tweet
    df['Analysis'] = df['Polarity'].apply(getAnalysis)

    df.head()
    
    mod = sm.OLS(df['All Stock'],sm.add_constant(df['Polarity']), hasconst=True)
    fii = mod.fit()
    p_values =fii.summary2(())

    plt.scatter(df['Polarity'],df['All Stock'])
    plt.title(name)
    plt.grid()
    plt.xlabel("Sentiment Score")
    plt.ylabel("Stock Price")
    x = np.linspace(-1,1,100)
    plt.plot(x,float(fii.params[1])*x+float(fii.params[0]), color = 'black', label = 'Slope: ' + str(int(fii.params[1]))+' Intercept: ' + str(int(fii.params[0])))
    plt.legend()

    print(p_values)

    return df

