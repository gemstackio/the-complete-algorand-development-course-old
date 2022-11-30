# 15.5: Configure an ASA Transfer Transactions

In this video we will develop logic that utilizes the `AssetTransferTxn` class to create two different ASA transfer transactions:
1. `Opt-In`: a 0 balance ASA transfer to and from the account that wants to opt-in to receive a specific ASA.
2. `ASA Transfer`: the transaction that will actually send a specific amount of ASA from the ASA creator account to the intended receiver; ie: the account that opted-in.

## Learning Objective

By the end of this section student should be able to

## Develop the ASA Transfer Configuration Logic
1. Created a new file called `configure.py`:
```sh
touch configure.py
```
2. Add the following import to `configure.py`:
```python
# configure.py

from algosdk.future.transaction import AssetTransferTxn
```
3. Within `configure.py` create a function called `configure_asa_transfer_transaction()`
   * It should accept two arguments: `algod_client` and `transaction_args`
```python
# configure.py
# ...

def configure_asa_transfer_transaction(algod_client, transaction_args ):
```
4. Next add a variable called `params` which stores the suggested params:
```python
# configure.py
# ...

def configure_asa_transfer_transaction(algod_client, transaction_args ):
    params = algod_client.suggested_params()
```
5. Then create a variable called `transaction` which will set equal to an instance of the `AssetTransferTxn` class:
```python
# configure.py
# ...

def configure_asa_transfer_transaction(algod_client, transaction_args ):
    # ...

    transaction = AssetTransferTxn()
```
6. Next we will set the:
   1. `sp` = `params`
   2. `amt` = `transaction_args["amount"]`
   3. `index` = `transaction_args["asset_id"]`
```python
# configure.py
# ...

def configure_asa_transfer_transaction(algod_client, transaction_args ):
    # ...

    transaction = AssetTransferTxn(
        sp=params,
        amt=transaction_args["amount"],
        index=transaction_args["asset_id"],
    )
```
7. Now set:
   * `sender` to `transaction_args["sender"]["address"]`
   * `receiver` to `transaction_args["receiver"]["address"]`:
```python
# configure.py
# ...

def configure_asa_transfer_transaction(algod_client, transaction_args ):
    # ...

    transaction = AssetTransferTxn(
        # ...
        sender=transaction_args["sender"]["address"],
        receiver=transaction_args["receiver"]["address"],
    )
```
8.  Next have the function return the `transaction` variable:
```python
# configure.py
# ...

def configure_asa_transfer_transaction(algod_client, transaction_args ):
    # ...

    return transaction
```
9. Then open the `main.py` file and import the `configure_asa_transfer_transaction()` function:
```python
# main.py
# ...
from configure import configure_asa_transfer_transaction

# ...
```
## Create the Unsigned Op-In Transaction

10. Now within the `if statement` we need to create two separate transactions:
    1. Handles the account opt-in
    2. Handles the asa transfer
11. First create a variable called `unsigned_opt_in_transaction` and set it equal to the `configure_asa_transfer_transaction()` function:
    *  This transaction will handle the actual account opt-in
```python
# main.py
# ...

    if not opted_in:
        unsigned_opt_in_transaction = configure_asa_transfer_transaction()
```
12. We now need to create set of arguments for this transaction, above the `unsigned_opt_in_transaction` create a variable called `asa_opt_transaction_args` and set it equal to the following information:
```python
# main.py
# ...

    if not opted_in:
        asa_opt_transaction_args = {
            "amount": 0,
            "asset_id": asset_id,
            "sender": account_opting_in,
            "receiver": account_opting_in
        }

        unsigned_opt_in_transaction = configure_asa_transfer_transaction()
```
13. Now pass in the required arguments `algod_client` and `asa_opt_transaction_args`:
```python
# main.py
# ...

    if not opted_in:
        asa_opt_transaction_args = {
            "amount": 0,
            "asset_id": asset_id,
            "sender": account_opting_in,
            "receiver": account_opting_in
        }

        unsigned_opt_in_transaction = configure_asa_transfer_transaction(algod_client, asa_opt_transaction_args)
```

## Create the Unsigned ASA Transfer Transaction

1. Now we need to create the ASA transfer transaction, create a variable within the `if statement` called `unsigned_asa_transfer_transaction` and set it equal to the `configure_asa_transfer_transaction()` function:
   * This transaction will handle transferring a provided amount of ASAs
```python
# main.py
# ...

    if not opted_in:
        # ...

        unsigned_asa_transfer_transaction = configure_asa_transfer_transaction()
```
2. We now need to make the transaction arguments for this transaction. Above the `if statement` create a variable called `asa_transfer_transaction_args` and set it equal to the following information:
   * With this set of arguments you have to make the sender equal to the `asa_creator`.
```python
# main.py
# ...

asa_transfer_transaction_args = {
    "amount": 1,
    "asset_id": asset_id,
    "sender": asa_creator,
    "receiver": account_opting_in
}

    if not opted_in:
        # ...

        unsigned_asa_transfer_transaction = configure_asa_transfer_transaction()
```
3. Now pass in the required arguments:
```python
# main.py
# ...

asa_transfer_transaction_args = {
    "amount": 1,
    "asset_id": asset_id,
    "sender": asa_creator,
    "receiver": account_opting_in
}

    if not opted_in:
        # ...

        unsigned_asa_transfer_transaction = configure_asa_transfer_transaction(algod_client,asa_transfer_transaction_args)
```
4. In the next video we will develop logic that allows us to sign and send our opt-in and ASA transfer transaction