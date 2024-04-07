#pylint: disable=protected-access
#pylint: disable=line-too-long
from typing import Callable
from fastapi import Request
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

async def request_adapter(request: Request, controller: Callable) -> HttpResponse:
    if request.method == "POST":
        body_dict = await request.json()
    else:
        body_dict = request.json()

    http_request = HttpRequest(
        headers=request.headers,
        query_params=request.query_params,
        path_params=request.path_params,
        url=request.url,
        body=body_dict
    )

    http_response = controller(http_request)

    return http_response
