from algosdk.future.transaction import AssetConfigTxn
from send import send_configured_transaction

def configure_and_execute_asa_deletion_transaction(algod_client, delete_transaction_args):
    unsigned_transaction = AssetConfigTxn(
        sp=delete_transaction_args["params"],
        index=delete_transaction_args["asset_id"],
        sender=delete_transaction_args["sender"]["address"],
        strict_empty_address_check= False,
    )

    signed_transaction = unsigned_transaction.sign(delete_transaction_args["sender"]["private_key"])

    confirmed_deletion_transaction = send_configured_transaction(algod_client, signed_transaction)

    return confirmed_deletion_transaction