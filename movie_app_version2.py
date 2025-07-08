from movie_app_functions import *




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
        add_movie(movie_db)
    elif choice==2:
        remove_movie(movie_db)
    elif choice==3:
        view_movies(movie_db)
    elif choice==4:
        find_movie(movie_db)
    elif choice==5:
        update_movie(movie_db)
    elif choice==6:
        rate_movie(movie_db)
    elif choice==7:
        like_movie(movie_db)
    elif choice==8:
        top_movies(movie_db)
    elif choice==9:
        print('Goodbye see u soon ')
        break

