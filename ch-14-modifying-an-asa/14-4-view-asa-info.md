# View ASA Information

## What We Are Going To Do

In this section we will learn how to start

## Learning Objective

By the end of this section student should be able to

## Getting Started
1. Open the `utility_functions.py` and create a function called `print_asset_info()`:
```python
# utility_functions.py
# ...

def print_asset_info(algod_client, account, asset_id):
```
2. Within the `print_asset_info()` function create a variable called `asset_info` which store the ASA information:
```python
# utility_functions.py
# ...

def print_asset_info(algod_client, account, asset_id):
    asset_info = algod_client.account_asset_info(account['address'], asset_id)
```
3. Then add a print statement that outputs the asset info:
```python
# utility_functions.py
# ...

def print_asset_info(algod_client, account, asset_id):
    # ...
    print(f"Asset Info: {format_json_data(asset_info, True)}")
```
4. Open the `main.py` and import the `print_asset_info()` function
```python
# main.py
# ...
from utility_functions import algo_client_connection, print_asset_info

# ...
```
5. Finally invoke the `print_asset_info()` function and pass it the required arguments:
```python
# main.py
# ...

print_asset_info(algod_client, asset_manager, asset_id)
```