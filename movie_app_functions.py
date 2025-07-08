def add_movie(movie_db):
    title = input('enter movie title: ')
    director = input('enter director: ')
    release_year = int(input('enter movie release_year: '))
    rating = float(input('enter movie_rating: '))
    likes = int(input('enter movie_likes: '))
    cast = input('enter movie_cast: ').split(',')
    movie = {'title': title, 'director': director, 'release_year': release_year, 'rating': rating, 'likes': likes,
             'cast': cast}
    movie_db[title] = movie
    print('movie is added to database')
def remove_movie(movie_db):
    title = input('enter movie title to remove: ')
    if title in movie_db:
        movie_db.pop(title)
        print('movie is removed ')
def view_movies(movie_db):
    print('All movies')
    for movie in movie_db.values():
        print(
            f"Title:{movie['title']},director:{movie['director']},release_year:{movie['release_year']},rating:{movie['rating']},likes:{movie['likes']},cast:{','.join(movie['cast'])} ")
def find_movie(movie_db):
    title = input('Enter the movie you want to find: ')
    if title in movie_db:
        movie = movie_db.get(title)
        print('Here is the movie you searched for ')
        print(
            f"Title:{movie['title']},director:{movie['director']},release_year:{movie['release_year']},rating:{movie['rating']},likes:{movie['likes']},cast:{','.join(movie['cast'])} ")
    else:
        print('Movie not found')
def update_movie(movie_db):
    title = input('Enter the movie you want to be updated:')
    if title in movie_db:
        update_field = input('Enter the field to be updated: ')
        new_value = input('Enter the new_value: ')
        movie_db[title][update_field] = new_value
        print(f'movie {title} updated ')
    else:
        print('Movie not found')
def rate_movie(movie_db):
    title = input('Enter the movie you wish to rate: ')
    if title in movie_db:
        rating = float(input("new rating:"))
        movie_db[title]["rating"] = rating
        print(f'movie {title} rated ')
    else:
        print('Movie not found')
def like_movie(movie_db):
    title = input("Enter the movie you wish to like: ")
    if title in movie_db:
        movie_db[title]["likes"] += 1
        print(f"movie {title} liked ")
    else:
        print('Movie not found')
def top_movies(movie_db):
    no = int(input('enter the number of movies:'))
    movies = sorted(movie_db.values(), key=lambda movie: movie['rating'], reverse=True)
    print(f'Top {no}  movies')
    for movie in movies[:no]:
        print(
            f"Title:{movie['title']},director:{movie['director']},release_year:{movie['release_year']},rating:{movie['rating']},likes:{movie['likes']},cast:{','.join(movie['cast'])} ")
