from fetch import Fetch
from movie import Movie

title_art = r"""
-------------------
< Hello! traveller >
-------------------
     /\_/\  
    ( o.o ) 
     > ^ < 

"""

print(title_art)


def main():
    search_results = True
    movie_list = None

    print("Enter the movie name \n")

    while search_results:
        movie_name = input(" ")
        print(f"Searching for {movie_name} .... \n")
        movie = Fetch()
        movie_list = movie.fetch_data(f"list_movies.json?query_term={movie_name}")

        if movie_list['data']['movie_count'] >= 1:
            search_results = False
        else:
            print(f"{movie_name} resulted in 0 results \n Please try with another name... \n")

    handle_movie = Movie(movie_list)
    handle_movie.display_movies()

    while handle_movie.valid_index:
        print("Please enter the index for the movie that you'd like to stream / download")
        user_choice = input()
        print("Enter 1 to stream the movie or 2 to download")
        stream_choice = int(input())

        if (stream_choice > 1):
            handle_movie.download = True
        handle_movie.handle_movie_stream(user_choice)


main()