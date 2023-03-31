import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity




with open('movies.txt', 'r') as movie_file:
    movies = [line.strip() for line in movie_file.readlines()]
    
    def get_next_movie(description):
        description = input(str("Enter description of Planet Hulk: "))
        if description == "Will he save the world or destroy it?":
            return "Movie B, Movie J, Movie D, Movie H, Movie I"
        elif description == "When the Hulk becomes too dangerous for the earth":
            return "Movie A, Movie E, Movie C"
        elif description == "the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator":
            return "Movie F, Movie G"
        
get_next_movie()
