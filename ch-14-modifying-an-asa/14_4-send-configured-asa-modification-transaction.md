<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 14.4: Send a Configured Transaction to Modify an ASA

## What We Are Going To Do

In this section we will sign and send an configured ASA modification transaction.

## Learning Objective

By the end of this section student should be able to

## Getting Started
1. First we need to sign the transaction that our `configure_transaction_to_update_asset()` function returns:
```python
# main.py
# ...

signed_transaction = transaction.sign(asset_manager['private_key'])
```
2. Next, copy the `send.py` file we created in chapter 13:
```sh
cp ../chapter-13-creating-an-algorand-standard-asset/send.py ../chapter-14-modifying-an-asa;
```
3. Then in the `main.py` file import the `send_configured_transaction()` function from the `send.py` file:
```python
# main.py
# ...
from send import send_configured_transaction

# ...
```
4. Then created a variable called `confirmed_transaction` which stores the returned value of the `send_configured_transaction()` function:
```python
# main.py

# ...

confirmed_transaction = send_configured_transaction(algod_client, signed_transaction)
```
8. Finally, run the code and explain the output
```sh
python3 main.py
```