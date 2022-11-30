<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 15.4: Check If An Account Is Opted In

## What We Are Going To Do

In this section we will develop functionality that checks if a provided account is opted-in to receive a specific ASA or not.

## Learning Objective

By the end of this section student should be able to

## Getting Started
1. Open the `main.py` and comment out the `print()` statement:
```python
# main.py
# ...

# print(format_json_data(account_info, True))
```
2. Create a variable called `opting_in_account_assets` and set it equal to the `assets` array within the `account_info` object:
```python
# main.py
opting_in_account_assets = opting_in_accounts_info["assets"]
```
3. Then created a new file called `check_if.py`:
```sh
touch check_if.py
```
4. Within `check_if.py` create a function called `is_account_opted_in()`
   * It should accept two arguments:
     1. `account_assets`
     2. `provided_asset_id`
```python
# check_if.py

def is_account_opted_in(account_assets, provided_asset_id):
```
5. Then write a `for loop` that iterates over the assets information stored within the `account_assets` array:
```python
# check_if.py

def is_account_opted_in(account_assets, provided_asset_id):
    for asset_info in account_assets:
```
6. Next, create a variable called `current_asset_id` which will set equal to the id of the asset being iterated over:
```python
# check_if.py

def is_account_opted_in(account_assets, provided_asset_id):
    # ...
        current_asset_id = asset_info["asset-id"]

```
7. Then write an `if statement` that checks to see if the `current_asset_id` matches the `provided_asset_id` that was passed in as an argument:
```python
# check_if.py

def is_account_opted_in(account_assets, provided_asset_id):
    # ...
        if(current_asset_id == provided_asset_id):

```
8. If this evaluates as true then:
   1.  Print _"The account is already opted-in"_
   2.  Create a variable called `opted_in` and set it equal to `True`
   3.  Return `opted_in`
```python
# check_if.py

def is_account_opted_in(account_assets, provided_asset_id):
    # ...
            print("The account is already opted-in")
            opted_in = True
            return opted_in
```
9. Finally if the statement evaluates to false:
   1.  Print _"The account is not opted-in"_
   2.  Create a variable called `opted_in` and set it equal to `False`
   3.  Return `opted_in`
```python
def is_account_opted_in(account_assets, provided_asset_id):
    # ...

    print("The account is not opted-in")
    print("Opting account in now")
    opted_in = False
    return opted_in

```
10. Open the `main.py` file and import the `is_account_opted_in()` function:
```python
# main.py
# ...
from check_if import is_account_opted_in
```
11. Then created a variable called `opted_in` and set it equal to an evocation the `is_account_opted_in()` function:
```python
# main.py
# ...

# ...
opted_in = is_account_opted_in(opting_in_account_assets, asset_id)
```
12. Finally create a `if statement` that checks to see if the variable `opted_in` is not true:
```python
# main.py
# ...

if not opted_in:
```
13. If this evaluates to true then we need to create some logic that will:
   1. Create and configure an ASA opt-in transaction
   2. Sign the transaction
   3. Send the transaction
14. In the next video we will develop logic that allows us to create and configure an ASA opt-in transaction