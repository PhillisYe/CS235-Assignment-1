from datetime import datetime

from domainmodel.movie import Movie

class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        self.__movie: Movie = movie
        self.__review_text: str = review_text
        if rating >= 1 and rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.now()

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return ("{}({!r})".format(self.__class__.__name__, self.__movie, self.__review_text, self.__rating, self.__timestamp))

    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        return other.__movie == self.__movie and \
               other.__review_text == self.__review_text and \
               other.__rating == self.__rating and \
               other.__timestamp == self.__timestamp

class TestReviewMethods:

    def test_init(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)

        print(review.movie)
        assert "<Movie Moana, 2016>"
        print("Review: {}".format(review.review_text))
        assert "Review: This movie was very enjoyable."
        print("Rating: {}".format(review.rating))
        assert "Rating: 8"