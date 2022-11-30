<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 12.3: Starting an Algorand Node

## What We Are Going To Do

In this section we will learn how to start a Algorand node on the Testnet.

## Learning Objective

By the end of this section student should be able to start their Algorand node on the Testnet.

## Getting Started
1. Navigate into your `sandbox` directory:

```sh
cd ~/algorand-development/sandbox/;
```
2. Start the sandbox:
```sh
./sandbox up testnet
```
* Please not that this command can take up 10-15 mins or longer to finish the initial setup. Just let it run until you see

![Sandbox start up finished](../assets/ch-12/ch-12-sandbox-start-up-finished.jpg)

* If you check your `Docker Desktop` application's `Containers tab` you will see that it now has a `sandbox` container running.

**Sandbox Commands:**
1. Start sandbox: `./sandbox up testnet`
2. Stop sandbox: `./sandbox down`
3. Reset Setting sandbox: `./sandbox clean`