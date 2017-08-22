def get_total_balance(transactions):
    total = 0
    for transaction in transactions:
        total += float(transaction.get('Amount'))
    return total


def get_running_daily_balances(transactions):
    dailies = {}
    for transaction in transactions:
        if transaction.get('Date') in dailies:
            dailies[transaction.get('Date')] += float(transaction['Amount'])
        else:
            dailies[transaction.get('Date')] = 0
    return dailies
