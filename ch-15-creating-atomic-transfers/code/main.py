from algosdk import account, mnemonic
from account_details import accounts
from send import send_configured_transaction
from utility_functions import algo_client_connection, format_json_data
from check_if import is_account_opted_in
from configure import configure_asa_transfer_transaction, configure_an_atomic_transfer

algod_client = algo_client_connection()

asset_id = 116492917

# known_asset_id = 116410004

asa_creator = accounts[0]
account_opting_in = accounts[1]

opting_in_accounts_info = algod_client.account_info(account_opting_in['address'])

opting_in_account_assets = opting_in_accounts_info["assets"]

opted_in = is_account_opted_in(opting_in_account_assets, asset_id)

asa_transfer_transaction_args = {
    "amount": 1,
    "asset_id": asset_id,
    "sender": asa_creator,
    "receiver": account_opting_in
}

if not opted_in:
    asa_opt_transaction_args = {
    "amount": 0,
    "asset_id": asset_id,
    "sender": account_opting_in,
    "receiver": account_opting_in
    }

    # Creating Unsigned Transactions:
    unsigned_opt_in_transaction = configure_asa_transfer_transaction(algod_client, asa_opt_transaction_args)

    unsigned_asa_transfer_transaction = configure_asa_transfer_transaction(algod_client,asa_transfer_transaction_args)

    # Grouping the Unsigned Transactions:
    unsigned_transactions = [unsigned_opt_in_transaction, unsigned_asa_transfer_transaction]

    # Grouping the Transaction Signers
    transaction_signers = [account_opting_in, asa_creator]

    # Creating a signed Atomic Transfer
    signed_atomic_transfer = configure_an_atomic_transfer(unsigned_transactions, transaction_signers)

    # Sending the signed Atomic Transfer
    confirmed_atomic_transfer = send_configured_transaction(algod_client, signed_atomic_transfer)

elif opted_in == True:

    unsigned_asa_transfer_transaction = configure_asa_transfer_transaction(algod_client, asa_transfer_transaction_args)

    signed__asa_transfer_transaction = unsigned_asa_transfer_transaction.sign(asa_creator['private_key'])

    confirmed_transaction = send_configured_transaction(algod_client, signed__asa_transfer_transaction)