from utility_functions import algo_client_connection
from send import send_configured_transaction
from algosdk.future.transaction import AssetConfigTxn
from account_details import accounts

algod_client = algo_client_connection()

asa_creator = accounts[0]
total = 1000
asa_unit_name = "tasa"
asa_name = "Test ASA"

params = algod_client.suggested_params()

transaction = AssetConfigTxn(
    sender=asa_creator["address"],
    sp=params,
    total=total,
    default_frozen=False,
    unit_name=asa_unit_name,
    asset_name=asa_name,
    manager=asa_creator["address"],
    reserve=asa_creator["address"],
    freeze=asa_creator["address"],
    clawback=asa_creator["address"],
    url="https:www.info.com",
    strict_empty_address_check=False,
    decimals=0
)

signed_transaction = transaction.sign(asa_creator["private_key"])

confirmed_transaction = send_configured_transaction(algod_client, signed_transaction)