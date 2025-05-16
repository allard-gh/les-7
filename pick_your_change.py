import requests
import json

def get_eur_to_currency_rate(api_key):
    response = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR")

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data["conversion_rates"], indent=4))
        currency = input('Naar welke valuta wil je omrekenen? \n')
        if currency in data["conversion_rates"]:
            return data["conversion_rates"][currency], currency
        else:
            print(f'Error: Wisselkoers {currency} niet gevonden.')
            return None, None
    else:
        print(f'Oeps, foutje: {response.status_code}: {response.text}')
        return None, None

def convert_eur_to_currency(amount, exchange_rate):
    return round((amount * exchange_rate), 2)

def main():
    api_key = "fa41e8015a533eb1fe76d0d3"
    eur_amount = float(input("Voer het bedrag in EUR in: ").strip())
    exchange_rate, currency = get_eur_to_currency_rate(api_key)
    currency_amount = convert_eur_to_currency(eur_amount, exchange_rate)
    print(f'EUR {eur_amount:.2f} is bij een wisselkoers van {exchange_rate}: {currency} {currency_amount:.2f}.')

main()
