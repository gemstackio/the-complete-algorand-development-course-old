<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 16.4: Revoke an ASA

In this section we will build a functionality that creates, configures, signs, and executes a transaction that revokes a specific ASA being held in a provided wallet address.

## Learning Objective

By the end of this section student should be able to develop logic that configures and executes an ASA revocation transaction.

## Configure The Transaction
1. Within the `chapter 16 project` created a new file called `revoke.py`:
```sh
touch revoke.py
```
2. Add the following import to `revoke.py`:
```python
# revoke.py

from algosdk.future.transaction import AssetTransferTxn
from send import send_configured_transaction
```
3. Within `revoke.py` create a function called `configure_and_execute_asa_revocation_transaction()`
   * It should accept three arguments:
     1. `algod_client`
     2. `revoke_transaction_args`
```python
# revoke.py
# ...

def configure_and_execute_asa_revocation_transaction(algod_client, revoke_transaction_args ):
```
4. Then create a variable called `unsigned_transaction` which will set equal to an instance of the `AssetTransferTxn` class:
```python
# revoke.py
# ...

def configure_and_execute_asa_revocation_transaction(algod_client, revoke_transaction_args ):
    # ...

    unsigned_transaction = AssetTransferTxn()
```
5. Next we will set the `sp`, `amt`, and `index` from the `revoke_transaction_args`:
```python
# revoke.py
# ...

def configure_and_execute_asa_revocation_transaction(algod_client, revoke_transaction_args ):

    unsigned_transaction = AssetTransferTxn(
        sp=revoke_transaction_args["params"],
        amt=revoke_transaction_args["amount"],
        index=revoke_transaction_args["asset_id"],
    )
```
6. Now set the `sender` of the transaction, this must be equal to the address must match the address listed in the ASA's `clawback` field:
```python
# revoke.py
# ...

def configure_and_execute_asa_revocation_transaction(algod_client, revoke_transaction_args ):
    # ...

    transaction = AssetTransferTxn(
        # ...

        sender=revoke_transaction_args['sender']["address"],
    )
```
7. Now set the `revocation_target` of the transaction equal to the account whose ASAs you are trying to revoke or clawback:
```python
# revoke.py
# ...

def configure_and_execute_asa_revocation_transaction(algod_client, revoke_transaction_args ):
    # ...

    transaction = AssetTransferTxn(
        # ...

        # The wallet address that is having their ASA revoked (or taken away)
        revocation_target=revoke_transaction_args["revocation_target"]["address"],
    )
```
8. Then set the `receiver` of the transaction equal to the account where the ASAs you are revoking will be sent, this can be any address you would like:
```python
# revoke.py
# ...

def configure_and_execute_asa_revocation_transaction(algod_client, revoke_transaction_args ):
    # ...

    transaction = AssetTransferTxn(
        # ...

        # The wallet address where the revoked ASAs will be transferred to
        receiver=revoke_transaction_args["receiver"]["address"]
    )
```

## Sign The transaction

1. Now create a variable called `signed_transaction` which we will use to store the signed transaction:
```python
# revoke.py
# ...

def configure_and_execute_asa_revocation_transaction(algod_client, revoke_transaction_args ):
    # ...

    signed_transaction = unsigned_transaction.sign(revoke_transaction_args["sender"]["private_key"])

```

## Execute The Transaction
1. Now we need to execute and return the transaction:
```python
# revoke.py
# ...

def configure_and_execute_asa_revocation_transaction(algod_client, revoke_transaction_args ):
    # ...

    confirmed_deletion_transaction = send_configured_transaction(algod_client, signed_transaction)

    return confirmed_deletion_transaction
```

## Execute The Transaction

1. Open the `main.py` file and import the `configure_and_execute_asa_revocation_transaction()` function:
```python
# main.py
# ...
from revoke import configure_and_execute_asa_revocation_transaction

# ...
```
2. Then created a variable called `revoke_transaction_args` which we will use to store all our transaction arguments:
   * `sender`: set to the ASA clawback address
   * `revocation_target`: set to the address which ASA should be revoked from
   * `receiver`: set to address where revoked ASA should be sent to
```python
# main.py
# ...

revoke_transaction_args = {
    "params": params,
    "amount": 50,
    "asset_id": asset_id,
    "sender": accounts[0],
    "revocation_target": accounts[1],
    "receiver": accounts[2]
}
```
3. Invoke the `configure_and_execute_asa_revocation_transaction()` function and provided it with the required arguments:
```python
# main.py
# ...

configure_asa_revocation_transaction(algod_client, revoke_transaction_args)
```
4. Finally, run the code:
```sh
python3 main.py
```
5. If you check the [AlgoExplorer](https://testnet.algoexplorer.io/) you will see that the `revocation_target` has had their assets revoked and transferred to the transaction `receiver` address