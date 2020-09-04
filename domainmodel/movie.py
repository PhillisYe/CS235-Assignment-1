from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from typing import List

class Movie:

    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title
        if release_year < 1900 or type(release_year) is not int:
            self.__release_year = None
        else:
            self.__release_year = release_year
        self.__description = ""
        self.__director = None
        self.__actors: List[Actor] = list()
        self.__genres: List[Genre] = list()
        self.__runtime_minutes = 0
        self.__rating = 0
        self.__votes = 0
        self.__revenue = 0
        self.__metascores = 0


    @property
    def title(self) -> str:
        return self.__title.strip()

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self) -> str:
        return self.__description.strip()

    @description.setter
    def description(self,description):
        self.__description = description

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self,director):
        director_list = [director]
        if len(director_list) == 1:
            self.__director = director

    @property
    def actors(self):
        return self.__actors

    @property
    def genres(self):
        return self.__genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self,runtime_minutes):
        if runtime_minutes > 0:
            self.__runtime_minutes = runtime_minutes
        else:
            raise ValueError

    @property
    def rating(self) -> float:
        return self.__rating

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    @property
    def votes(self) -> int:
        return self.__votes

    @votes.setter
    def votes(self, votes):
        self.__votes = votes

    @property
    def revenue(self):
        return self.__revenue

    @revenue.setter
    def revenue(self, revenue):
        self.__revenue = revenue

    @property
    def metascores(self) -> int:
        return self.__metascores

    @metascores.setter
    def metascores(self, metascores):
        self.__metascores = metascores

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return other.__title == self.__title and other.__release_year == self.__release_year

    def __lt__(self, other):
        return (self.__title, self.__release_year) < (other.__title, other.__release_year)

    def __hash__(self):
        return hash((self.__title, self.__release_year))

    def add_actor(self, actor: Actor):
        self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre: Genre):
        self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            self.__genres.remove(genre)


class TestMovieMethods:

    def test_init(self):
        movie = Movie("Moana", 2016)
        print(movie)
        assert "<Movie Moana, 2016>"

    def test_dire(self):
        movie = Movie("Moana", 2016)
        director = Director("Ron Clements")
        movie.director = director
        print(movie.director)
        assert "<Director Ron Clements>"

    def test_acto(self):
        movie = Movie("Moana", 2016)
        actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
        for actor in actors:
            movie.add_actor(actor)
        print(movie.actors)
        assert "[<Actor Auli'i Cravalho>, <Actor Dwayne Johnson>, <Actor Rachel House>, <Actor Temuera Morrison>]"

    def test_runtime(self):
        movie = Movie("Moana", 2016)
        movie.runtime_minutes = 107
        print("Movie runtime: {} minutes".format(movie.runtime_minutes))
        assert "Movie runtime: 107 minutes"