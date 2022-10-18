from unittest import TestCase

from src.lotr.endpoints import LordOfTheRings


class BooksTest(TestCase):
    def setUp(self) -> None:
        self.client = LordOfTheRings()

    def test_get_books(self):
        books = self.client.get_books()
        self.assertEqual(books['total'], 3)

    def test_get_book(self):
        books = self.client.get_books('5cf58077b53e011a64671583')
        self.assertEqual(books['total'], 1)

    def test_get_book_chapters(self):
        chapters = self.client.get_books('5cf58077b53e011a64671583', 'chapter')
        self.assertEqual(chapters['total'], 21)
