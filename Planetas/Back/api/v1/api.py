from fastapi import APIRouter
from api.v1.endpoints import planeta

api_router = APIRouter()
api_router.include_router(planeta.router, prefix="/planetas", tags=["planetas"])