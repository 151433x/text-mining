from imdb import Cinemagoer
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def reviewgetter(movie_name=None):
    """this function will take in a name of a movie as a string and will return the first review of that movie. """
    ia=Cinemagoer()
    movie=ia.search_movie(movie_name)[0]
    movie_review=ia.get_movie_reviews(movie.movieID)
    reviewprint=movie_review['data']['reviews'][0]['content']
    return reviewprint
# get 5 actors from the movie
def get_actor(movie_name):
    """this function takes in a movie name and returns 5 actors in the film"""
    ia=Cinemagoer()
    movie=ia.search_movie(movie_name)[0]
    movie=ia.get_movie(movie.movieID)
    fiveactors=movie["cast"][:5]
    return fiveactors
# actor id getter    
def movie_actor_finder(movie_name):
    """this function takes in a movie name and returns 5 actor ids from the cast"""
    alist=[]
    actors=get_actor(movie_name)
    for i in actors:
        alist.append((i.personID))
    return alist
#getting movie list for the actor and thier roles in those movies
def movies_listforactor(actorid):
    """creates a list of all the work that a an actor has been in where they were an actor"""
    ia=Cinemagoer()
    actor=ia.get_person(actorid)
    result=[]
    for job in actor['filmography'].keys():
        if job =='actor':
            for movie in actor['filmography'][job]:
                try : 
                    genre=ia.get_movie(movie.movieID)['genre'or'genres'][0]
                    result.append(genre)
                except: pass
    return result
def count_genre(actorid):
    """ takes the list created in movies_listforactor and counts the genres as well as the number of movies in each genre."""
    genres=movies_listforactor(actorid)
    genre_set=set(genres)
    genre_name=[]
    genre_count=[]
    for genre in genre_set:
        print(f'for the genre {genre},this actor has {genres.count(genre)} movies')
        genre_name.append(genre)
        genre_count.append(genres.count(genre))
    return genre_name,genre_count

def text_analysis(movie_name):
    """this function takes a movie name and analyzes the first review of that movie and print the overall sentiment of the"""
    review=reviewgetter(movie_name)
    score = SentimentIntensityAnalyzer().polarity_scores(review)
    print(score)
# print(text_analysis('truemanshow')) #{'neg': 0.096, 'neu': 0.752, 'pos': 0.152, 'compound': 0.9199}

def main():    
    """creates visualzations for an actors filmogroaphy and its genres"""
    # genre anlysis using graphs
    ia=Cinemagoer()
    actor_name='will smith'
    person=ia.search_person(actor_name)[0]
    print(person)
    name,count= count_genre(person.personID)
    # creating the dataset
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    print('check point, plotting now.')
    plt.bar(name, count, color ='maroon',
            width = 0.4)
    plt.xlabel("Genres")
    plt.ylabel("No. of Movies")
    plt.title(f"Generes of Movies for {person}")
    plt.show()

if __name__=='__main__':
    main()

    
    

