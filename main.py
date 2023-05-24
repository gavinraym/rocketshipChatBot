from dataset import questions, answers
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# # Remove punctuation and stop words
# def preprocess_text(text):
#     text.translate(str.maketrans("","",'''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''))  # Remove punctuation
#     text = text.lower()  # Convert to lowercase
#     return text

processed_dataset = []
for question in questions:
    question.translate(str.maketrans("","",'''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''))  # Remove punctuation
    question = question.lower()  # Convert to lowercase
    processed_dataset.append(question)
    
# Count vectorize the questions
vectorizer = CountVectorizer(stop_words='english')
count_matrix = vectorizer.fit_transform(processed_dataset)

# Main loop
while True:
    # Ask for user input
    user_input = input("Ask a question (or enter 'q' to quit): ")
    if user_input == 'q':
        break
    
    user_input.translate(str.maketrans("","",'''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''))  # Remove punctuation

    # Process user input
    processed_input = user_input.lower()
    input_vector = vectorizer.transform([processed_input])

    # Calculate cosine similarities
    similarities = cosine_similarity(input_vector, count_matrix)

    # Find most similar question
    most_similar_index = similarities.argmax()

    answer = answers[most_similar_index]

    # Return the answer
    print("Answer:", answer)
