from algosdk.future.transaction import AssetTransferTxn, calculate_group_id


def configure_asa_transfer_transaction(algod_client, transaction_args ):
    params = algod_client.suggested_params()

    transaction = AssetTransferTxn(
        sp=params,
        amt=transaction_args["amount"],
        index=transaction_args["asset_id"],
        sender=transaction_args["sender"]["address"],
        receiver=transaction_args["receiver"]["address"],
    )

    return transaction

def configure_an_atomic_transfer(unsigned_transactions, transaction_signers):

    # Obtaining a group id and assign it to each transaction
    # Expects a list of arguments
    transaction_group_id = calculate_group_id(unsigned_transactions)

    index = 0

    # Will be used to group the signed Txns
    signed_transactions = []

    for transaction in unsigned_transactions:
        # Adding Group ID to each Txn
        transaction.group = transaction_group_id

        # Signing each Txn
        signed_transaction = transaction.sign(transaction_signers[index]['private_key'])
        index+=1

        # Grouping the signed Txns
        signed_transactions.append(signed_transaction)


    # Returning the signed Txns
    return signed_transactions