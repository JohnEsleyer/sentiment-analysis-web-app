import nltk

text = "This is a very nice day"
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
score = ((sid.polarity_scores(str(text))))['compound']

if (score > 0):
    label = 'This sentence is positive'
elif (score == 0):
    label = 'This sentence is neutral'
else:
    label = 'This sentence is negative'