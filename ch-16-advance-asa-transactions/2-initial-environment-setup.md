# 16.1: Initial Environment Setup
In this section we will learn how to utilize the `AssetFreezeTxn` class to create a transaction that freezes an ASA.

## What We Are Going To Do

In this section we will setup our initial environment so by creating our project structure and copying over some pre-existing  files.

## Learning Objective

By the end of this section student should be able to

## Start Your Node:

1. If your sandbox is not already running, navigate into your `sandbox` directory and start it:
```sh
cd ~/algorand-development/sandbox/;
./sandbox up testnet;
```

## Create and Configure the Project Boilerplate

1. Open another terminal window and navigate to your `algo-course-walkthrough` directory:
```sh
cd ~/<PATH TO>/algo-course-walkthrough/;
```
2. Create a new directory called `chapter-16-advance-asa-transactions`:
```sh
mkdir chapter-16-advance-asa-transactions;
```
3. Copy the `account_details.py` and `utility_functions.py` files from within your `chapter-15` directory into your newly created `chapter-16` directory:
```sh
cp ./chapter-15-atomic-transfer/account_details.py chapter-16-advance-asa-transactions;

cp ./chapter-15-atomic-transfer/utility_functions.py chapter-16-advance-asa-transactions;
cp ./chapter-15-atomic-transfer/send.py chapter-16-advance-asa-transactions;
```
```
5. Inside the `chapter-16` directory create a `main.py` file:
```sh
touch ./chapter-16-advance-asa-transactions/main.py
```
6. Open the `chapter-16` directory within your text editor:
```sh
code ./chapter-16-advance-asa-transactions;
```
1. Open the `main.py` and import the `account_details` module and `algo_client_connection()`function:
```python
# main.py

from account_details import accounts
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
2. Copy the `asa_creator.py` file from `chapter-15`:
```sh
cp ./chapter-15-atomic-transfer/asa_creator.py chapter-16-advance-asa-transactions;
```
3. Take note that the `asa_creator` variable is set to your first account information:
```python
# asa_creator.py
# ...

asa_creator = accounts[0]

# ...
```
4. Update the ASA name and unit name and then run the file:
```python
# asa_creator.py

# ...
asa_unit_name = "<Provided a new unit name>"
asa_name = "<Provided a new name>"
# ...
```

```sh
python3 asa_creator.py;
```
5. Be sure to note that we have set the `default_frozen` equal to `False` and provided an address in the `freeze` value which the address that must send a freeze transaction:
```python
# asa_creator.py

# ...
transaction = AssetConfigTxn(
    # ...
    default_frozen=False,
    # ...
)
# ...
```
6. This is what make a transaction unfrozen at creation
7. Now inside your `main.py` file add a variable called `asset_id` and set it equal to the newly created ASA id:
```python
# main.py
# ...

# ...
asset_id = 0
```