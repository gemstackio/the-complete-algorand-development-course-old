from algosdk.future.transaction import AssetConfigTxn
from account_details import accounts

def create_asset_transaction(algod_client):
    params = algod_client.suggested_params()

    transaction = AssetConfigTxn(
        sender=accounts[0]['address'],
        sp=params,
        total=1000,
        default_frozen=False,
        unit_name="CER",
        asset_name="Cera Asset",
        manager=accounts[1]['address'],
        reserve="",
        freeze="",
        clawback="",
        url="https:www.info.com",
        strict_empty_address_check=False,
        decimals=0
    )

    return transaction