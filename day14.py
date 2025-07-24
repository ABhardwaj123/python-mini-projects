#json movie record keeper

import os
import json

file_name = "movies.json"
#json->javascript object notation

file_name = "movies.json"

def load_movies():
    if not os.path.exists(file_name):
        return []
    
    with open(file_name , "r" , encoding = "utf-8") as f:
        return json.load(f)
    
    
def save_movies(movies): #accepts movies as the json file
    with open(file_name , "w" , encoding = "utf-8") as f:
        json.dump(movies , f , indent = 5)


def add_movies(movies):
    movie_name = input("enter movie name: ").strip().lower()

    if any(movie['title'].lower() == movie_name for movie in movies):
        print("this movie already exists!")
        return
    
    genre = input(f"enter the genre of {movie_name}: ")
    try:
        rating = float(input("enter rating from 1-10: "))
        if rating <0 or rating > 10:
            raise ValueError()
        
    except ValueError():
        print("invalid rating")
        return
    
    movies.append({"title" : movie_name , "genre" : genre , "rating": rating})
    save_movies(movies)

def search_movie(movies):
    search = input("enter the movie name or genre you want to search: ").strip().lower()

    matches = [
        movie for movie in movies
        if search in movie['title'].lower() or search in movie['genre'].lower()
    ]

    if not matches:
        print("no match found!")
        return
    
    print(f"found {len(matches)} result(s)")

    for movie in matches:
        print(f"{movie['title']} -> {movie['genre']} -> {movie['rating']}")


def display_movies(movies):
    if not movies:
        print("no movies found!\n")
        return
    
    print()
    for movie in movies:
        print(f"{movie['title']} -> {movie['genre']} -> {movie['rating']}")

    print()



def run_movie_fxn():

    movies = load_movies()

    while True:
        print("1. Add movie")
        print("2. View All Movie(s)")
        print("3. Search movie")
        print("4. Exit")

        choice = int(input("enter your choice: "))

        match choice:
            case 1:
                add_movies(movies)

            case 2:
                display_movies(movies)

            case 3:
                search_movie(movies)

            case 4:
                break

            case _:
                print("invalid choice!")
                

if __name__ == "__main__":
    run_movie_fxn()






    



