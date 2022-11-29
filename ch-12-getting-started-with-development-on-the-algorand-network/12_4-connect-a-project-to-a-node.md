# Connecting a Project to a Node

## What We Are Going To Do
In this section we will create a helper function which allows us to connect our project to our local Algorand Node.

## Learning Objective
* By the end of this section student should be able to connect a project to a local node instance

## Getting Started

1. Let's start off by creating a project directory for our course work:
```sh
mkdir algo-course-walkthrough; cd algo-course-walkthrough;
```
2. Then create a directory called `chapter-12`
```sh
mkdir chapter-12; cd chapter-12;
```
3. Next lets create two python files `main.py` and `connect.py`
   * `main.py`: will be the entry point to our application
   * `connect.py`: will be one of many module we will make
```sh
touch main.py connect.py
```
3. Open your text editor:
```sh
code .
```

## How To Do It
Now that we have created our initial file structure and two starter files, we are going to create a helper method which we can utilize connect the project to our local node

1. Open the `connect.py` file
2. Import the `algosdk client`:
```python
from algosdk.v2client import algod
```
3. Next, create a function called `algo_client_connection()`:
```python
def algo_client_connection():
```
4. Then within the function we are going to set two variables:
   1. `algod_address`
   2. `algod_token`
```python
def algo_client_connection():
    algod_address = "http://localhost:4001"

    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
```
5. Finally, we will make the `algo_client_connection()` method return a algo client daemon (DEE-muhn):
```python
def algo_client_connection():
    algod_address = "http://localhost:4001"

    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    return algod.AlgodClient(algod_token, algod_address)
```

## Code Explanation
We have implemented a function called `algo_client_connection()` which will be utilized to connect our application the local node we have running on our computer. This connection is the base layer of our application.

We are able to establish this connection by creating two variables:
1. `algod_address` - stores an valid REST endpoint
   * ie: The location where our node is running: `localhost:4001`
2. `algod_token` - stores the token which is required by your application to authenticate access to the node
   * Because we are access the TestNet for development purposes, the token is not very secure

Finally, we add a return statement which returns a client that handles all request sent to and from the node we are connecting to.