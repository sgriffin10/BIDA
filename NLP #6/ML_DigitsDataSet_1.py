# # Make sure to install the scikit-learn package first
# from sklearn.datasets import load_digits
#
# # Digits is a "Bunch" object that is a special type of object in scikit-learn
# digits = load_digits()
# # Verify that this is a Bunch Object
# print(type(digits))
# # Bunch has target and data attributes.
# print(digits.target)
# print(digits.target_names)
# print(digits.data)
# print(digits.data.shape)
#
# # Show the images that we need to recognize
# # Browsing, exploring the data
# import matplotlib.pyplot as plt
# figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))
# for item in zip(axes.ravel(), digits.images, digits.target):
#     axes, image, target = item
#     axes.imshow(image, cmap=plt.cm.gray_r)
#     axes.set_xticks([])
#     axes.set_yticks([])
#     axes.set_title(target)
# plt.tight_layout()
# plt.show()
#
#
# # Split the data into training and testing data sets randomly.  By default 25% of the data is test.
# # Convention...X--> samples split into training and test sets, y --> target split into training and test sets
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=1)
# print(X_train.shape)
#
# # Train the classifier - kNN in this case
# from sklearn.neighbors import KNeighborsClassifier
#
# model = KNeighborsClassifier(n_neighbors=100)
# model.fit(X=X_train, y=y_train)
#
# # Lets predict on the TEST data set and see how close the predictions are
# predicted = model.predict(X=X_test)
# actual = y_test
#
# # Check the first 20 samples to visually see prediction accuracy
# print(predicted[:20])
# print(actual[:20])
#
# # Isolate the wrong predictions
# wrong = [(p,e) for (p,e) in zip(predicted, actual) if p != e]
# print(wrong)
#
# #Scikit-learn provides these x`
# #Accuracy
# print(model.score(X_test, y_test))
# #confusion matrix - each cell represents the frequency of a class
# # rows --> actual classes
# # columns --> predicted classes
# from sklearn.metrics import confusion_matrix
# confusion = confusion_matrix(y_true=actual, y_pred = predicted)
# print(confusion)
# from sklearn.metrics import classification_report
# names = [str(digit) for digit in digits.target_names]
# print(classification_report(actual, predicted, target_names = names))
#
