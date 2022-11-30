from algosdk.future import transaction
import json
import base64

def send_a_transaction(algod_client, unsigned_transaction, private_key, amount):
      # signing with our private key
    signed_transaction = unsigned_transaction.sign(private_key)

    # submit transaction -> Returns the transaction ID
    submitted_transaction_id = algod_client.send_transaction(signed_transaction)

    # Print Transaction ID:
    print("Successfully sent transaction. Transaction ID: {}".format(submitted_transaction_id))

     # awaiting confirmation on transaction
    try:
        confirmed_transaction = transaction.wait_for_confirmation(algod_client, submitted_transaction_id, 4) # 4 is the number of rounds to block for before exiting with an Exception. default is 1000
    except Exception as err:
        print(err)
        return

    # print out transaction information upon success
    print("Transaction information: {}".format(json.dumps(confirmed_transaction, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(confirmed_transaction["txn"]["txn"]["note"]).decode()))
    print("Amount transferred: {} microAlgos".format(amount))