# #1. Add movie
# 2. Remove movie
# 3. View all movies
# 4. Find a movie
# 5. Update a movie
# 6. Rate a movie
# 7. Like a movie
# 8. Top n movies
# 9. Quit
#
# Enter your choice: 1
#
# Enter the movie title: ABC
# Enter the movie director: JOHN
# Enter the movie release year: 2010
#
# Movie ABC added successfully!



menu='''Movie App
1. Add movie
2. Remove movie
3. View all movies
4. Find a movie
5. Update a movie
6. Rate a movie
7. Like a movie
8. Top n movies
9. Quit

Enter your choice:
'''
movie_db={
    'titanic':{'title':'titanic1','director':'james cameroon','release_year': 1998,'rating':7.2,'likes':56500,'cast':['leonardo','kate'] },
    'titanic1':{'title':'titanic2','director':'james cameroon','release_year': 1998,'rating':7.4,'likes':56500,'cast':['leonardo','kate'] },
    'titanic2':{'title':'titanic3','director':'james cameroon','release_year': 1998,'rating':7.6,'likes':56500,'cast':['leonardo','kate'] },
    'titanic3':{'title':'titanic4','director':'james cameroon','release_year': 1998,'rating':7.1,'likes':56500,'cast':['leonardo','kate'] },
}
while True:
    choice=int(input(menu))
    if choice==1:
        title=input('enter movie title: ')
        director=input('enter director: ')
        release_year=int(input('enter movie release_year: '))
        rating=float(input('enter movie_rating: '))
        likes=int(input('enter movie_likes: '))
        cast=input('enter movie_cast: ').split(',')
        movie={'title':title,'director':director,'release_year':release_year,'rating':rating,'likes':likes,'cast':cast}
        movie_db[title]=movie
        print('movie is added to database')
    elif choice==2:
        title=input('enter movie title to remove: ')
        if title in movie_db:
            movie_db.pop(title)
            print('movie is removed ')
    elif choice==3:
        print('All movies')
        for movie in movie_db.values():
            print(f"Title:{movie['title']},director:{movie['director']},release_year:{movie['release_year']},rating:{movie['rating']},likes:{movie['likes']},cast:{','.join(movie['cast'])} ")
    elif choice==4:
        title=input('Enter the movie you want to find: ')
        if title in movie_db:
            movie=movie_db.get(title)
            print('Here is the movie you searched for ')
            print(f"Title:{movie['title']},director:{movie['director']},release_year:{movie['release_year']},rating:{movie['rating']},likes:{movie['likes']},cast:{','.join(movie['cast'])} ")
        else:
            print('Movie not found')
    elif choice==5:
        title=input('Enter the movie you want to be updated:')
        if title in movie_db:
           update_field = input('Enter the field to be updated: ')
           new_value = input('Enter the new_value: ')
           movie_db[title][update_field]=new_value
           print(f'movie {title} updated ')
        else:
            print('Movie not found')
    elif choice==6:
        title=input('Enter the movie you wish to rate: ')
        if title in movie_db:
            rating= float(input("new rating:"))
            movie_db[title]["rating"] = rating
            print(f'movie {title} rated ')
        else:
            print('Movie not found')
    elif choice==7:
        title=input("Enter the movie you wish to like: ")
        if title in movie_db:
            movie_db[title]["likes"] += 1
            print(f"movie {title} liked ")
        else:
            print('Movie not found')
    elif choice==8:
        no=int(input('enter the number of movies:'))
        movies=sorted(movie_db.values(),key=lambda movie:movie['rating'],reverse=True)
        print(f'Top {no}  movies')
        for movie in movies[:no]:
            print(
                f"Title:{movie['title']},director:{movie['director']},release_year:{movie['release_year']},rating:{movie['rating']},likes:{movie['likes']},cast:{','.join(movie['cast'])} ")
    elif choice==9:
        print('Goodbye see u soon ')
        break

