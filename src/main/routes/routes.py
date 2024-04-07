from fastapi import APIRouter, status, Request


# Import adapters
from src.main.adapters.request_adapter import request_adapter

# Import composers
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer

router = APIRouter()

@router.get('/user/find', status_code=status.HTTP_200_OK)
async def find_user(request: Request):
    http_response = await request_adapter(request, user_finder_composer())
    return http_response

@router.post('/user/', status_code=status.HTTP_201_CREATED)
async def register_user(request: Request):
    http_response = await request_adapter(request, user_register_composer())
    return http_response
