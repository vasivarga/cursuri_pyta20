import unittest

from requests_folder.books_api import submit_order


class TestSubmitOrder(unittest.TestCase):

    def test_submit_order_valid_book_id(self):
        response = submit_order(1, "PyTa20")
        assert response.status_code == 201, "Unexpected status code"
        assert response.json()['created'], "Order not created"

    # def_test_submit_order_for_book_out_of_stock(self):

    # def_test_submit_order_for_invalid_book_id(self):