import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

or_text = "Hello! If you reading this text - you are literally can read different words."
with open("or_text.txt", "w", encoding="utf-8") as file:
    file.write(or_text)

with open("or_text.txt", "r", encoding="utf-8") as file:  # Fixed filename
    text = file.read()

tokens = word_tokenize(text)

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
stemmed_tokens = [stemmer.stem(token) for token in tokens]

stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in stemmed_tokens if word.lower() not in stop_words]

processed_tokens = [word for word in filtered_tokens if word not in string.punctuation]

processed_text = ' '.join(processed_tokens)  

# Save the processed text to a new file
with open("processed_text.txt", "w", encoding="utf-8") as file:
    file.write(processed_text)

print("Text successfully saved in a new file.")
