import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# define the paths to the training data folders
normal_folder = 'normaldmgs_train'
virus_folder = 'virusdmgs_train'

# define the vectorizer and classifier
vectorizer = CountVectorizer()
classifier = MultinomialNB()

# define the training data and labels
training_data = []
labels = []

# iterate through the normal folder and add the data to the training set
for filename in os.listdir(normal_folder):
    filepath = os.path.join(normal_folder, filename)
    with open(filepath, 'r') as f:
        data = f.read()
        training_data.append(data)
        labels.append(0)

# iterate through the virus folder and add the data to the training set
for filename in os.listdir(virus_folder):
    filepath = os.path.join(virus_folder, filename)
    with open(filepath, 'r') as f:
        data = f.read()
        training_data.append(data)
        labels.append(1)

# transform the training data into feature vectors
features = vectorizer.fit_transform(training_data)

# train the classifier on the feature vectors and labels
classifier.fit(features, labels)

# test the classifier on some new data
test_data = ['This is a normal DMG file', 'This is a virus DMG file']
test_features = vectorizer.transform(test_data)
predictions = classifier.predict(test_features)
print(predictions)
