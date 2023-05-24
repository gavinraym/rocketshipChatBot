import numpy as np
from numpy import linalg
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

# Two phrases
phrase1 = 'This is the first phrase'
phrase2 = 'This is the second phrase'

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the phrases
vectorizer.fit([phrase1, phrase2])
print(vectorizer.transform(["this is a new phrase"]).toarray())
# Convert the count vectors to array
# count_vectors_array = count_vectors.toarray()

# # Get the vectors for phrase1 and phrase2
# vector1 = count_vectors_array[0]
# vector2 = count_vectors_array[1]

# # Calculate the Euclidean distance using linalg.norm
# distance = linalg.norm(vector1 - vector2)

# # Print the Euclidean distance
# print("Euclidean distance:", distance)
