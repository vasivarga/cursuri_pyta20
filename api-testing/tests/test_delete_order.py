from requests_folder.books_api import submit_order, delete_order, get_order_by_id


class TestDeleteOrder:

    def test_delete_valid_order(self):
        response_1 = submit_order(1, "Pyta20")
        assert response_1.status_code == 201, "Unexpected status code"

        order_id = response_1.json()['orderId']

        response_2 = delete_order(order_id)
        assert response_2.status_code == 204

        response_3 = get_order_by_id(order_id)
        assert response_3.json()['error'] == f"No order with id {order_id}."