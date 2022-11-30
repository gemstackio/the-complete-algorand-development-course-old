from account_details import accounts
from utility_functions import algo_client_connection, print_asset_details
from create_transaction import create_asset_transaction
from send import send_configured_transaction

algod_client = algo_client_connection()

transaction = create_asset_transaction(algod_client)

signed_transaction = transaction.sign(accounts[0]['private_key'])

confirmed_transaction = send_configured_transaction(algod_client, signed_transaction)

asset_id = confirmed_transaction["asset-index"]

print_asset_details(algod_client, asset_id, accounts[0]['address'])