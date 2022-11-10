from datetime import datetime
from typing import Dict, Any

from framework.constants import DATETIME_FORMAT


class TestDataCreator:
    @property
    def google_text_to_search(self) -> str:
        return "Selenium"

    @property
    def python_text_to_search(self) -> str:
        return "builtin"

    @staticmethod
    def swagger_order_data(
        id: int = 10,
        pet_id: int = 198772,
        quantity: int = 7,
        ship_date: datetime = datetime.now(),
        status: str = "approved",
        complete: bool = True,
    ) -> Dict[str, Any]:
        return {
            "id": id,
            "petId": pet_id,
            "quantity": quantity,
            "shipDate": ship_date.strftime(DATETIME_FORMAT),
            "status": status,
            "complete": complete,
        }

    @staticmethod
    def swagger_order_response(order_data: Dict[str, Any]) -> Dict[str, Any]:
        order_data["shipDate"] = order_data["shipDate"][:-4] + "+00:00"
        return order_data

    def get_some_other_test_data(self):
        #  prepare and return test data
        pass
