<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 16.3: Freeze An ASA

In this section we will build a functionality that creates, configures, signs, and executes a transaction that freezes a specific ASA being held in a provided wallet address.

## Learning Objective

By the end of this section student should be able to configure and execute a transaction that freezes an ASA.

## Configure The Transaction
1. Created a new file called `freeze.py`:
```sh
touch freeze.py
```
2. Add the following import to `freeze.py`:
```python
# freeze.py

from algosdk.future.transaction import AssetFreezeTxn
from send import send_configured_transaction
```
1. Within `freeze.py` create a function called `configure_and_execute_asa_freeze_transaction()`, which accepts `algod_client` and `freeze_transaction_args` as parameters:
```python
# freeze.py
# ...

def configure_and_execute_asa_freeze_transaction(algod_client, freeze_transaction_args):
```
1. Then create a variable called `unsigned_freeze_transaction` which will set equal to an instance of the `AssetFreezeTxn` class:
```python
# freeze.py
# ...

def configure_and_execute_asa_freeze_transaction(algod_client, asset_id,accounts_for_transaction ):
    unsigned_freeze_transaction = AssetFreezeTxn()
```
6. Next we will set the `sp` and `index`
```python
# freeze.py
# ...

def configure_and_execute_asa_freeze_transaction(algod_client, asset_id,accounts_for_transaction ):
    # ...

    unsigned_freeze_transaction = AssetFreezeTxn(
        sp=freeze_transaction_args["params"],
        index=freeze_transaction_args["asset_id"],
    )
```
7. Now set the `sender` and `target` of the transaction. The asset managers address should be the sender and the account's who ASA you want to freeze should be the `target`:
```python
# freeze.py
# ...

def configure_and_execute_asa_freeze_transaction(algod_client, asset_id,accounts_for_transaction ):
    # ...

    unsigned_freeze_transaction = AssetFreezeTxn(
        # ...
        sender=freeze_transaction_args['sender']["address"],
        target=freeze_transaction_args["target"]["address"],
    )
```
1. Then we have to set the `new_freeze_state` argument to `True`:
```python
# freeze.py
# ...

def configure_and_execute_asa_freeze_transaction(algod_client, asset_id,accounts_for_transaction ):
    # ...

    unsigned_freeze_transaction = AssetFreezeTxn(
        # ...
        new_freeze_state=True
    )
```

## Sign and Return the Transaction

1. Now create a variable called `signed_freeze_transaction` which we will use to store our signed transaction:
```python
# freeze.py
# ...

def configure_and_execute_asa_freeze_transaction():
    # ...

    signed_freeze_transaction = unsigned_freeze_transaction.sign(freeze_transaction_args["sender"]["private_key"])
```
2. Then created a variable called `confirmed_transaction` which stores the returned value of the `send_configured_transaction()` function:
```python
# freeze.py
# ...
def configure_and_execute_asa_freeze_transaction():
    # ...
    confirmed_freeze_transaction = send_configured_transaction(algod_client, signed_freeze_transaction)
```
3. Now have the function return the the `confirmed_freeze_transaction`:
```python
# freeze.py
# ...
def configure_and_execute_asa_freeze_transaction():
    # ...
    return confirmed_freeze_transaction
```
## Execute The Transaction

1. Then within the `main.py` files, import and invoke the `configure_and_execute_asa_freeze_transaction` function:
```python
# main.py
# ...
from freeze import configure_and_execute_asa_freeze_transaction

# ...

configure_and_execute_asa_freeze_transaction()
```
4. Now create two variables called `params` and `freeze_transaction_args` and have it store a dictionary with the required arguments:
```python
# main.py
# ...
params = algod_client.suggested_params()

freeze_transaction_args = {
    "params": params,
    "asset_id": asset_id,
    "sender": accounts[0],
    "target": accounts[1],
    "new_freeze_state": True
}

# ...
```
5. Then pass the `algod_client` and `freeze_transaction_args` to the `configure_and_execute_asa_freeze_transaction()` function:
```python
# main.py

# ...

configure_and_execute_asa_freeze_transaction(algod_client, freeze_transaction_args)
```
6. Finally, run the code and explain the output
```sh
python3 main.py
```
5. We can verify that the ASA is not frozen by looking it up on the [AlgoExplorer](https://testnet.algoexplorer.io/)

## Attempt to Transfer Frozen ASA

1. Now open `chapter 15` and try and transfer an ASA to the account that has been frozen:
```sh
python3 ../chapter-15-atomic-transfer/main.py
```
2. You will then be provided this error:
```sh
The account is already opted-in
TransactionPool.Remember: transaction {ACCOUNT_ADDRESS}: asset frozen in recipient
```
3. This is due to the account having been frozen out of sending or receiving that particular ASA.
4. Change the account that is attempting to receive an ASA to our third account you will see that the transaction is completed without an issue:
```diff
# chapter-15-atomic-transfer/main.py
# ...
-account_opting_in = accounts[1] 
+account_opting_in = accounts[2] 
# ...
```
5. Now run the `chapter-15-atomic-transfer/main.py`:
```sh
python3 ../chapter-15-atomic-transfer/main.py
```
6. And the transaction should work.