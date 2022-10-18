from unittest import TestCase

import pytest


class CharactersTest(TestCase):
    @pytest.fixture(autouse=True)
    def setup_client(self, get_client) -> None:
        self.client = get_client

    def test_get_characters(self):
        characters = self.client.get_characters()
        self.assertEqual(characters['total'], 933)

    def test_get_character(self):
        characters = self.client.get_characters('5cd99d4bde30eff6ebccfe2e')
        self.assertEqual(characters['total'], 1)

    def test_get_movie_quotes(self):
        quotes = self.client.get_characters('5cd99d4bde30eff6ebccfe2e', 'quote')
        self.assertEqual(quotes['total'], 166)
