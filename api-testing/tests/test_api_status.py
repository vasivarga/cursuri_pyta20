import unittest

from requests_folder.books_api import get_api_status


class TestApiStatus(unittest.TestCase):

    def test_api_status(self):
        response = get_api_status()

        response_body = response.json()
        assert response.status_code == 200, "Unexpected status code"
        assert response_body['status'] == 'OK', "Unexpected status"
