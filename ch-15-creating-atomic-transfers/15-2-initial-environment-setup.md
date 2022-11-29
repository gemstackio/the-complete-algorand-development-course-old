# 15.2: Initial Environment Setup

In this section we will setup our initial environment so by creating our project structure and copying over some pre-existing files.


## Learning Objective

By the end of this section student should be able to stand up a basic Python AlgoSDK project.

## Getting Started
1. If your sandbox is not already running, navigate into your `sandbox` directory and start it:
```sh
cd ~/algorand-development/sandbox/;
./sandbox up testnet;
```
2. Open another terminal window and navigate to your `algo-course-walkthrough` directory:
```sh
cd ~/<PATH TO>/algo-course-walkthrough/;
```
3. Create a new directory called ` chapter-15-atomic-transfer`:
```sh
mkdir chapter-15-atomic-transfer;
```
1. Copy the `account_details.py`, `send.py`, and `utility_functions.py` directory from within your `chapter-14` directory into your newly created `chapter-15` directory:
```sh
cp chapter-14-modifying-an-asa/account_details.py  chapter-15-atomic-transfer;
cp chapter-14-modifying-an-asa/send.py  chapter-15-atomic-transfer;
cp chapter-14-modifying-an-asa/utility_functions.py  chapter-15-atomic-transfer;
```
5. Inside the `chapter-15` directory create a `main.py` file:
```sh
touch chapter-15-atomic-transfer/main.py
```
6. Open the `chapter-15` directory within your text editor:
```sh
code ./ chapter-15-atomic-transfer;
```
7. Open the `main.py` and import the `account_details` module and `algo_client_connection()` function
```python
# main.py

from account_details import accounts
from send import send_configured_transaction
from utility_functions import algo_client_connection
```
8. Initialize an Algo Client:
```python
# main.py
# ...

algod_client = algo_client_connection()
```

## Create a New ASA

1. The last thing we will do is create a new ASA to work with.
2. Create a file called `asa_creator.py`:
```sh
touch asa_creator.py;
```
3. Paste in the following code:
```python
# asa_creator.py
from utility_functions import algo_client_connection
from send import send_configured_transaction
from algosdk.future.transaction import AssetConfigTxn
from account_details import accounts

algod_client = algo_client_connection()

asa_creator = accounts[0]
total = 1000
asa_unit_name = "CREDS"
asa_name = "Galactic Credits"

params = algod_client.suggested_params()

transaction = AssetConfigTxn(
    sender=asa_creator["address"],
    sp=params,
    total=total,
    default_frozen=False,
    unit_name=asa_unit_name,
    asset_name=asa_name,
    manager=asa_creator["address"],
    reserve=asa_creator["address"],
    freeze=asa_creator["address"],
    clawback=asa_creator["address"],
    url="https:www.info.com",
    strict_empty_address_check=False,
    decimals=0
)

signed_transaction = transaction.sign(asa_creator["private_key"])

confirmed_transaction = send_configured_transaction(algod_client, signed_transaction)
```
4.  Take note that the `asa_creator` variable is set to your first account information:
```python
# asa_creator.py
# ...

asa_creator = accounts[0]

# ...
```
5.  Feel free to update any information you would like and then run the file:
```sh
python3 asa_creator.py;
```
6. Now inside your `main.py` file add a variable called `asset_id` and set it equal to the newly created ASA id:
```python
# main.py
# ...

# ...
asset_id = <ASSET_ID>
```