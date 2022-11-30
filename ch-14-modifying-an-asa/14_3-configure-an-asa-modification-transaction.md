<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 14.3: Configure an ASA Update Transaction

## What We Are Going To Do

In this section we will build a function to that will configure a transaction to change the `Manager` and `Reserve` address of an existing ASA.

## Learning Objective

By the end of this section student should be able to

## Getting Started
1. Open the `main.py` and create a variable called `asset_id` and set it's value equals to the id of the asset we created in the last chapter:
   * You can also go to the [AlgoExplorer](https://testnet.algoexplorer.io/) and search the wallet address that you used to create an ASA and grab the ID from there
```python
# main.py
# ...

asset_id = 108157012
```
2. Then created another variable called `asset_manager` and set it equal to the account that you used to create the asset in the last chapter:
```python
# main.py
# ...

asset_manager = accounts[1]
```
3. Then created one more variable called `accounts_for_transaction` this will store a dictionary of all the account information we would like to modify in our transaction:
```python
# main.py
# ...
accounts_for_transaction = {
    "current_manager": asset_manager["address"],
    "new_manager": accounts[0]["address"],
    "new_reserve": "",
    "new_freeze": "",
    "new_clawback": ""
}
```
4. Now created a new file called `configure.py`:
```sh
touch configure.py
```
4. Add the following imports to `configure.py`:
```python
# configure.py

from algosdk.future.transaction import AssetConfigTxn
```
5. Within `configure.py` create a function called `configure_transaction_to_update_asset()`
   * It should accept three arguments:
     1. `algod_client`
     2. `asset_id`
     3. `accounts_for_transaction`:
```python
# configure.py
# ...

def configure_transaction_to_update_asset(algod_client, asset_id, accounts_for_transaction ):
```
5. Next add a variable called `params` which stores the suggested params:
```python
# configure.py
# ...

def configure_transaction_to_update_asset(algod_client, asset_id, accounts_for_transaction ):
    params = algod_client.suggested_params()
```
6. Then create a variable called `transaction` which will set equal to an instance of the `AssetConfigTxn` class:
```python
# configure.py
# ...

def configure_transaction_to_update_asset(algod_client, asset_id,accounts_for_transaction ):
    # ...

    transaction = AssetConfigTxn()
```
7. Then we will set the `sender` of the transaction to the current asset manager of the asset:
```python
# configure.py
# ...

def configure_transaction_to_update_asset(algod_client, asset_id,accounts_for_transaction ):
    # ...

    transaction = AssetConfigTxn(
        # Sender of the transaction **must be** the currently listed `manager`
        sender= accounts_for_transaction['current_manager'],
    )
```
8. Next we will set the:
   1. `sp` = `params`
   2. `index` = `asset_id`
```python
# configure.py
# ...

def configure_transaction_to_update_asset(algod_client, asset_id,accounts_for_transaction ):
    # ...

    transaction = AssetConfigTxn(
        # ...
        sp=params,
        index=asset_id,
    )
```
9.  Now we can provide a new `manager` address
```python
# configure.py
# ...

def configure_transaction_to_update_asset(algod_client, asset_id,accounts_for_transaction ):
    # ...

    transaction = AssetConfigTxn(
        # ...
        manager=accounts_for_transaction["new_manager"],
        reserve=accounts_for_transaction["new_reserve"],
        freeze=accounts_for_transaction["new_freeze"],
        clawback=accounts_for_transaction["new_clawback"],
    )
```
10. Note that we could update the `reserve`, `freeze`, or `clawback` at this time if we would like
11. Next we will set the:
   1. `strict_empty_address_check` = `False`
```python
# configure.py
# ...

def configure_transaction_to_update_asset(algod_client, asset_id,accounts_for_transaction ):
    # ...

    transaction = AssetConfigTxn(
        # ...
        strict_empty_address_check= False,
    )
```
12. Next have the function return the `transaction` variable:
```python
# configure.py
# ...

def configure_transaction_to_update_asset(algod_client, asset_id, accounts_for_transaction ):
    # ...

    return transaction
```
8. Then open the `main.py` file and import the `configure_transaction_to_update_asset()` function:
```python
# main.py
# ...
from configure import configure_transaction_to_update_asset

# ...
```
9. Finally, within the `main.py` file create a variable called `transaction` and set it equal to the `configure_transaction_to_update_asset()` function:
```python
# main.py
# ...

# ...
transaction = configure_transaction_to_update_asset(algod_client, asset_id, accounts_for_transaction)
```
10. Next up we will look at how to sign and send out transaction