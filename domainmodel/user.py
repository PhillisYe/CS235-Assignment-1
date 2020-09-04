from domainmodel.movie import Movie
from domainmodel.review import Review
from typing import List

class User:

    def __init__(self, user_name:str, password:str):
        self.__user_name = user_name.lower().strip()
        self.__password: str = password
        self.__watched_movies: List[Movie] = list()
        self.__reviews: List[Review] = list()
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    def __repr__(self) -> str:
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other.__user_name == self.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash((self.__user_name, self.__password))

    def watch_movie(self,movie):
        self.__watched_movies.append(movie)
        runtime = movie.runtime_minutes
        self.__time_spent_watching_movies_minutes += runtime

    def add_review(self,review):
        self.__reviews.append(review)

class TestDirectorMethods:

    def test_init(self):
        user1 = User('Martin', 'pw12345')
        movie = Movie("Moana",2016)
        user1.watch_movie(movie)
        print(user1.time_spent_watching_movies_minutes)
        assert 107
        user2 = User('Ian', 'pw67890')
        user3 = User('Daniel', 'pw87465')
        print(user1)
        assert "<User martin>"
        print(user2)
        assert "<User ian>"
        print(user3)
        assert "<User daniel>"