import requests
from io import StringIO
import pandas as pd
import csv


###################################################
'''NOTE: must edit path every time you change directory '''
def mergeData(tweetcsv, name, url_hist):
    '''
    Given a csv containing twitter tweets, and a url to the csv from yahoo finance, 
    return the path to a csv with twitter tweets and corresponding stock prices.
    Assumes tweets are given in the same time period and chronological order as the 
    stock prices, from oldest to newest

    name = name of the company data, must createa directory with this same name 
    ur_hist = url to the csv file that can be downloaded from yahoo finance (make sure
    you specify the dates of the stock)
    tweetcsv = path to csv of tweet text
    '''
    x = input("Name of csv file: ")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'}
    
    response = requests.get(url_hist, headers=headers)
    file = StringIO(response.text)
    reader = csv.reader(file)
    data = list(reader)

    date = []
    close_stock = []
    for row in data:
        date.append(row[0]), close_stock.append(row[4])

    date.pop(0)
    close_stock.pop(0)

    data = pd.read_csv(tweetcsv)    
    tweets = []
    for row in data['d$text'][:len(date)]:
        tweets.append(row)

    dict = {'Date': date, 'text': tweets, 'Stock': close_stock}
    path = "/Users/joshuagrajales/Desktop/qac211/project/SM_comm/"+str(name)+"/"+str(x)
    pd.DataFrame(dict).to_csv(path)
    
    print("File stored: "+path)
    return path

            
