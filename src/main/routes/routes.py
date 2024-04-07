from fastapi import APIRouter, Request


# Import adapters
from src.main.adapters.request_adapter import request_adapter

# Import composers
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer

# Import error handler
from src.errors.error_handler import handle_errors

router = APIRouter()

@router.get('/user/find')
async def find_user(request: Request):
    http_response = None

    try:
        http_response = await request_adapter(request, user_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response

@router.post('/user/')
async def register_user(request: Request):
    http_response = None
    try:
        http_response = await request_adapter(request, user_register_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return http_response
