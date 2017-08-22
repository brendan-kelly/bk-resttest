import requests


def get_transactions():
    transactions = []
    page = 1
    while True:
        transactions_api = 'http://resttest.bench.co/transactions/{}.json'.format(page)
        req = requests.get(transactions_api)
        # Assumption: If the API returns a 200, there are results in the list
        if req.status_code == 200:
            transactions.extend(req.json().get('transactions') or [])
        elif req.status_code == 404:
            break
        else:
            break
        page += 1
    return transactions
