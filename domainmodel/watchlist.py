from domainmodel.movie import Movie

class WatchList:

    def __init__(self):
        self.__watchlist = list()

    def add_movie(self, movie:Movie):
        if movie not in self.__watchlist:
            self.__watchlist.append(movie)

    def remove_movie(self,movie:Movie):
        if movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self,index):
        if index >= len(self.__watchlist) or index < 0:
            return None
        else:
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if self.__watchlist == []:
            return None
        else:
            return self.__watchlist[0]

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.__watchlist):
            result = self.__watchlist[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

class TestWatchListMethods:

    def test_add_movie(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        watchlist.add_movie(Movie("Moana", 2016))
        print(f"Size of watchlist: {watchlist.size()}")
        assert "Size of watchlist: 3"

    def test_remove_movie(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        watchlist.remove_movie(Movie("Moana", 2016))
        print(f"Size of watchlist: {watchlist.size()}")
        assert "Size of watchlist: 2"
        print(watchlist.first_movie_in_watchlist())
        assert "<Movie Ice Age, 2002>"

    def test_remove_movie_not_in_list(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        watchlist.remove_movie(Movie("Moana", 2016))
        watchlist.remove_movie(Movie("The Great Wall", 2016))
        print(f"Size of watchlist: {watchlist.size()}")
        assert "Size of watchlist: 1"
        print(watchlist.first_movie_in_watchlist())
        assert "<Movie Guardians of the Galaxy, 2012>"

    def test_select_smaller_than_zero(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        print(watchlist.select_movie_to_watch(-1))
        assert "None"

    def test_select_in_range(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        print(watchlist.select_movie_to_watch(2))
        assert "<Movie Guardiansof the Galaxy, 2012>"

    def test_select_out_range(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        print(watchlist.select_movie_to_watch(3))
        assert "None"

    def test_first_movie_empty_list(self):
        watchlist = WatchList()
        print(watchlist.first_movie_in_watchlist())
        assert "None"

    def test_iter(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        alist = iter(watchlist)
        for x in alist:
            print(x)
        assert "<Movie Moana, 2016>"
        assert "<Movie Ice Age, 2002>"
        assert "<Movie Guardians of the Galaxy, 2012>"

    def test_next(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        alist = iter(watchlist)
        print(next(alist))
        print(next(alist))
        print(next(alist))
        assert StopIteration

