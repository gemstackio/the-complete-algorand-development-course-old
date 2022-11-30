from algosdk.future.transaction import AssetTransferTxn
from send import send_configured_transaction

def configure_and_execute_asa_revocation_transaction(algod_client, revoke_transaction_args ):
    unsigned_transaction = AssetTransferTxn(
        sp=revoke_transaction_args["params"],
        amt=revoke_transaction_args["amount"],
        index=revoke_transaction_args["asset_id"],
        sender=revoke_transaction_args['sender']["address"],
        revocation_target=revoke_transaction_args["revocation_target"]["address"],
        receiver=revoke_transaction_args["receiver"]["address"]
    )

    signed_transaction = unsigned_transaction.sign(revoke_transaction_args["sender"]["private_key"])

    confirmed_deletion_transaction = send_configured_transaction(algod_client, signed_transaction)

    return confirmed_deletion_transaction