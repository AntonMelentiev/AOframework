def test_make_order__send_correct_data__response_correct(t):
    order_data = t.data.swagger_order_data()

    response = t.step.api.make_order(request_data=order_data)

    t.step.check.equality(obj1=response.json(), obj2=t.data.swagger_order_response(order_data=order_data))
