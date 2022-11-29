from algosdk.v2client import algod

def algo_client_connection():
    # connect to the node
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    # client = algod.AlgodClient(algod_token, algod_address)
    # print(client.status())

    # return client
    return algod.AlgodClient(algod_token, algod_address)