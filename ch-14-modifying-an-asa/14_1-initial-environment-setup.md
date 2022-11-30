<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 14.1: Initial Environment Setup
In this section we will learn how to utilize the `AssetConfigTxn` class to modify an existing ASA. It's important to remember that when modifying an ASA, you can only change the following fields:
1. Manager Address
2. Reserve Address
3. Freeze Address
4. Clawback Address

*All* other options for an ASA are frozen for the entire life of the asset and cannot be changed.

## What We Are Going To Do

In this section we will setup our initial environment so by creating our project structure and copying over some pre-existing  files.

## Learning Objective

By the end of this section student should be able to

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
3. Create a new directory called `chapter-14-modifying-an-asa`:
```sh
mkdir chapter-14-modifying-an-asa;
```
1. Copy the `account_details.py` and `utility_functions.py` directory from within your `chapter-13` directory into your newly created `chapter-14-modifying-an-asa` directory:
```sh
cp ./chapter-13-creating-an-algorand-standard-asset/account_details.py chapter-14-modifying-an-asa;
cp ./chapter-13-creating-an-algorand-standard-asset/utility_functions.py chapter-14-modifying-an-asa;
```
5. Inside the `chapter-14` directory create a `main.py` file:
```sh
touch ./chapter-14-modifying-an-asa/main.py
```
6. Open the `chapter-14` directory within your text editor:
```sh
code ./chapter-14-modifying-an-asa/main.py;
```
7. Open the `main.py` and import:
   1. The `account_details` module
   2. `algo_client_connection()` and `send_configured_transaction` function
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