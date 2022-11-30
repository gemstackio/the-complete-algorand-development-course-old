from algosdk.future.transaction import AssetFreezeTxn
from send import send_configured_transaction

def configure_and_execute_asa_freeze_transaction(algod_client, freeze_transaction_args):
    unsigned_freeze_transaction = AssetFreezeTxn(
        sp=freeze_transaction_args["params"],
        index=freeze_transaction_args["asset_id"],
        sender=freeze_transaction_args['sender']["address"],
        target=freeze_transaction_args["target"]["address"],
        new_freeze_state=freeze_transaction_args['new_freeze_state']
    )

    signed_freeze_transaction = unsigned_freeze_transaction.sign(freeze_transaction_args["sender"]["private_key"])

    confirmed_freeze_transaction = send_configured_transaction(algod_client, signed_freeze_transaction)
