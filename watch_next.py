# Import module
import spacy

# Load model "en_core_web_md" - a relative small module but not the smallest
nlp = spacy.load("en_core_web_lg")

# Old movie description
movie_description = 'Will he save their world or destroy it? When the Hulk becomes too dangerous' \
                    ' for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet ' \
                    'where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold' \
                    ' into slavery and trained as a gladiator.'

# Read the movies file
try:
    with open("movies.txt", "r") as movie_txt:
        movie_list = movie_txt.read().splitlines()
except FileExistsError:
    print("movie.txt does not exist.")


# Recommend a movie
def recommendation(n_movie, old_movie_description):
    n_movie = n_movie.split(":")

    # Check similarity
    def check_sim(old_movie_, new_movie_):
        return old_movie_.similarity(new_movie_)

    # Perform direct similarity check
    old_movie = nlp(old_movie_description)
    new_movie = nlp(n_movie[1])
    score_normal = check_sim(new_movie, old_movie)

    # Perform the similarity check after we remove all stop words (assume stop words have less relevance)
    new_movie = nlp(' '.join([str(word1) for word1 in new_movie if not word1.is_stop]))
    old_movie = nlp(' '.join([str(word2) for word2 in old_movie if not word2.is_stop]))
    score_no_stop = check_sim(new_movie, old_movie)

    # Perform the similarity check using only 'NOUN', 'PROPN' (assume the most relevant words are 'NOUN', 'PROPN')
    new_movie = nlp(' '.join([str(word) for word in new_movie if word.pos_ in ['NOUN', 'PROPN']]))
    old_movie = nlp(' '.join([str(word) for word in old_movie if word.pos_ in ['NOUN', 'PROPN']]))
    score_npv = check_sim(new_movie, old_movie)

    # Uncomment next line to see all scores for all movies
    # print(f" {movie[0]} - score_normal={score_normal} - score_no_stop={score_no_stop} - score_npv={score_npv}")

    # Method choice
    if method_choice == 'n':
        return score_normal
    elif method_choice == 's':
        return score_no_stop
    elif method_choice == 'r':
        return score_npv
    elif method_choice == 'a':
        return (score_normal + score_no_stop + score_npv) / 3
    else:
        quit()


while True:
    # Main menu
    method_choice = input(f'''Chose the method used for recommendation and check out the different results:
                 n - For simple similarity check
                 s - To eliminate all stop words
                 r - To perform check using only  PROPER NOUNs and NOUNs
                 a - To make an average of all 3 methods 
                 e - Press e or any other unassigned key to exit program
                :''').strip().lower()

    # Compare old movie descriptions with all possible recommendation
    score = 0
    recommended_movie = ""
    for movie in movie_list:
        new_score = recommendation(movie, movie_description)
        if new_score > score:
            recommended_movie = movie
            score = new_score

    recommended_movie = recommended_movie.split(":")
    print(f"\nOur recommendation is {recommended_movie[0]} with a score of {round(score * 100)}% \n\n"
          f"Movie description:\n {recommended_movie[1]}")
    print(f'\n***************** Old movie description ******************\n\n {movie_description}\n\n')
