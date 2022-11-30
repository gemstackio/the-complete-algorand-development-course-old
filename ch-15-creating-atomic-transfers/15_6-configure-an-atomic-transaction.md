# 15.6: Configure An Atomic Transfer

In the last video we were able to set up our logic that creates an unsigned opt-in transaction.

In this video we will develop logic that allows us to group a ASA opt-in and ASA transfer transactions into a single Atomic Transfer.

`Atomic Transfers` allow you to group transaction that either all succeed or fail. In our current use-case we want to execute two transaction together:
1. That opts an account into a specific ASA
2. A transaction that transfers a specified amount of ASAs from a creators account to a receivers account.

## Learning Objective

By the end of this section student should be able to

## Develop Logic to Configure an Atomic Transfer Transaction

1. Now that we have our two unsigned transactions we can start to configure our `Atomic Transfer`
2. Create a new function called `configure_an_atomic_transfer()` that accepts two arguments `unsigned_transactions` and `transaction_signers`:
```python
# configure.py
# ...

def configure_an_atomic_transfer(unsigned_transactions, transaction_signers):
```
3. Now and the `calculate_group_id()` method to the imports from `algosdk.future.transaction`
```diff
# configure.py
- from algosdk.future.transaction import AssetTransferTxn
+ from algosdk.future.transaction import AssetTransferTxn, calculate_group_id

# ...
```
4. We will utilize the `calculate_group_id()` to assign our entire Atomic Transfer a single ID which is called the `group id`:
```python
# configure.py
# ...

def configure_an_atomic_transfer(unsigned_transactions, transaction_signers):
    transaction_group_id = calculate_group_id(unsigned_transactions)
```
5. Once created we will then add `group id` to each transactions group property, we will do this by iterating over the `unsigned_transactions` we pass in as parameters:
```python
# configure.py
# ...

def configure_an_atomic_transfer(unsigned_transactions, transaction_signers):
    # ...
    for transaction in unsigned_transactions:
        transaction.group = transaction_group_id
```
6. Now we need to sign each transaction. Above the `for loop` create two new variable `index` and `signed_transactions`:
```python
# configure.py
# ...

def configure_an_atomic_transfer(unsigned_transactions, transaction_signers):
    # ...
    index = 0

    signed_transactions = []

    for transaction in unsigned_transactions:
        # ...
```
7. Now within the `for loop` create a variable called `signed_transaction` and have it store the signed transaction. We will use the `index` variable to access the `transaction_signer`'s `private key`:
```python
# configure.py
# ...

def configure_an_atomic_transfer(unsigned_transactions, transaction_signers):
    # ...

    for transaction in unsigned_transactions:
        # ...
        signed_transaction = transaction.sign(transaction_signers[index]['private_key'])

        index+=1
```
8. Next we need to append the `signed_transaction` to the `signed_transactions` list:
```python
# configure.py
# ...

def configure_an_atomic_transfer(unsigned_transactions, transaction_signers):
    # ...

    for transaction in unsigned_transactions:
        # ...
        signed_transactions.append(signed_transaction)
```
9. Finally have the function return the `signed_transactions` list:
```python
# configure.py
# ...

def configure_an_atomic_transfer(unsigned_transactions, transaction_signers):
    # ...
    index = 0

    signed_transactions = []

    for transaction in unsigned_transactions:
        # ...
    return signed_transactions

```

## Configure an Atomic Transfer

1.  Now open the `main.py` and `configure_an_atomic_transfer()` function to the `configure.py` import:
```diff
# main.py
# ...
- from configure import configure_asa_transfer_transaction
+ from configure import configure_asa_transfer_transaction, configure_an_atomic_transfer
```
2. Within the `if statement` create a two new variables `unsigned_transactions` and `transaction_signers`:
```python
# main.py
# ...

if not opted_in:
    # ...

    unsigned_transactions = [unsigned_opt_in_transaction, unsigned_asa_transfer_transaction]

    transaction_signers = [account_opting_in, asa_creator]
```
3. Create another variable called `signed_atomic_transfer` and set it equal to the `configure_an_atomic_transfer()` and pass it the required arguments:
```python
# main.py
# ...

if not opted_in:
    # ...
    signed_atomic_transfer = configure_an_atomic_transfer(unsigned_transactions, transaction_signers)
```
4. In the next video we will develop logic that allows us to send our `Atomic Transfer`.