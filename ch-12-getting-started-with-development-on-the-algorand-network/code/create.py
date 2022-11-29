from algosdk import account, mnemonic

def create_an_algorand_account():
    # generate the private key and an address
    private_key, address = account.generate_account()

    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))

    passphrase = mnemonic.from_private_key(private_key)

    print("My passphrase: {}".format(passphrase))