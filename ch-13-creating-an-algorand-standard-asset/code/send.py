from algosdk.future.transaction import wait_for_confirmation
import json


def send_configured_transaction(algod_client, signed_transaction):
    try:
        transaction_id = algod_client.send_transaction(signed_transaction)

        print("Transaction ID:", transaction_id)
        print("|--------------------------------|")

        confirmed_transaction = wait_for_confirmation(algod_client, transaction_id, 4)

        print(f"Transaction information: {json.dumps(confirmed_transaction, indent=4)}")
        print("|--------------------------------|")

        return confirmed_transaction

    except Exception as err:
        print(err)
        print("|--------------------------------|")