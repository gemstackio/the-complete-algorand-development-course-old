from algosdk.future import transaction
from algosdk import constants

def build_unsigned_transaction(algo_client, sender_address, amount, receiver_address, note):

    params = algo_client.suggested_params()

    # print(vars(params))

    params.flat_fee = True

    params.fee = constants.MIN_TXN_FEE

    unsigned_txn = transaction.PaymentTxn(sender_address, params, receiver_address, amount, None, note)

    return unsigned_txn