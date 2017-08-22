import sys

from transactions import get_transactions
from balances import get_total_balance, get_running_daily_balances
from pprint import pprint


if __name__ == '__main__':
    if sys.argv[1] == 'transactions':
        pprint(get_transactions())

    elif sys.argv[1] == 'total_balance':
        transactions = get_transactions()
        total = str(get_total_balance(transactions))
        print 'total balance =', total

    elif sys.argv[1] == 'running_daily_balances':
        print 'daily balances'
        transactions = get_transactions()
        dailies = get_running_daily_balances(transactions)
        for key in sorted(dailies.iterkeys()):
            print key, '=', str(dailies[key])

    else:
        print 'Error: no option selected\n' +\
              'Usage: `python resttest/cli.py transactions`\n' +\
              '       `python resttest/cli.py total_balance`\n' +\
              '       `python resttest/cli.py running_daily_balances`'
