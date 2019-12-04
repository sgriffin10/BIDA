# #Import - make sure you install the textblob package!
# import nltk
# from textblob import TextBlob
# #nltk.download("stopwords")
# # Simple text
# text = "today is a beautiful day.  tomorrow looks like bad weather, uh oh"
# #Create a text blob
# blob = TextBlob(text)
# # Delete stop words
# from nltk.corpus import stopwords
# stops = stopwords.words("english")
# # print(stops)
# for word in blob.words:
#     if word not in stops:
#         print(word)
# # n-grams
# print(blob.ngrams())