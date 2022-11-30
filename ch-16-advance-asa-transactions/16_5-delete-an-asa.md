<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 16.5: Revoke an ASA

In this section we will build a functionality that creates, configures, signs, and executes a transaction that deletes a specific ASA being held in a provided wallet address.

Created assets can be destroyed only by the asset manager account. All of the assets must be owned by the creator of the asset before the asset can be deleted.

## Learning Objective

By the end of this section student should be able to develop logic that configures and executes an ASA deletion transaction.

## Configure The Transaction
1. Created a new file called `delete.py`:
```sh
touch delete.py
```
2. Add the following import to `delete.py`:
```python
# delete.py

from algosdk.future.transaction import AssetConfigTxn
from send import send_configured_transaction
```
3. Within `delete.py` create a function called `configure_and_execute_asa_deletion_transaction()`
   * It should accept three arguments:
     1. `algod_client`
     2. `delete_transaction_args`
```python
# delete.py
# ...

def configure_and_execute_asa_deletion_transaction(algod_client, delete_transaction_args):
```
4. Then create a variable called `unsigned_transaction` which will set equal to an instance of the `AssetConfigTxn` class:
```python
# delete.py
# ...

def configure_and_execute_asa_deletion_transaction(algod_client, asset_id, asset_creator):
    # ...

    unsigned_transaction = AssetConfigTxn()
```
5. Next we will set the `sp` and `index`
```python
# delete.py
# ...

def configure_and_execute_asa_deletion_transaction(algod_client, asset_id, asset_creator):
    # ...

    transaction = AssetConfigTxn(
        sp=delete_transaction_args["params"],
        index=delete_transaction_args["asset_id"],
    )
```
6. Now set the `sender` of the transaction equal to the current asset managers address:
```python
# delete.py
# ...

def configure_and_execute_asa_deletion_transaction(algod_client, asset_id, asset_creator):
    # ...

    transaction = AssetConfigTxn(
        # ...

        sender=delete_transaction_args["sender"]["address"],

    )
```
7. Next we will set the `strict_empty_address_check` = `False`, you must set this or you will receive an error:
```python
# delete.py
# ...

def configure_and_execute_asa_deletion_transaction(algod_client, asset_id, asset_creator):
    # ...

    transaction = AssetConfigTxn(
        # ...
        strict_empty_address_check= False,
    )
```

## Sign The transaction
1. Create a variable called `signed_deletion_transaction` which store an expression that signs the transaction:
```python
# delete.py
# ...

def configure_and_execute_asa_deletion_transaction(algod_client, delete_transaction_args):
    # ...

    signed_transaction = unsigned_transaction.sign(delete_transaction_args["sender"]["private_key"])
```
2. Finally have to send the transaction `signed_deletion_transaction` and have the function return it:
```python
# delete.py
# ...

def configure_and_execute_asa_deletion_transaction(algod_client, delete_transaction_args):
    # ...

    confirmed_deletion_transaction = send_configured_transaction(algod_client, signed_transaction)

    return confirmed_deletion_transaction
```

## Execute The Transaction

1. open the `main.py` file and import the `configure_and_execute_asa_deletion_transaction()` function:
```python
# main.py
# ...
from delete import configure_and_execute_asa_deletion_transaction

# ...
```

2. Now create a new variable to hold the address for the ASA we want to delete:
```python
# main.py
# ...

asset_to_be_deleted_id = 116983968

# ...
```
3. Then created a variable called `delete_transaction_args` which stores the following:
```python
# main.py
# ...

delete_transaction_args = {
    "params": params,
    "asset_id": asset_to_be_deleted_id,
    "sender": accounts[0]
}
```
4. Then invoke the `configure_and_execute_asa_deletion_transaction()` function and pass it the required arguments:
```python
# main.py
# ...

configure_and_execute_asa_deletion_transaction(algod_client, delete_transaction_args)
```
5. Finally, run the code:
```sh
python3 main.py
```
6. If you check the [AlgoExplorer](https://testnet.algoexplorer.io/) you will see that the ASA now has a transaction that states it was deleted. You will still be able to access the ASA information via the AlgoExplorer.
7. But if you attempt to transfer or interaction with the ASA you will receive an error stating that the ASA has been deleted.