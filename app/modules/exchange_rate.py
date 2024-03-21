from typing import Dict, List, TypedDict, Union

import requests
from cachetools import TTLCache, cached
from fastapi import APIRouter, HTTPException, Query

router = APIRouter(prefix="/exchange-rate", tags=["Exchange Rate"])

api_url: str = "https://economia.awesomeapi.com.br/json/last/"
options_currency: List[str] = ["USD", "BRL", "EUR", "BTC", "ETH"]


class ExchangeRate(TypedDict):
    code: str
    codein: str
    name: str
    high: str
    low: str
    varBid: str
    pctChange: str
    bid: str
    ask: str
    timestamp: str
    create_date: str


# aqui eu criei um cache para armazenar os valores das requisições feitas para a API
cache = TTLCache(maxsize=128, ttl=86400)


# aqui eu defini que a função get_exchange_rate_from_api será cacheada
# isso reduz significativamente o tempo de resposta da API
@cached(cache)
def get_exchange_rate_from_api(currency: str) -> Dict[str, ExchangeRate]:
    try:
        response = requests.get(f"{api_url}{currency}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        raise HTTPException(status_code=500, detail=str(error)) from error


@router.get("/", response_model=Dict[str, Union[str, float]])
async def get_exchange_rate(
    currency_from: str = Query(options_currency[1], enum=options_currency),
    currency_to: str = Query(options_currency[0], enum=options_currency),
    amount: float = Query(1.0, ge=0),
) -> Dict[str, Union[str, float]]:
    if currency_from == currency_to:
        raise HTTPException(
            status_code=400,
            detail="As moedas a serem convertidas não podem ser iguais",
        )
    if (
        currency_from not in options_currency
        or currency_to not in options_currency
    ):
        raise HTTPException(
            status_code=400,
            detail="As moedas fornecidas são inválidas. Escolha entre USD, BRL, EUR, BTC, ETH",
        )

    try:
        response = get_exchange_rate_from_api(
            f"{currency_from}-{currency_to}".upper()
        )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error)) from error

    currency = f"{currency_from}{currency_to}".upper()

    return {
        "currency_from": currency_from,
        "currency_to": currency_to,
        "amount": amount,
        "exchange_rate": float(response[currency]["bid"]),
        "total": amount * float(response[currency]["bid"]),
    }


exchange_rate_router = router
