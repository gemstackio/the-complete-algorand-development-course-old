<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 15 Assignment

## Setup Instructions

1. If required, start up your Algorand node
2. Create a new python project called `chapter-15-assignment`

### Atomic Transfer 1

* **Transaction 1**: `Account A` creates a new ASA
* **Transaction 2**: `Account B` opts-in to receive the newly created ASA
* **Transaction 3**: `Account B` sends X amount of Algos to `Account A`
* **Transaction 4**: `Account A` sends X number of ASA to `Account B`

## Atomic Transfer 2: Bonus

For this prompt, you will develop an atomic transfer that handles the logic for selling a house. You will need to create three new accounts:
1. Account A - The buyer
2. Account B - The broker
3. Account C - The seller

Develop an atomic transfer with the following logic:

* **Transaction 1**: Have `Account C - The seller` create a new ASA
 * The asset_name should be `House Deed`
 * It's total supply should be 1
 * The manager address should be set to `Account C - The seller`
 * Leave the reserve, freeze, and clawback blank
* **Transaction 2**: `Account C - The seller` sends a modification transaction that updates the `House ASA's` manger address to `Account B - The broker's` wallet address
* **Transaction 3**: `Account A - The buyer` pay `Account B - The broker` 10 Algos
* **Transaction 4**: `Account B - The broker` pays `Account C - The seller` 5 Algos
* **Transaction 5**:`Account C - The seller` sends the `House ASA` to `Account A - The buyer`
* **Transaction 6**:`Account B - The broker` sends a modification transaction that updates the `House ASA` manager address to `Account A - The buyer's` wallet address