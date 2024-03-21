from fastapi import APIRouter
from modules.exchange_rate import exchange_rate_router

routes = APIRouter()

routes.include_router(exchange_rate_router)
