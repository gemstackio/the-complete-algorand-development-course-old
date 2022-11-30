from connect import algo_client_connection
from create import create_an_algorand_account
from check import check_account_balance
from build import build_unsigned_transaction
from send import send_a_transaction
from account_details import accounts

algo_client = algo_client_connection()

create_an_algorand_account()

check_account_balance(algo_client,  accounts[1]["address"])

sender_address = accounts[1]["address"]
senders_private_key = accounts[1]["private_key"]

receiver_address=  accounts[0]["address"]

amount = 1000000
note =  "Account 1 is sending 1 Algo to account 2"


unsigned_transaction = build_unsigned_transaction(algo_client, sender_address, amount, receiver_address, note)


send_a_transaction(algo_client, unsigned_transaction, senders_private_key, amount)