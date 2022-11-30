from algosdk.future.transaction import wait_for_confirmation
from utility_functions import format_json_data

def send_configured_transaction(algod_client, signed_transaction):
    try:
        # if we send an Atomic Transfer (ie: a list of transactions)
        if type(signed_transaction) is list:
            transaction_id = algod_client.send_transactions(signed_transaction)
        # If we send a single transaction
        else:
            transaction_id = algod_client.send_transaction(signed_transaction)

        confirmed_transaction = wait_for_confirmation(algod_client, transaction_id, 4)

        print(f"Transaction information: {format_json_data(confirmed_transaction, True)}")
        print("|--------------------------------|")

        return confirmed_transaction

    except Exception as err:
        print(err)
        print("|--------------------------------|")