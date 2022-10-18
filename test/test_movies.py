from unittest import TestCase

import pytest


class MoviesTest(TestCase):
    @pytest.fixture(autouse=True)
    def setup_client(self, get_client) -> None:
        self.client = get_client

    def test_get_movies(self):
        movies = self.client.get_movies()
        self.assertEqual(movies['total'], 8)

    def test_get_movie(self):
        movies = self.client.get_movies('5cd95395de30eff6ebccde5b')
        self.assertEqual(movies['total'], 1)

    def test_get_movie_quotes(self):
        quotes = self.client.get_movies('5cd95395de30eff6ebccde5b', 'quote')
        self.assertEqual(quotes['total'], 1010)
