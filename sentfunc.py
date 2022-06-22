from textblob import TextBlob
# Create a function to get the subjectivity 
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

# Create function to get polarity (tells you how positive or negative the text is)
def getPolarity(text):
    return TextBlob(text).sentiment.polarity 

# Create a function to compute the negative, neutral, and positive analysis 
def getAnalysis(score):
    if score < 0: 
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else: 
        return 'Positive'