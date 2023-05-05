# ======================================== L3T12 Compulsory Task 2 ========================================
# This program reads in the descriptions of movies. Then it defines a function to determine what a viewer should 
# watch next based on the description of a movie they just watched. It returns what to watch next.

import spacy

nlp = spacy.load('en_core_web_md')

# Read in the movies file and make a list of all the descriptions
with open('movies.txt', 'r') as file:
    movies = [line.strip() for line in file.readlines()]

# Define a variable containing hulk description
hulk_description = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
                    Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet 
                    where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where 
                    he is sold into slavery and trained as a gladiator.'''

# Function to return which movies a user would watch
def watch_next(description):
    doc = nlp(description)
    max_similarity = 0          # initialise a highest similairty score
    most_similar_movie = None   # initialise a most similar movie  
    for movie in movies:
        movie_doc = nlp(movie)
        similarity = doc.similarity(movie_doc)
        if similarity > max_similarity: # update the max_similarity and most_similar_movie if the current movie has higher similarity
            max_similarity = similarity
            most_similar_movie = movie
    return most_similar_movie

# Call the function on hulk_description
print("Based on your recent viewing you should watch this next: ")
print(watch_next(hulk_description))
