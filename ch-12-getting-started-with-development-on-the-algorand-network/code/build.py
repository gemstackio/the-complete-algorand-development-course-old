from algosdk.future import transaction
from algosdk import constants

def build_unsigned_transaction(algo_client, sender_address, amount, receiver_address, note):

    # build unsigned transaction
    params = algo_client.suggested_params()

    # Allows us to show what params stores
    # print(vars(params))

    # Set Transaction Fee
    params.flat_fee = True

    # setting fee to minimum required amount
    params.fee = constants.MIN_TXN_FEE

    # building the unsigned transaction
    unsigned_txn = transaction.PaymentTxn(sender_address, params, receiver_address, amount, None, note)

    return unsigned_txn