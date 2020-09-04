import csv
from typing import List, Dict
from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies: List(Movie) = list()
        self.__dataset_of_actors: Set(Actor) = set()
        self.__dataset_of_directors: Set(Director) = set()
        self.__dataset_of_genres: Set(Genre) = set()
        self.__movies_with_given_year: Dict(Movie) = dict()
        self.__movies_with_given_director: Dict(Movie) = dict()
        self.__movies_with_given_actor: Dict(Movie) = dict()
        self.__movies_with_given_genre: Dict(Movie) = dict()

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    @property
    def movies_with_given_year(self):
        return self.__movies_with_given_year

    @movies_with_given_year.setter
    def movies_with_given_year(self, year):
        return self.__movies_with_given_year[year]

    @property
    def movies_with_given_actor(self):
        return self.__movies_with_given_actor

    @movies_with_given_actor.setter
    def movies_with_given_actor(self, actor):
        return self.__movies_with_given_actor[actor]

    @property
    def movies_with_given_director(self):
        return self.__movies_with_given_director

    @movies_with_given_director.setter
    def movies_with_given_director(self, director):
        return self.__movies_with_given_director[director]

    @property
    def movies_with_given_genre(self):
        return self.__movies_with_given_genre

    @movies_with_given_genre.setter
    def movies_with_given_genre(self, genre):
        return self.__movies_with_given_genre[genre]

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                self.__dataset_of_movies.append(Movie(title, release_year))

                # add movie with same year into movies_with_given_year
                if release_year not in self.__movies_with_given_year.keys():
                    self.__movies_with_given_year[release_year] = [Movie(title, release_year)]
                else:
                    movie = Movie(title, release_year)
                    self.__movies_with_given_year[release_year].append(movie)

                actors = row['Actors']
                actors_list = actors.split(',')
                for actor in actors_list:
                    if actor not in self.__dataset_of_actors:
                        self.__dataset_of_actors.add(Actor(actor))

                # add movie with same actor into movies_with_given_actor
                for actor in actors_list:
                    if actor not in self.__movies_with_given_actor:
                        self.__movies_with_given_actor[actor] = [Movie(title, release_year)]
                    else:
                        self.__movies_with_given_actor[actor].append(Movie(title, release_year))

                director = row['Director']
                if director not in self.__dataset_of_directors:
                    self.__dataset_of_directors.add(Director(director))

                #add movie with same director into movies_with_given_director
                if director not in self.__movies_with_given_director:
                    self.__movies_with_given_director[director] = [Movie(title, release_year)]
                else:
                    self.__movies_with_given_director[director].append(Movie(title, release_year))

                genres = row['Genre']
                genres_list = genres.split(',')
                for genre in genres_list:
                    if genre not in self.__dataset_of_genres:
                        self.__dataset_of_genres.add(Genre(genre))

                #add movie with same genre into movies_with_given_genre
                for genre in genres_list:
                    if genre not in self.__movies_with_given_genre:
                        self.__movies_with_given_genre[genre] = [Movie(title, release_year)]
                    else:
                        self.__movies_with_given_genre[genre].append(Movie(title, release_year))

                if index > 1000:
                    break

                index += 1

filename = 'Data1000Movies.csv'
movie_file_reader = MovieFileCSVReader(filename)
movie_file_reader.read_csv_file()

class TestcsvMethods:

    def test_init(self):
        filename = 'Data1000Movies.csv'
        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()

        print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
        assert "number of unique movies: 1000"
        print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
        assert "number of unique actors: 1985"
        print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
        assert "number of unique directors: 644"
        print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')
        assert("number of unique genres: 20")

    def test_extension(self):
        filename = 'Data1000Movies.csv'
        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()

        print(len(movie_file_reader.movies_with_given_year[2014]))
        assert "98"
        print(movie_file_reader.movies_with_given_actor["Chris Pratt"])
        assert "[<Movie Guardians of the Galaxy, 2014>, <Movie Jurassic World, 2015>, <Movie The Lego Movie, 2014>]"
        print(movie_file_reader.movies_with_given_director["James Gunn"])
        assert "[<Movie Guardians of the Galaxy, 2014>, <Movie Slither, 2006>, <Movie Super, 2010>]"
        print(len(movie_file_reader.movies_with_given_genre["Action"]))
        assert "303"
