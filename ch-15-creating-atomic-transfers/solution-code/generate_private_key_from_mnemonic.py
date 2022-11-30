from algosdk import account, mnemonic, logic
from account_details import accounts

for account in accounts:
    private_key = mnemonic.to_private_key("")
    print(f"\"private_key\": \"{private_key}\",")