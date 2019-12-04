#Import - make sure you install the textblob package!
import nltk
from textblob import TextBlob
# import Path - part of standard Python
from pathlib import Path

blob = TextBlob(Path("NLP #4/textblob1.txt").read_text())

# #Sentiment - Polarity -1.0 (negative) to +1.0 (positive) 0.0 (neutral)
# #Sentiment - subjectivity - 0 (objective) to 1.0 (subjective)
# # subjective sentence expresses some personal feelings, views, beliefs,
# # opinions, allegations, desires, beliefs, suspicions, and speculations where as Objective sentences are factual.
# # https://medium.com/@rahulvaish/textblob-and-sentiment-analysis-python-a687e9fabe96
print(blob.sentiment)

sentences = blob.sentences
print(len(sentences))
for sent in sentences:
    print(sent.sentiment)
    print("")


