from unittest import TestCase

import pytest


class QuotesTest(TestCase):
    @pytest.fixture(autouse=True)
    def setup_client(self, get_client) -> None:
        self.client = get_client

    def test_get_quotes(self):
        quotes = self.client.get_quotes()
        self.assertEqual(quotes['total'], 2390)

    def test_get_quote(self):
        quotes = self.client.get_quotes('5cd96e05de30eff6ebccebce')
        self.assertEqual(quotes['total'], 1)
