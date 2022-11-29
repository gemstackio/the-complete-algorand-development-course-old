# Check an Account Balance
## What We Are Going To Do
In this section we will add functionality that allows us to check an accounts balance.

## Build It
1. Navigate to your `algo-course-walkthrough` directory:
```sh
cd ~/<PATH TO>/algo-course-walkthrough;
```
2. Create a `check.py` file:
```sh
touch check.py;
```
3. Open the project within your text editor:
```sh
code .;
```
4. Declare a method called `check_account_balance()`
```python
# check.py
def check_account_balance():
```
5. `check_account_balance()` should accept two parameters `algod_client` and `address`:
```python
# check.py
def check_account_balance(algo_client, address):
```
6. Next, create a variable called `account_info` which store the following:
```python
# check.py
def check_account_balance(algo_client, address):
    account_info = algo_client.account_info(address)
```
7. Then, write the following print statement:
```python
# check.py
def check_account_balance(algo_client, address):
    # ...

    print(f'Account balance: {account_info.get("amount")} microAlgos')
```
8. Next open your `main.py` file and comment out the `create_an_algorand_account()`:
```python
# main.py

# ...

algo_client = algo_client_connection()

# create_an_algorand_account()
```
1.  The next thing we have to do is import our function and invoke it, we also need to import our account details:
```python
# main.py

# ...
from check import check_account_balance
from account_details import accounts

algo_client = algo_client_connection()

# create_an_algorand_account()

check_account_balance(algo_client, accounts[0]["address"])
```
    
## Code Explanation
In step 5, we add two expected parameters to the method:
   1. `algo_client`: expects an instance of an algo client
   2. `address`: expects an valid wallet address

In step 6, we create a variable called `account_info` which stores utilizes the provided Algo client to execute an account info look up via the `account_info()` method. The `account_info()` method accepts an address as an argument and returns a dictionary with information for the provided account.

In step 7, we write a print statement that outputs the account balance by deconstructing the dictionary with the `.get()` method.


## Test It
<!-- Provide walkthrough on testing it -->