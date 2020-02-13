import requests, json

def set_currency():
    url="https://api.exchangerate-api.com/v4/latest/USD"

    response = json.loads(requests.request("GET",url).text)

    bases = dict(response['rates'])
    names = list(bases.keys())
    
    for name in names:
        currency = '<option>{0}</option>'.format(name)
        print(currency)

    return names

if __name__ == '__main__':
    set_currency()