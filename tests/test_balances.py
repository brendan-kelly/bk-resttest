from resttest.balances import get_total_balance, get_running_daily_balances
from example_data import transactions_list


def test_get_total_balance():
    expected_total_balance = 80.0
    actual_total_balance = get_total_balance(transactions_list)
    assert expected_total_balance == actual_total_balance


def test_get_running_daily_balances():
    expected_daily_running_balances = {
        '2013-12-12': 40.0,
        '2013-12-13': 70.0,
        '2013-12-20': 80.0
    }
    actual_daily_running_balances = get_running_daily_balances(transactions_list)
    assert expected_daily_running_balances == actual_daily_running_balances
