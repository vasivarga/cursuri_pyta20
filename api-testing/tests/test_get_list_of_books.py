import unittest

from requests_folder.books_api import get_list_of_books


class TestGetListOfBooks(unittest.TestCase):

    def test_get_list_of_books_no_params(self):
        response = get_list_of_books()

        assert response.status_code == 200, "Unexpected status code"

        response_body = response.json()

        print(type(response_body))
        print(len(response_body))
        print(type(response_body[0]))
        print(response_body[0]['name'])
        print(response_body[1]['name'])
        print(response_body[2]['name'])
        print(response_body[3]['name'])

        assert len(response_body) == 6, "Unexpected number of results"

    def test_get_list_of_books_filter_by_type(self):
        response = get_list_of_books(book_type="fiction")
        assert response.status_code == 200, "Unexpected status code"

        response_body = response.json()

        for book in response_body:
            print(book['name'])
            assert book['type'] == 'fiction', "Unexpected book type returned"

    def test_get_list_of_books_with_valid_limit(self):
        response = get_list_of_books(limit_size=2)

        assert response.status_code == 200, "Unexpected status code"
        response_body = response.json()
        assert len(response_body) == 2, "Unexpected number of results"

    def test_get_list_of_books_filter_by_invalid_type(self):
        response = get_list_of_books(book_type="invalid_type")

        assert response.status_code == 400, "Unexpected status code"

        response_body = response.json()
        assert response_body['error'] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."

    # def test_get_list_of_books_filter_by_type_and_limit(self):

    # def test_get_list_of_books_with_limit_less_than_0(self):

    # def test_get_list_of_books_with_limit_greater_than_20(self):

