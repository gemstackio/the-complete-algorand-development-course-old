from account_details import accounts
from utility_functions import algo_client_connection
from freeze import configure_and_execute_asa_freeze_transaction
from delete import configure_and_execute_asa_deletion_transaction

algod_client = algo_client_connection()

asset_id = 116981431


params = algod_client.suggested_params()

freeze_transaction_args = {
    "params": params,
    "asset_id": asset_id,
    "sender": accounts[0],
    "target": accounts[1],
    "new_freeze_state": False
}

# configure_and_execute_asa_freeze_transaction(algod_client, freeze_transaction_args)

asset_to_be_deleted_id = 116983968

delete_transaction_args = {
    "params": params,
    "asset_id": asset_id,
    "sender": accounts[0]
}

configure_and_execute_asa_deletion_transaction(algod_client, delete_transaction_args)