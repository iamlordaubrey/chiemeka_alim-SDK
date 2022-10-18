from unittest import TestCase

import pytest


class ChaptersTest(TestCase):
    @pytest.fixture(autouse=True)
    def setup_client(self, get_client) -> None:
        self.client = get_client

    def test_get_chapters(self):
        chapters = self.client.get_chapters()
        self.assertEqual(chapters['total'], 62)

    def test_get_chapter(self):
        chapters = self.client.get_chapters('6091b6d6d58360f988133bc8')
        self.assertEqual(chapters['total'], 1)
