# Build a transaction

## What We Are Going To Do
In this section we are going to develop a new feature which allows us to build a new transaction. A thing to note is that this feature will not send a transaction. We will develop that logic in the next section.

## Build It
1. Navigate to your `algo-course-walkthrough` directory:
```sh
cd ~/<PATH TO>/algo-course-walkthrough;
```
2. Create a `build.py` file:
```sh
touch build.py;
```
3. Open the project within your text editor:
```sh
code .;
```
4. Import the following:
```python
# build.py

from algosdk.future import transaction
from algosdk import constants
```
5. Declare a method called `build_unsigned_transaction()`
```python
# build.py

# ...

def build_unsigned_transaction():
```
5. For now we only want the method to expect one parameter `algo_client`:
```python
# build.py

# ...

def build_unsigned_transaction(algo_client):
```
6. Next, create a variable called `params` which stores the following:
```python
# build.py
def build_unsigned_transaction(algo_client):

    params = algo_client.suggested_params()
```
7. Add the following print statement and invoke the method:
```python
def build_unsigned_transaction(algo_client):

    params = algo_client.suggested_params()

    print(vars(params))

build_unsigned_transaction(algo_client)
```
8. Let's take a look at what params stores:
```sh
python3 build.py

# outputs:
# {'first': 22709883, 'last': 22710883, 'gh': 'SGO1GKSzyE7IEPItTxCByw9x8FmnrCDexi9/cOUJOiI=', 'gen': 'testnet-v1.0', 'fee': 0, 'flat_fee': False, 'consensus_version': 'https://github.com/algorandfoundation/specs/tree/d5ac876d7ede07367dbaa26e149aa42589aac1f7', 'min_fee': 1000}
```
9. Delete the `build_unsigned_transaction()` function call and comment out the params print statement
10. Next, set the `params` `flat_fee` attribute to `True`
```py
# build.py
def build_unsigned_transaction(algo_client):
    # ...

    params.flat_fee = True
```
11. Then, lets set the `params` `fee` attribute to the minimum amount:
```py
# build.py
def build_unsigned_transaction(algo_client):
    # ...

    params.fee = constants.MIN_TXN_FEE
```
12. Now we need to add four more expected parameters to the method declaration; sender_address, amount, receiver_address, and note:
```py
# build.py
def build_unsigned_transaction(algo_client, sender_address, amount, receiver_address, note):
    # ...
```
13. Finally we will build the unsigned transaction and return it:
```py
# build.py
def build_unsigned_transaction(algo_client, sender_address, amount, receiver_address, note):
    # ...

    unsigned_txn = transaction.PaymentTxn(sender_address, params, receiver_address, amount, None, note)

    return unsigned_txn
```
### Code Explanation


## Test It
1. Open the `main.py` file
2. Import the build module into the file:
```python
# main.py

# ...
from build import build_unsigned_transaction
```
3. Create the following variables:
```python
# main.py

# ...
from build import build_unsigned_transaction

sender_address = "<Wallet Address>"
senders_private_key = "<Private Key>"

receiver_address=  "<Wallet Address>"

amount = 1000000
note =  "Account 1 is sending 1 Algo to account 2"
```
4. Create a variable called `unsigned_transaction` and set its value to the `build_unsigned_transaction()` method being called:
```python
# main.py

# ...
from build import build_unsigned_transaction

# ...
unsigned_transaction = build_unsigned_transaction(algo_client, sender_address, amount, receiver_address, note)
```
5. Run the program:
```sh
python3 main.py
```
6. **Note:** At this point you can run the file but you are not going to get much of an output unless you like print the unsigned transaction.
