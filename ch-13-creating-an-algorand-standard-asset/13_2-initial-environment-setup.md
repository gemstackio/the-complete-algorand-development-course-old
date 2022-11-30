<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 13.2: Initial Environment Setup

## What We Are Going To Do

In this section we will will setup our development environment so that we can begin creating our own ASAs.

## Learning Objective

By the end of this section student will have:
    * There testnet node up and running
    * A folder structure created to utilize while following along with this chapter
    * A `main.py` and `utility_functions.py` file created
    * Two helper functions created:
      1. `algo_client_connection`
      2. `format_json_data()`

## Getting Started
1. Navigate into your `sandbox` directory:

```sh
cd ~/algorand-development/sandbox/;
```
2. Start the sandbox:
```sh
./sandbox up testnet
```
3. Open another terminal window and navigate to your `algo-course-walkthrough` directory:
```sh
cd ~/<PATH TO>/algo-course-walkthrough/;
```
4. Create a new directory called `chapter-13-creating-an-algorand-standard-asset`:
```sh
mkdir chapter-13-creating-an-algorand-standard-asset;
```
5. Copy the `account_details.py` directory from within your `chapter-12` directory into your newly created `chapter-13-creating-an-algorand-standard-asset` directory:
```sh
cp chapter-12/account_details.py chapter-13-creating-an-algorand-standard-asset/
```
6. Create a `main.py` and `utility_functions.py` file:
```sh
touch main.py utility_functions.py
```
7. Open the `algorand-course-walkthrough` directory within your text editor:
```sh
code .;
```
8. Open the `utility_functions.py` file and create a `algo_client_connection` function which will return an instance of an algod client:
```python
# utility_functions.py
from algosdk.v2client import algod

def algo_client_connection():
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    algod_client = algod.AlgodClient(
        algod_token=algod_token, algod_address=algod_address)
    return algod_client
```
9. Next we will create another helper function called `format_json_data()`:
```python
# utility_functions.py
# ...

def format_json_data(data, should_return):
    """
    Helper Functions that takes json data and formats it.

    Args:
       data (string): the data to format
       should_return (bool): True returns data | False prints data
    """
    if(should_return == True):
        return json.dumps(data, indent=4)

    print(json.dumps(data, indent=4))
```