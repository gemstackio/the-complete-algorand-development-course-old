from algosdk.v2client import algod
import json

def algo_client_connection():
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    algod_client = algod.AlgodClient(
        algod_token=algod_token, algod_address=algod_address)

    return algod_client


def format_json_data(data, should_return):
    """
    Helper Functions that takes json data and formats it.

    Args:
       data (string): the data to format
       should_return (bool): True returns data | False prints data
    """
    if(should_return == True):
        return json.dumps(data, indent=4)

    print(json.dumps(data, indent=4))



def print_asset_details(algod_client, asset_id,  account):
    """
    Helper Functions that prints details for a provided asset

    Args:
        algod_client: Instance of an algod client
        asset_id: The asset's ID
        account: The account that owns the asset
    """

    account_info = algod_client.account_info(account)
    index = 0

    # print(json.dumps(account_info, indent=4))

    for list_of_assets in account_info['created-assets']:
        current_asset = account_info['created-assets'][index]
        index = index + 1

        if (current_asset['index'] == asset_id):
            print(f"Asset {current_asset['index']} Details: \n {format_json_data(current_asset, True)}")

            break