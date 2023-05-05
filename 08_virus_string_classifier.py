import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report

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

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, df['label'], test_size=0.3)

# Train multiple models on the data
models = {
    'MultinomialNB': MultinomialNB(),
    'LogisticRegression': LogisticRegression(),
    'SVC': SVC()
}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"Model: {name}")
    print(classification_report(y_test, y_pred))
