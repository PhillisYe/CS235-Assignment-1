
class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self) -> str:
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other) -> bool:
        # TODO
        if not isinstance(other, Genre):
            return False
        return other.__genre_name == self.__genre_name

    def __lt__(self, other):
        # TODO
        return self.__genre_name < other.__genre_name

    def __hash__(self):
        # TODO
        return hash(self.__genre_name)

class TestGenreMethods:

    def test_init(self):
        genre1 = Genre("Horror")
        assert repr(genre1) == "<Genre Horror>"
        genre2 = Genre("")
        assert genre2.genre_name is None
        genre3 = Genre(42)
        assert genre3.genre_name is None