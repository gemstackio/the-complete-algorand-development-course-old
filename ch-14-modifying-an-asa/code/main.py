from account_details import accounts
from utility_functions import algo_client_connection, print_asset_info
from configure import configure_transaction_to_update_asset
from send import send_configured_transaction

# Initialize an algod client
algod_client = algo_client_connection()

# Modify An Assets information
# You are only able to modify an assets manager, reserve, freeze and/or clawback account information can be


# Configure the Transaction
# You must provide the id for the asset you want to modify
asset_id = 106515079

asset_manager = accounts[0]

transaction = configure_transaction_to_update_asset(algod_client, asset_id, asset_manager)

# The transaction must be signed by the currently listed `manager`
signed_transaction = transaction.sign(asset_manager['private_key'])

# Sending Transaction
send_configured_transaction(algod_client, signed_transaction)


print_asset_info(algod_client, asset_manager, asset_id)