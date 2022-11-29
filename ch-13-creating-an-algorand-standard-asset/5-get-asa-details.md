# Get Asset Details

## What We Are Going To Do

In this section we will learn how to start 

## Learning Objective

By the end of this section student should be able to

## Getting Started
1. Open the `utility_functions.py` file:
2. Create a function called `print_asset_details()` which accepts an algo_client, asset_id, and an account as arguments:
```python
# utility_functions.py
# ...

def print_asset_details(algod_client, asset_id,  account):
```
4. Next we will create a variable called `account_info` which will utilize the algo client to pull all information for the provided account:
```python
# utility_functions.py
# ...

def print_asset_details(algod_client, asset_id,  account):
    account_info = algod_client.account_info(account)
```
5. Then we will create a variable called `index` which will be used as we iterate over the account information we have stored:
```python
# utility_functions.py
# ...

def print_asset_details(algod_client, asset_id,  account):
    # ...

    index = 0
```
6. Then we will create a `for loop` to iterate over the `create-asset` data stored within the `account_info`:
```python
# utility_functions.py
# ...

def print_asset_details(algod_client, asset_id,  account):
    # ...

    for list_of_assets in account_info['created-assets']:
```
7. Then create a variable called `current_asset` which will store an asset on each iteration, then increment the `index` by 1:
```python
# utility_functions.py
# ...

def print_asset_details(algod_client, asset_id,  account):
    # ...

    for list_of_assets in account_info['created-assets']:
        current_asset = account_info['created-assets'][index]

        index = index + 1
```
8. Finally write an `if statement` that checks to see if the current asset ID matches the `asset_id` provided, if so print out the asset details:
```python
# utility_functions.py
# ...

def print_asset_details(algod_client, asset_id,  account):
    # ...

    for list_of_assets in account_info['created-assets']:
        # ...

        if (current_asset['index'] == asset_id):
            print(f"Asset {current_asset['index']} Details: \n {format_json_data(current_asset, True)}")
            break
```