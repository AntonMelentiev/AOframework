from http import HTTPStatus
from typing import Dict, Any

import allure
from requests import Session, Request, Response, RequestException

from framework.enums import HTTPMethod


class UnexpectedStatusCode(RequestException):
    pass


class ApiStep:
    def __init__(self, base_api_url: str):
        self._session = None
        self._base_api_url = base_api_url

    @property
    def __session(self) -> Session:
        if self._session is None:
            self._session = Session()
        return self._session

    def _call(self, request: Request, expected_status_code: HTTPStatus) -> Response:
        request.url = self._base_api_url + request.url
        request.headers.update({"Content-Type": "application/json"})
        prepared_request = self.__session.prepare_request(request=request)
        response = self.__session.send(request=prepared_request)

        if response.status_code != expected_status_code:
            raise UnexpectedStatusCode(
                f"Expected status code {expected_status_code}, but returned {response.status_code}",
                response=response,
            )

        return response

    ####################################################################################################################
    # Actions
    ####################################################################################################################

    @allure.step
    def make_order(
        self,
        request_data: Dict[str, Any],
        expected_status_code: HTTPStatus = HTTPStatus.OK,
    ):
        request = Request(
            method=HTTPMethod.POST, url="/store/order", headers={}, json=request_data  # add headers if required
        )

        response = self._call(request=request, expected_status_code=expected_status_code)

        return response  # you can return body from here
