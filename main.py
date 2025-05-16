import requests

def get_eur_to_usd_rate(api_key):
    response = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR")

    if response.status_code == 200:
        data = response.json()
        if "USD" in data["conversion_rates"]:
            return data["conversion_rates"]["USD"]
        else:
            print(f'Error: Wisselkoers USD niet gevonden.')
            return None
    else:
        print(f'Oeps, foutje: {response.status_code}: {response.text}')
        return None

def convert_eur_to_usd(amount, exchange_rate):
    return round((amount * exchange_rate), 2)

def main():
    api_key = "fa41e8015a533eb1fe76d0d3"
    eur_amount = float(input("Voer het bedrag in EUR in: ").strip())
    exchange_rate = get_eur_to_usd_rate(api_key)
    usd_amount = convert_eur_to_usd(eur_amount, exchange_rate)
    print(f'€{eur_amount:.2f} is bij een wisselkoers van {exchange_rate}: ${usd_amount:.2f}.')

main()
