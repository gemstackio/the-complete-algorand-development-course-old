<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 15.7 - Executing an Atomic Transfer

In the last video we developed logic that creates a `signed_atomic_transfer`. Now we need to send the Atomic Transfer to network for execution.

In this video we will update the logic within our `send_configured_transaction` to check if we are sending a single transaction or an Atomic Transfer.

Once we have completed that task we will develop logic to submit our Atomic Transfer.

We will expand our conditional logic so if an account is opted in to the specified ASA it will just create and execute a single ASA transfer transaction rather than an Atomic Transfer.

## Learning Objective

By the end of this section student should be able to

## Update the send_configured_transaction Function
1. Within the `main.py` file create a variable called `confirmed_atomic_transfer` and set it equal to the `send_configured_transaction()` function with the following arguments:
```python
# main.py
# ...
if not opted_in:
    # ...
    confirmed_atomic_transfer = send_configured_transaction(algod_client, signed_atomic_transfer)
```
2. Now open the `send.py` file and within the `try statement` add an `if statement` that checks to see if the `signed_transaction` parameter is equal to a `list`, if so we will utilize the `algod_client.send_transactions()` method
```python
# send.py
# ...

def send_configured_transaction(algod_client, signed_transaction):
    try:

        if type(signed_transaction) is list:
            transaction_id = algod_client.send_transactions(signed_transaction)
```
3. Now add an `else statement` that utilizes the original logic:
```python
# send.py
# ...

def send_configured_transaction(algod_client, signed_transaction):
    try:

        if type(signed_transaction) is list:
            # ...
        else:
            transaction_id = algod_client.send_transaction(signed_transaction)
```

## Execute an Atomic Transfer

1. Now we are actually able to execute our `Atomic Transfer`, go ahead and run the `main.py` file:
```sh
python3 main.py
```
2. Now if we check the [AlgoExplorer](https://testnet.algoexplorer.io/) we can see that the `account_opting_in` has a transaction for opting into the ASA and another transaction that transferred the specified amount of ASAs to it.

## Develop Logic to Send a Single ASA Transfer

1. Now that the `Atomic Transfer` logic is functional let's quickly add some logic that will execute an ASA transfer transaction if the `account_opting_in` is already opted-in to the ASA:
2. Underneath the `if statement` add an `elif statement` that checks to see if `opted_in` is `True`:
```python
# main.py
# ...

elif opted_in == True:
```
3. Now add logic that creates an `unsigned_asa_transfer_transaction`, signs it, and then executes it:
```python
# main.py
# ...

elif opted_in == True:

    unsigned_asa_transfer_transaction = configure_asa_transfer_transaction(algod_client, asa_transfer_transaction_args)

    signed__asa_transfer_transaction = unsigned_asa_transfer_transaction.sign(asa_creator['private_key'])

    confirmed_transaction = send_configured_transaction(algod_client, signed__asa_transfer_transaction)
```

## Execute a Single ASA Transfer Transaction

1. Now run the `main.py` file again so that the `elif` logic run:
```sh
python3 main.py
```
2. If we check the [AlgoExplorer](https://testnet.algoexplorer.io/) we can see that the `account_opting_in` has a single transaction that transferred the specified amount of ASAs to it.