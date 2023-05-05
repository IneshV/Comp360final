import os
import hashlib
import csv
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report


def get_training_data():
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
    return models.items()


def virus_classifier(path, model_items):
    with open(path, 'r') as file:
        new_file_text = file.read()

    # Convert the new file text into numerical features using the same vectorizer used in training
    vectorizer = CountVectorizer()
    new_file_X = vectorizer.transform([new_file_text])

    # Use the trained models to classify the new file
    for name, model in model_items:
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
        

def is_in_hash_csv(file_path,csv):

    # Calculate the MD5 hash of the file
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            md5_hash.update(chunk)
            sha256_hash.update(chunk)

    # Convert the hash values to hexadecimal strings
    md5_hex = md5_hash.hexdigest()
    sha256_hex = sha256_hash.hexdigest()

    virus = 0
    # Read the data from the CSV file
    for row in csv:
        if row["md5"] == md5_hex or row["sha"]==sha256_hex:
            virus = 1

    if virus = 1:
        print('VIRUS: This file has been hashed and matched as a known virus')
        return True

    else:
        print('This file has been hashed and has not been matched with a known virus')
        return False


def is_executable(file_path):
    byte_count = 0
    line = []

    # Initialize the executable flag to False
    executable = False

    # Open the file for reading in binary mode
    with open(file_path, 'rb') as file:
        # Read the contents of the file and store them in file_content
        file_content = file.read()

    # Get the first two bytes of the file in hexadecimal format
    bit_one = "{0:0{1}x}".format(file_content[0],2)
    bit_two = "{0:0{1}x}".format(file_content[1],2)

    # If the first two bytes are "4d" and "5a" respectively, set the executable flag to True
    if (bit_one=='4d' and bit_two =='5a') or (bit_one == 'MZ' or bit_two == 'MZ'):
        executable = True
        print(file_path+ ' is an executable file')
        return True
    else:
        print(file_path+ ' is not an executable file')
        return False




# function to print the names of all files in a directory
def get_all_files():
    all_files = []
    for root, dirs, files in os.walk("/"):
        for file in files:
            all_files.append(os.path.join(root, file))
            
def main():
    for item in get_all_files():
        executable_files = []
        
        if is_executable(item):
            executable_files.append(item)
        
            print('Executabl Files  are: ')


            with open("data.csv") as csvfile:
                read_csv = csv.DictReader(csvfile)
                c
                
            viruses =[]
            if is_in_hash_csv(item,read_csv):
                viruses.append(item)
                print('Known viruses are: ')
                print(viruses)
            else:
                model_items = get_training_data()
                virus_classifier(item,model_items)


main()
