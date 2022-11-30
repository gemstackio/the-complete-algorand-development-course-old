from algosdk.future.transaction import AssetConfigTxn
from account_details import accounts

def configure_transaction_to_update_asset(algod_client, asset_id,current_asset_manager ):
    params = algod_client.suggested_params()

    transaction = AssetConfigTxn(
        # Sender of the transaction **must be** the currently listed `manager`
        sender= current_asset_manager['address'],
        sp=params,
        index=asset_id,
        manager=accounts[0]['address'],
        reserve="",
        freeze="",
        clawback="",
        strict_empty_address_check= False
    )

    return transaction