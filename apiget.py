# json
# {"name": "Radek"} - json - odpowiednik słownik
# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/
from typing import List

import requests as re
import json
from pydantic import BaseModel


class Rate(BaseModel):
    no: str
    effectiveDate: str
    mid: float


# w pydantic podpowiedzi służą jako walidator
class Currency(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rate]


url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'

response = re.get(url)
print(response)
# <Response [200]>  - ok
# 4.. - błedy, 404 błedny adres
# 3.. - posrednie
# 5.. błedy wewnętrne serwera
table = response.json()
print(table)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR', 'rates': [{'no': '099/A/NBP/2023', 'effectiveDate': '2023-05-24', 'mid': 4.4803}]}
print(table['table'])
print(table['rates'])
# [{'no': '099/A/NBP/2023', 'effectiveDate': '2023-05-24', 'mid': 4.4803}]
print(table['rates'][0])
# {'no': '099/A/NBP/2023', 'effectiveDate': '2023-05-24', 'mid': 4.4803}
print(table['rates'][0]['mid'])

currency_obj = Currency.parse_raw(response.text)
print(currency_obj)

print(currency_obj.rates[0].mid)
