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