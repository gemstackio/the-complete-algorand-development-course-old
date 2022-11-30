def check_account_balance(algod_client, address):

    account_info = algod_client.account_info(address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")