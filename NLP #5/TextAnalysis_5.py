from textblob.sentiments import  NaiveBayesAnalyzer
from textblob import TextBlob

# import Path - part of standard Python
from pathlib import Path

blob = TextBlob(Path("NLP #5/textblob1.txt").read_text())

newblob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
print(newblob.sentiment)

