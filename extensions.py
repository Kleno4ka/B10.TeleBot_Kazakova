import requests
import json
from config import exchanges


class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Impossible to convert the same currency {base} ')

        try:
            quote_ticker = exchanges[quote]
        except KeyError:
            raise ConvertionException(f'Impossible to convert {quote}')

        try:
            base_ticker = exchanges[base]
        except KeyError:
            raise ConvertionException(f'Impossible to convert {base}')

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise ConvertionException(f'Impossible to convert amount {amount}')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[exchanges[base]] * float(amount)

        return round(total_base, 2)