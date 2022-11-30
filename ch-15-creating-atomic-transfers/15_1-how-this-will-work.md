# 15.1: How This Will Work

In this chapter we will learn how to develop logic that utilizes the `AssetTransferTxn` class which allows an account to opt-in to a specific ASA and then have it transferred to their account.

Also explain that we are going to build an Atomic Transfer and what that is.

`Atomic Transfers` allow you to group transaction that either all succeed or fail. In our current use-case we want to execute two transaction together:
1. That opts an account into a specific ASA
2. A transaction that transfers a specified amount of ASAs from a creators account to a receivers account.


## Learning Objective

By the end of this video student will be informed about the basic Python AlgoSDK project that we will be creating to opt an account into a specific ASA and then have it transferred to their accounts.

## Getting Started
1. Showcase the existing application and what it is able to do.