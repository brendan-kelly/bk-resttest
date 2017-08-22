import json
import sys

from transactions import get_transactions
from balances import get_total_balance, get_running_daily_balances
from pprint import pprint
from lib.byteify import json_loads_byteified


if __name__ == '__main__':
    if sys.argv[1] == 'transactions':
        transactions = get_transactions()
        # Used to print out JSON string without unicode u's
        transactions_json = json.dumps(get_transactions())
        pprint(json_loads_byteified(transactions_json))

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
