from resttest.transactions import get_transactions


def test_get_transactions_is_list():
    transactions = get_transactions()
    assert isinstance(transactions, list)
