<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Consensus

In this chapter, engineers will discuss consensus and two types of mechanisms, nodes, and transactions.

## Learning Objectives

* Be able to define and discuss:
    * Consensus
    * Proof of Work
    * Proof of Stake
    * Nodes
    * Transactions

## Table of Contents

- [Consensus](#consensus)
  - [Learning Objectives](#learning-objectives)
  - [Table of Contents](#table-of-contents)
  - [What is Consensus?](#what-is-consensus)
  - [Types of Consensus Mechanisms](#types-of-consensus-mechanisms)
    - [Proof of Work](#proof-of-work)
    - [Proof of Stake](#proof-of-stake)
  - [Nodes](#nodes)
  - [Transactions](#transactions)
  - [Resources](#resources)
  - [Glossary](#glossary)

## What is Consensus?

An integral part of a blockchain system is `consensus`. It refers to any number of algorithms or methodologies used to achieve agreement, trust, and security across a decentralized network. In this section, we will explore it in-depth and dig a little deeper into two of the most prevalent and specific mechanisms:

1.	`Proof of work` (PoW)
2.	`Proof of stake` (PoS)

`Consensus` is a fault-tolerant mechanism used in blockchain to achieve the necessary agreement on a single data value or a single network state among distributed processes or multi-agent systems, such as with cryptocurrencies.

In centralized systems, such as a retail database. It would that hold information about a customer and administrator(s), and it has the authority to update and maintain said database. The task of updating, which includes adding, deleting, and updating names or addresses of the customers, is always performed by that central authority.

Public blockchains operate differently. They are decentralized, self-regulating systems that work on a global scale without any single authority. They take in hundreds of thousands of participants (nodes) who work on verifying, authenticating and confirming `transactions`.

Since `blockchain technology` is changing at a rapid pace, these public ledgers need an efficient, real-time, and secure mechanism to ensure `transactions` on the network are accurate, genuine and agreed upon. The `consensus mechanism` completes this critical task. It does this by defining rules to process, update, and authenticate `transactions` on the blockchain, as well as handling and updating nodes.

## Types of Consensus Mechanisms

There are different types of `consensus` mechanisms, each operating a bit differently. While we will be focusing on `proof of work` and `proof of stake`, there are other variations and implementations that exist, such as:

1. **Proof of Burn (PoB)**: transactors must send a small amount of cryptocurrency to inaccessible wallet addresses, therefore ‘burning’ them out of existence. This implementation avoids the possibility of any cryptocurrency coin double-spending.
2. **Proof of Capacity (PoC)**: allows sharing memory space of the contributing `nodes` on the network. Essentially, the more memory or hard disk space a node on the network has, the more rights its granted for maintaining the public ledger.
3. **Proof of Activity (PoA)**: a hybrid mechanism that uses aspects of both `proof of stake` and `proof of work`.

### Proof of Work

`Proof of work` is a decentralized `consensus` mechanism requiring network members to spend effort solving an arbitrary mathematical puzzle to confirm blocks.

The concept of `proof of work` was adapted to secure digital assets by Hal Finney in 2004 through the idea of ["Reusable Proof of Work"](https://nakamotoinstitute.org/finney/rpow/index.html) using the SHA-256 algorithm. The [SHA-256 (Secure Hash Algorithm)](https://www.n-able.com/blog/sha-256-encryption) algorithm is a hash function created by the National Security Agency in 2001 which outputs a fixed-length string value that is 256 bits or 64 characters long.

Like most ideas and concepts in blockchain, it wasn’t until Bitcoin arrived in 2009 that the concept of `proof of work` became largely adopted and implemented. A fun fact too: Finney was also the recipient of the first Bitcoin `transaction`. `Proof of work` is also the basis of many other cryptocurrencies (such as Dogecoin, Litecoin, and Ethereum prior to ERC-20/ Ethereum 2.0 implementation).

Moving forward, we will be discussing `proof of work` as it applies to Bitcoin. As we learned in chapter one, the blockchain digital ledger contains a record of all `transactions`, arranged in blocks.

The way tampering is detected within a network is by validating the hash for each block. Once the execution of an SHA-256 hash function on a data set is complete, it outputs a single hash value. The SHA-256 hash function is unidirectional; meaning that once a block has been hashed, you cannot easily un-hash it. You can only verify that the data that generated the hash matches the original data.

For example, if we were to hash the following phrases:
   * `proof of work`
   * `proof of work!`

The SHA-256 value would be completely different:

| Word           | SHA-256 Value                                                    |
| -------------- | ---------------------------------------------------------------- |
| proof of work  | 73b01e93631118159b40599836bb23022ca7ad00c1203d18984cd982654e7f40 |
| proof of work! | 235e9d2d6ff07309d9bdbc34ea380b6e59d6e974cb72a9447b1ac281ea1d86db |


As mentioned briefly in the prior chapter, any change to the original data will result in an unrecognizable hash. Modern-day computers can easily generate a hash for a set of Bitcoin `transactions`. Hence, the Bitcoin network sets a difficulty level to turn the process of solving a puzzle into `work`. This difficulty level is adjusted so that new blocks are mined approximately every ten minutes. The difficulty level setting is accomplished by establishing a target for the hash; the lower the target, the smaller the set of valid hashes, and the harder it is to generate one. This essentially means that a hash starts with a long string of zeros.

Mining is a highly competitive process. Someone around the world will generate acceptable an accepted block (i.e. completing the puzzle) just around every ten minutes. No one knows who that person or group will be, and t gain a competitive advantage, miners work together to increase their chances of successfully mining blocks. Which is how they are rewarded. `Proof of work` makes it hard to alter any aspect of the blockchain since its alteration would require re-mining all the subsequent blocks.

To summarize, here’s an example of `proof of work`. The hash for block #660000, mined on December 4th, 2020, is 00000000000000000008eddcaf078f12c69a439dde30dbb5aac3d9d94e9c18f6.2 . The block reward for that successful hash was 6.25 BTC. That block will always contain 745 `transactions` involving just over 1,666 Bitcoins and the previous block's header. Therefore, if someone tried to change a `transaction` amount by even the smallest amount, the resulting hash would be unrecognizable. As a result, The network would reject the fraudulent attempt to change it.

### Proof of Stake

`Proof of stake` was created as an alternative to `proof of work`. With `proof of stake`, users validate block `transactions` based on the number of coins a validator stakes. It is seen as more efficient and less risky in terms of the potential of a cyberattack. This is specifically because a malicious entity would also be altering their stake in the network. Because it does not involve the immense computing power to solve a mathematical puzzle, it is much more energy efficient.

`Proof of stake` reduces the amount of power a computer needs to verify blocks and `transactions` that keep the blockchain secure. The owners offer their coins as collateral for the opportunity to validate a block, thus becoming ‘validators’. Rather than using a competitive-based mechanism, like `proof of work`, validators are selected randomly to validate the block.

The goal of `proof of stake` is to reduce the scalability and environmental sustainability issues surrounding the `proof of work` mechanism, which has been an important topic of concern in the cryptocurrency world. Since users utilizing the `proof of work` mechanism are always looking for a competitive advantage in mining, such as setting using massive hardware farms, `proof of stake` is seen as a much more efficient and environmentally friendly option.

The amount of energy required to mine on the `proof of work` mechanism significantly impacts profit and pricing dynamics. A study conducted by the University of Cambridge stated that `proof of work` mining uses as much energy as a small country. The [Cambridge Bitcoin Electricity Consumption Index](https://ccaf.io/cbeci/index/comparisons) estimates the bitcoin mining network consumes almost 70 terawatt-hours (TWh) of electricity per year, ranking it the 40th largest consumer of electricity by country. By way of comparison, Ireland (ranked 68th) uses just over a third of Bitcoin’s consumption, or 25 TWh, and Austria, at number 42, consumes 64.6 TWh of electricity per year, according to 2016 data compiled by the [CIA](https://www.cia.gov/the-world-factbook/field/electricity-consumption/).

Even Ethereum is transitioning it's protocol from `proof of work` to `proof of stake`.

## Nodes

`Nodes` are infrastructure that forms the blockchain network. think of nodes similar to computer servers in this regard. They can be any electronic device, from a computer, laptop, or physical server. All the `nodes` are connected on the blockchain network, and they continuously exchange and relay the newest information to each other, ensuring they’re all synced and up-to-date.  They are often geographically spread out and preserve blockchain data, which is why they are considered the backbone of the network.

When one node attempts to add a new block of `transactions` to the blockchain, the node transmits and distributes that information to the rest of the `nodes` on the network. The other `nodes` can either accept or reject the block. If the `nodes` accept the new block of `transactions`, it saves and stores it sequentially on top of the blocks it has already stored. The rest of the network is then updated so the rest of the nodes know of the update. 

It's important to note that these details can vary drastically from different blockchains, it will be up to you to learn the specifics of each.

Several types of `nodes` exist in the blockchain ecosystem (view the resources section below for more information), but two general types are as follows:

1.	Full nodes
2.	Lightweight nodes

Full nodes are best known for maintaining `consensus` between other `nodes`. They support and provide security to the blockchain network and ensure that data is authentic and verified. Full nodes will constantly download and store a copy of the blockchain's complete history to observe and enforce its rules.

A lightweight node is a `node` for each user on the blockchain network that needs to connect to a full node to synchronize to the current state of the network to participate. Lightweight nodes usually only contain a partial list of the blockchain operations, the block headers, instead of its entire `transaction` history, which validates the authenticity of the `transactions`. Because of this, lightweight nodes are easier to maintain.

## Transactions

When a new `transaction` between users is requested and entered into the network, it is then transmitted to `nodes` across that network. The network of `nodes` confirm the validity of the `transaction` (via their consensus mechanism). Once validated and confirmed, they are added to the public ledger and the transaction goes through.

Some networks can be completely independent of one another as well. Entities such as banks, governments, and even schools can have their own private blockchain networks (if it's supported by the specific blockchain implementation).

A public ledger is distributed across all `nodes` and stored. This includes the price, asset amount, and ownership. Since a `transaction` is transparent and recorded on the ledger, it is open for anyone to see (this can vary based upon implementation).

---
## Resources

* [Consensus Mechanisms](https://ethereum.org/en/developers/docs/consensus-mechanisms/)
* [What is "proof of work" or "proof of stake"?](https://www.coinbase.com/learn/crypto-basics/what-is-proof-of-work-or-proof-of-stake?utm_source=google_search_nb&utm_medium=cpc&utm_campaign=9943088770&utm_content=127915792732&utm_term=&utm_creative=580583551399&utm_device=c&utm_placement=&utm_network=g&utm_location=9061283&gclid=CjwKCAjwopWSBhB6EiwAjxmqDajnMMn9FFxauxEXigGudTzp44q-zuRbsiCSN1V61mS7EMsAWmkErRoC_7kQAvD_BwE)
* ["Reusable Proof of Work"](https://nakamotoinstitute.org/finney/rpow/index.html)
* [SHA-256 Algorithm Overview](https://www.n-able.com/blog/sha-256-encryption)
* [ Fiat Money](https://www.investopedia.com/terms/f/fiatmoney.asp)
* [Cambridge Bitcoin Electricity Consumption Index](https://ccaf.io/cbeci/index/comparisons)
* [CIA World Factbook](https://www.cia.gov/the-world-factbook/field/electricity-consumption/)
* [Bitcoin Mining](https://www.investopedia.com/terms/b/bitcoin-mining.asp)
* [Proof of Burn](https://www.investopedia.com/terms/p/proof-burn-cryptocurrency.asp)
* [Ethereum 2.0](https://markets.businessinsider.com/news/currencies/ethereum-blockchain-technology-crypto-cryptocurrency-ether-eth-vitalik-buterin-markets-2022-3)

## Glossary

* `Consensus`: A fault-tolerant mechanism used in computer and blockchain systems to achieve the necessary agreement on a single data value or a single state of the network among distributed processes or multi-agent systems, such as with cryptocurrencies.
* `Nodes`: An electronic device, usually a computer, laptop, or server, on a blockchain network that stores, spreads, and preserves blockchain data.
* `Proof of Stake`: A decentralized consensus mechanism that requires members of a network to use their assets as collateral to have the opportunity to validate a block.
* `Proof of Work`: A decentralized consensus mechanism that requires network members to expend effort solving an arbitrary mathematical puzzle to prevent anyone from getting over on the system.
* `Transactions`: An agreement, or communication, between a buyer and seller to exchange goods, services, or assets for payment.