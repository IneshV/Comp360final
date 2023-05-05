import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report

# Define the folders for safe and malicious strings
safe_strings_folder = 'path/to/safe_strings_folder'
malicious_strings_folder = 'path/to/malicious_strings_folder'

# Load the safe strings into a pandas dataframe
safe_strings = []
for filename in os.listdir(safe_strings_folder):
    with open(os.path.join(safe_strings_folder, filename), 'r') as file:
        safe_strings.append(file.read())
safe_df = pd.DataFrame({'text': safe_strings, 'label': 0})

# Load the malicious strings into a pandas dataframe
malicious_strings = []
for filename in os.listdir(malicious_strings_folder):
    with open(os.path.join(malicious_strings_folder, filename), 'r') as file:
        malicious_strings.append(file.read())
malicious_df = pd.DataFrame({'text': malicious_strings, 'label': 1})

# Concatenate the safe and malicious dataframes into one dataframe
df = pd.concat([safe_df, malicious_df])

# Convert the text data into numerical features using the CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train multiple models on the data
models = {
    'MultinomialNB': MultinomialNB(),
    'LogisticRegression': LogisticRegression(),
    'SVC': SVC()
}
for name, model in models.items():
    model.fit(X, y)

# Load the new file to classify
new_file_path = 'path/to/new/file'
with open(new_file_path, 'r') as file:
    new_file_text = file.read()

# Convert the new file text into numerical features using the same vectorizer used in training
new_file_X = vectorizer.transform([new_file_text])

# Use the trained models to classify the new file
for name, model in models.items():
    print(f"Model: {name}")
    prediction = model.predict(new_file_X)[0]
    if prediction == 0:
        print("Prediction: Safe")
    else:
        print("Prediction: Malicious")
    print("Confusion Matrix:")
    print(confusion_matrix(y, model.predict(X)))
    print("Classification Report:")
    print(classification_report(y, model.predict(X)))
