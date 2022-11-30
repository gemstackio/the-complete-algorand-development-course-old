<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 15.1: How This Will Work

In this chapter we will learn how to develop logic that utilizes the Python AlgoSDK `AssetTransferTxn` class which allows an account to opt-in to a specific ASA and then have it transferred to their account.

Also explain that we are going to build an Atomic Transfer and what that is.

`Atomic Transfers` allow you to group transaction that either all succeed or fail. In our current use-case we want to execute two transaction together:
1. That opts an account into a specific ASA
2. A transaction that transfers a specified amount of ASAs from a creators account to a receivers account.