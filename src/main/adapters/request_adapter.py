#pylint: disable=protected-access
#pylint: disable=line-too-long
from typing import Callable
from fastapi import Request as FastApiRequest
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

async def request_adapter(request: FastApiRequest, controller: Callable) -> HttpResponse:
    body = await request.json() if request.headers.get("Content-Type") == "application/json" else None
    http_request = HttpRequest(
        body=body,
        headers=request.headers,
        query_params=request.query_params,
        path_params=request.path_params,
        url=request.url._url
    )

    http_response = controller(http_request)
    return http_response
