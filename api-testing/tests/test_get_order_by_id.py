import unittest

from requests_folder.books_api import submit_order, get_order_by_id


class TestGetOrder(unittest.TestCase):

    def test_get_order_by_valid_id(self):

        response_1 = submit_order(1, "Pyta20")
        assert response_1.status_code == 201, "Unexpected status code"

        order_id = response_1.json()['orderId']
        response_2 = get_order_by_id(order_id)

        assert response_2.status_code == 200, f"Unexpected status code,\n {response_2.status_code} \n {response_2.text}"
        assert response_2.json()['id'] == order_id, "Unexpected order id"

    # def test_get_order_by_invalid_id(self):