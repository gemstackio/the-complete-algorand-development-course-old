# 15.2: Checking Account Info

In this section we will build logic that allows us to pull account information into our project which we will use later to check in the account is opted-in to hold a specific ASA.

## Learning Objective

By the end of this section student should be able to

## Getting Started
1. Now we need to create two variables `asa_creator` and`account_opting_in` :
```python
# main.py
# ...
asa_creator = accounts[0]
account_opting_in = accounts[1]
```
1. Next created a variable called `opting_in_accounts_info` which will invoke the `account_info()` and pass it the address for `account_opting_in` variable as an argument:
```python
# main.py
# ...

opting_in_accounts_info = algod_client.account_info(account_opting_in['address'])
```
3. Now lets print the the information it returns be sure to import `format_json_data` from the `utility_functions` module:
```python
# main.py
# ...
from utility_functions import algo_client_connection, format_json_data

# ...
print(format_json_data(opting_in_accounts_info, True))
```
4. The print statement will output something like this:
```sh
{
    "address": "S7JXSCSI65MDUV7UKOJT3QSO6UOOSLK7ADAKGKDDS7TWYHNGMLH7KAAVTA",
    "amount": 988000,
    "amount-without-pending-rewards": 988000,
    "apps-local-state": [],
    "apps-total-schema": {
        "num-byte-slice": 0,
        "num-uint": 0
    },
    "assets": [
        {
            "amount": 0,
            "asset-id": 106515079,
            "is-frozen": false
        },
        {
            "amount": 0,
            "asset-id": 106542996,
            "is-frozen": false
        }
    ],
    "created-apps": [],
    "created-assets": [],
    "min-balance": 300000,
    "pending-rewards": 0,
    "reward-base": 27521,
    "rewards": 0,
    "round": 23916471,
    "status": "Offline",
    "total-apps-opted-in": 0,
    "total-assets-opted-in": 2,
    "total-created-apps": 0,
    "total-created-assets": 0
}

```
5. You will see that there is a lot of information about the account, our main concern here is the fact that the there is a property called `assets` which contains (or will contain) a list of dictionaries.
   *. Each dictionary represents a specific asset that the account is either:
      *  Opted-into or Capable of holding
      *  Is opted-into and currently holds a specific amount of algos