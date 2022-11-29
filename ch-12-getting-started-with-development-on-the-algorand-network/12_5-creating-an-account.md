# Creating an Account

## What We Are Going To Do
In this section we will add a feature to our application which allows us to create new Algorand accounts.

## How To Do It
1. Navigate to your `chapter-12` directory:
```sh
cd ~/<PATH TO>/algo-course-walkthrough/chapter-12;
```
2. Create a `create.py` file:
```sh
touch create.py;
```
3. Open the project within your text editor:
```sh
code .;
```
4. Import the required module:
```python
from algosdk import account, mnemonic
```
5. Declare a function called `create_an_algorand_account()`:
```python
# create.py
def create_an_algorand_account():
```
6. Within the `create_an_algorand_account()` function add the following code:
```python
# create.py
def create_an_algorand_account():
    private_key, address = account.generate_account()
```
7. Then, create a variable called `passphrase` and add the following code:
```python
# create.py

def create_an_algorand_account():
    # ...

    passphrase = mnemonic.from_private_key(private_key)
```
1. Finally, add the following variable and use a print statements:
```python
# create.py

def create_an_algorand_account():
    # ...

    account_details = {
        "address": address,
        "private_key": private_key,
        "passphrase": passphrase
    },

    print(account_details)
```
10. Open your `main.py` file.
11. Import your `create` module:
```py
# main.py
from create import create_an_algorand_account
```
12. Invoke the `create_an_algorand_account()` method:
```py
# main.py
from create import create_an_algorand_account

create_an_algorand_account()
```
13. Run your code:
```sh
python3 main.py
```
1.  Store your new account information somewhere safe
2.  Run this function again so that you have a second account and store that information

## Code Explanation
In step 4 we import two modules from the Algo SDK: `account` and `mnemonic`. Both of which have logic that we need to create an Algorand account.

In step 5 we declare the function.

Step 6, we create two variables: `private_key` and `address` and we set their values to the returns values of the account modules `generate_account()` method. When executed `generate_account()` returns a newly created `private key` and an `account address`.

Step 7, we wrote two print statements that output the newly created wallet address and private key.

In step 8, we utilize the `mnemonic` module's `from_private_key()` method which returns the mnemonic for the private key which we store in a newly created variable `passphrase`.

Finally in step 9 we add a print statement which prints the passphrase to the console.