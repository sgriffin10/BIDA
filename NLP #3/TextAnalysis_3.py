#Import - make sure you install the textblob package!
import nltk
from textblob import TextBlob
# import Path - part of standard Python
from pathlib import Path
blob = TextBlob(Path("NLP #3/textblob1.txt").read_text())
#If you need stopwords, download this
#nltk.download("stopwords")

# Delete stop words
from nltk.corpus import stopwords
stops = stopwords.words("english")
listOfWords = []
for word in blob.words:
    if word not in stops:
        listOfWords.append(word)

# print(listOfWords)
# Create a string from the list
concatenatedWords = ' '.join(listOfWords)
# Because TextBlob can deal with Strings
blob2 = TextBlob(concatenatedWords);
#Dictionary / tuple of words and their counts
items = blob2.word_counts.items()
# print(items)
#how many words do we have?
print(len(blob2.words))

# Sorting in descending order
from operator import itemgetter
sortedItems = sorted(items, key=itemgetter(1), reverse=True)
# print(sortedItems)
# Just getting only 20 items
# sortedItems = sortedItems[:21]
# print(sortedItems)

#Create a dataframe for the word count
import pandas as pd
df = pd.DataFrame(sortedItems, columns=['word', 'count']);
# print(df)

# # Visualization - BAR GRAPH
axes = df.plot.bar(x='word', y='count', legend=False)
import matplotlib.pyplot as plt

# plt.show()

# # Visualization - WORD CLOUD

import imageio
from wordcloud import WordCloud

wordcloud = WordCloud(colormap='prism', background_color='white')
wordcloud = wordcloud.generate(concatenatedWords)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
