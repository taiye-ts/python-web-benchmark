from test_pb2 import TransactionStore, TransactionItem


def to_dict_g(t):
    return {
        'id': t.id,
        'account_id': t.account_id,
        'lock_version': t.lock_version,
        'transactions': [
            {
                'transaction_catalog_item_id': item.transaction_catalog_item_id,
                'balance': item.balance
            } for item in t.transactions
        ]
    }

def generate_message(count):
    t = TransactionStore()
    t.id = str(count)
    t.lock_version = count
    t.account_id = count
    for i in range(count):
        t.transactions.append(TransactionItem(transaction_catalog_item_id=i, balance=i))

    result = t.SerializeToString()
    print(result)
    print(len(result))

    return t
