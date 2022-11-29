# Send a Transaction

## What We Are Going To Do
In this section we are going to build out a feature that allows us to take an unsigned transaction and send it.

## Build It
1. Navigate to your `algo-course-walkthrough` directory:
```sh
cd ~/<PATH TO>/algo-course-walkthrough;
```
2. Create a `send.py` file:
```sh
touch send.py;
```
3. Open the project within your text editor:
```sh
code .;
```
4. Then import the required modules:
```python
# send.py

from algosdk.future import transaction
import json
import base64
```
5. Next, declare a method called `send_a_transaction()`
```python
# send.py

def send_a_transaction():
```
6. The method should accept 4 parameters; `algo_client`, `unsigned_txn`, `private_key`, and `amount`:
```python
# send.py

def send_a_transaction(algo_client, unsigned_transaction, private_key, amount):
```
7. Then, we will create a variable called `signed_transaction` which will store and an expression that signs the `unsigned_transaction`:
```python
# send.py

def send_a_transaction(algo_client, unsigned_transaction, private_key, amount):
    signed_transaction = unsigned_transaction.sign(private_key)
```
8. We will now create a variable called `submitted_transaction_id` which will store the id of the transaction we are going to submit
```python
# send.py

def send_a_transaction(algo_client, unsigned_transaction, private_key, amount):
    # ...
    submitted_transaction_id = algo_client.send_transaction(signed_transaction)
```
9. After which, we will write the following print statement:
```python
# send.py

def send_a_transaction(algo_client, unsigned_transaction, private_key, amount):
    # ...
    print("Successfully sent transaction. Transaction ID: {}".format(submitted_transaction_id))
```
10.  Next, we will create a `try` statement which wait for the transaction to be confirmed to the network:
```python
# send.py

def send_a_transaction(algo_client, unsigned_transaction, private_key, amount):
    # ...
    try:
        confirmed_transaction = transaction.wait_for_confirmation(algo_client, submitted_transaction_id, 4)
```
11. Add the following `exception` statement to the `try` statement:
```python
# send.py

def send_a_transaction(algo_client, unsigned_transaction, private_key, amount):
    # ...
    try:
        confirmed_transaction = transaction.wait_for_confirmation(algo_client, submitted_transaction_id, 4)
    except Exception as err:
        print(err)
        return
```
12. The last thing we will do is add three `print` statements so that we are able to output some information about a completed transaction:
```python
# send.py

def send_a_transaction(algo_client, unsigned_transaction, private_key, amount):
    # ...
    print("Transaction information: {}".format(json.dumps(confirmed_transaction, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(confirmed_transaction["txn"]["txn"]["note"]).decode()))
    print("Amount transferred: {} microAlgos".format(amount))
```
### Code Explanation
In step 6, we declare four parameters for the method to expect:
1.  `algo_client`: provides a connection to our Algorand node
2.  `unsigned_txn`: should store the unsigned transaction returned from our `build_unsigned_transaction()` method
3.  `private_key`: is the private key for the wallet that created this transaction
4.  `amount`: the total amount of algos being sent in this transaction

In step 7, we create a variable called `signed_transaction`. Within this variable we place an expression that takes the `unsigned_transaction` and utilize the `sign()` method to sign the transaction with the senders private key.

In step 8, the `submitted_transaction_id` variable will contain an expression that utilize the `algo_client`'s `send_transaction()` method to broadcast the signed transaction to the network. The `send_transaction()` method returns the id that the networks associates with the transaction.

In step 9, we print the `submitted_transaction_id` to verify that the transaction was submitted properly.

In step 10, we create a `try` statement which will wait a specific amount of voting rounds for the submitted transaction to be verified by the network. Within the `try` statement we create a variable called `confirmed_transaction` which stores an expression that utilizes the `transaction` module that was imported in step 4. We then utilize the `transaction` modules `wait_for_confirmation()` method which is what allows our program to wait until the transaction is confirmed by the network.

`wait_for_confirmation` accepts three parameter:
1. `algo_client`: an instance of the algod client
2. `txid`: transaction ID
3. `wait_rounds`: (optional) – The number of rounds to block for before exiting with an Exception. If not supplied, this will be 1000.

In step 11, we add an `except` statement that is thrown if the transaction is not confirmed within the amount of rounds dictated in the `wait_for_confirmation()` method.

In step 12, we create 3 print statements:
1. `print("Transaction information: {}".format(json.dumps(confirmed_transaction, indent=4)))` - prints the json data that is stored within the `confirmed_transaction` variable.
2. `print("Decoded note: {}".format(base64.b64decode(confirmed_transaction["txn"]["txn"]["note"]).decode()))` - converts the note we provided the transaction with the `base64` module and prints it.
3. `print("Amount transferred: {} microAlgos".format(amount))` - prints the total number of algos sent in the transaction

## Test It
1. Open the `main.py` file:
2. Next, verify you have the following code within the `main.py` file:
```python
# main.py

from connect import algo_client_connection
from build import build_unsigned_transaction

algo_client = algo_client_connection()

sender_address = "<Wallet Address>"
senders_private_key = "<Private Key>"

receiver_address=  "<Another Wallet Address>"

amount = 1000000
note =  "Account 1 is sending 1 Algo to account 2"

unsigned_transaction = build_unsigned_transaction(algo_client, sender_address, amount, receiver_address, note)
```
3. Then import the `send_a_transaction` from the `send` module:
```python
# main.py

# ...
from send import send_a_transaction

# ...
```
4. Next, invoke the `send_a_transaction()` method:
```python
# main.py

# ...
from send import send_a_transaction

# ...
send_a_transaction(algo_client, unsigned_transaction, senders_private_key, amount)
```
4. Run the program:
```sh
python3 main.py
```
5. The program should output information that looks similar to the following:
```sh
Successfully sent transaction. Transaction ID: Q2FDHAGLGCLKBFFPOW5I7QJBIYXNXOOYOBJUDDCDEZYI2S5A7YPA
Transaction information: {
    "confirmed-round": 22773333,
    "pool-error": "",
    "txn": {
        "sig": "fIxqpHaDcWezAXgklXfO5ze09Cd2d5lQqsT7MSPxsqdBrDZIcMV9cozBXP63gdw5RhU/TsyQdDaOxeuP+RgsDA==",
        "txn": {
            "amt": 1000000,
            "fee": 1000,
            "fv": 22773331,
            "gen": "testnet-v1.0",
            "gh": "SGO1GKSzyE7IEPItTxCByw9x8FmnrCDexi9/cOUJOiI=",
            "lv": 22774331,
            "note": "QWNjb3VudCAxIGlzIHNlbmRpbmcgMSBBbGdvIHRvIGFjY291bnQgMg==",
            "rcv": "ABZAFLZPC7RHE4PZT6DSATH57BRCAHW3JBCZVHB35MQMGA7HX5YR3O3ZGA",
            "snd": "WKWDH6WDQTNMJ6BISNYKT2PJYK5H5PN6ACZXMJAWR3G3XPOXTRD7MNY2AU",
            "type": "pay"
        }
    }
}
Decoded note: Account 1 is sending 1 Algo to account 2
Amount transferred: 1000000 microAlgos
```

### Code Explanation