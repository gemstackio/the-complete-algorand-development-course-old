# Create and Configure an ASA Transaction

## What We Are Going To Do

In this section we learn how to configure a transaction to create a ASA.

## Learning Objective

By the end of this section student should be able to configure a transaction to create a ASA

## Getting Started
1. Inside the `chapter-<PROVIDE THE PROPER-CHAPTER-NUMBER>` create a file called `create_transaction.py`:
```sh
touch create_transaction.py;
```
2. Added the following imports:
```python
# create_transaction.py
from algosdk.future.transaction import AssetConfigTxn
from account_details import accounts
```
3. Next create function called `create_asset_transaction()`, it should accept an instance of an algo client as an argument:
```python
# create_transaction.py
# ...

def create_asset_transaction(algod_client):
```
4. Then establish some default params:
```python
# create_transaction.py
# ...

def create_asset_transaction(algod_client):
    params = algod_client.suggested_params()
```
5. Next create a variable called `transaction` which represents a transaction for asset creation:
```python
# create_transaction.py
# ...

def create_asset_transaction(algod_client):
    # ...

    transaction = AssetConfigTxn(
        sender=,
        sp=,
        total=,
        default_frozen=,
        unit_name=,
        asset_name=,
        manager=,
        reserve="",
        freeze="",
        clawback="",
        url=,
        strict_empty_address_check=,
        decimals=
    )
```
6. Now we have to provide the actual configuration information:
```python
# create_transaction.py
# ...

def create_asset_transaction(algod_client):
    # ...

    transaction = AssetConfigTxn(
        sender=accounts[0]['address'],
        sp=params,
        total=1000,
        default_frozen=False,
        unit_name="CRED",
        asset_name="Galactic Credits",
        manager=accounts[1]['address'],
        reserve="",
        freeze="",
        clawback="",
        url="https:www.info.com",
        strict_empty_address_check=False,
        decimals=0
    )

    return transaction
```
7. Finally we need to return the newly created asset transaction:
```python
# create_transaction.py
# ...

def create_asset_transaction(algod_client):
    # ...

    return transaction
```
8. Now open the `main.py` file and import the following:
```python
# main.py
from account_details import accounts
from utility_functions import algo_client_connection, print_asset_details
from create_transaction import create_asset_transaction
```
9. Instantiate an instance of the algo client:
```python
# main.py
# ...

algod_client = algo_client_connection()
```
10. Finally, create a variable called `transaction` which stores the return value of the `create_asset_transaction()` function:
```python
# main.py
# ...

transaction = create_asset_transaction(algod_client)
```