from test_pb2 import TransactionStore


def to_dict(body):
    t = TransactionStore()
    t.ParseFromString(body)
    result = {
        'id': t.id,
        'account_id': t.account_id,
        'lock_version': t.lock_version,
        'transactions': [{
            'transaction_catalog_item_id': item.transaction_catalog_item_id,
            'balance': item.balance
        } for item in t.transactions]
    }
    return result
