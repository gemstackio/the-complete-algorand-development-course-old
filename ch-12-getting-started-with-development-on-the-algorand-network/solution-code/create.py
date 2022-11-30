from algosdk import account, mnemonic

def create_an_algorand_account():
    private_key, address = account.generate_account()
    passphrase = mnemonic.from_private_key(private_key)

    account_details = {
        "address": address,
        "private_key": private_key,
        "passphrase": passphrase
    }

    print(account_details)