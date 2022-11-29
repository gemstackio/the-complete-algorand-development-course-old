# Send an ASA Configuration Transaction

## What We Are Going To Do

In this section we will learn how to start

## Learning Objective

By the end of this section student should be able to

## Getting Started
1. First we need to sign the transaction that our `create_asset_transaction()` function returns:
```python
# main.py
# ...

signed_transaction = transaction.sign(accounts[0]['private_key'])
```
2. Next, create a file called `send.py`:
```sh
touch send.py;
```
3. Added the following import:
```python
# send.py
from algosdk.future.transaction import wait_for_confirmation
```
4. Next create function called `send_configured_transaction()` which accepts an instance of an algo client and a signed transaction as arguments:
5. Once the transaction is created we must sign it:
```python
# create_asset.py
# ...

def send_configured_transaction(algod_client, signed_transaction):
```
6. Within the `send_configured_transaction()` function create a `try except` statement:
```python
# create_asset.py
# ...

def send_configured_transaction(algod_client, signed_transaction):
    try:
        transaction_id = algod_client.send_transaction(signed_transaction)

        print("Signed transaction with txID: {}".format(transaction_id))
        print("|--------------------------------|")

        confirmed_transaction = wait_for_confirmation(algod_client, transaction_id, 4)

        print("Transaction ID:", transaction_id)
        print("|--------------------------------|")

        return confirmed_transaction

    except Exception as err:
        print(err)
        print("|--------------------------------|")
```
1. Then back in the `main.py` file created a variable called `confirmed_transaction` which stores the returned value of the `send_configured_transaction()` function:
```python
# main.py
# ...

confirmed_transaction = send_configured_transaction(algod_client, signed_transaction)
```
8. Finally, run the code and explain the output
```sh
python3 main.py
```
* **Thing to remember is that this output is exactly what you will get when you run the print_asset_details() function in the next lesson**
* Also be sure to save your Asset ID somewhere for later