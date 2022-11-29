from algosdk.future.transaction import wait_for_confirmation
from utility_functions import format_json_data


def send_configured_transaction(algod_client, signed_transaction):
    try:
        transaction_id = algod_client.send_transaction(signed_transaction)

        print("Transaction ID:", transaction_id)
        print("|--------------------------------|")

        confirmed_transaction = wait_for_confirmation(algod_client, transaction_id, 4)

        print(f"Transaction information: {format_json_data(confirmed_transaction, True)}")
        print("|--------------------------------|")

    except Exception as err:
        print(err)
        print("|--------------------------------|")