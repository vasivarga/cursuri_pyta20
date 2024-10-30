import random
import unittest

from requests_folder.books_api import get_book_by_id


class TestGetASingleBook(unittest.TestCase):

    def test_get_book_by_id(self):
        book_to_get = random.randint(1, 6)
        print(book_to_get)

        response = get_book_by_id(book_to_get)

        assert response.status_code == 200, "Unexpected status code"
        assert response.json()['id'] == book_to_get, "Unexpected book returned"

        print(response.json())

    # def test_get_book_with_invalid_id(self):