from src.presentation.controllers.user_register_controller import UserRegisterController
from src.data.tests.user_register import UserRegisterSpy


class HttpRequestMock():
    def __init__(self) -> None:
        self.body = { "first_name": "meuTeste", "last_name": "teste", "age" : 3}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = UserRegisterSpy()
    user_register_controller = UserRegisterController(use_case)

    response = user_register_controller.handle(http_request_mock)

    assert response.status_code == 200
    assert response.body["data"] is not None
