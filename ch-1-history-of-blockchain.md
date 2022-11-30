<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 1: History of BlockChain

In this chapter, engineers will become familiar with the history of blockchain technology, gain knowledge of its characteristics and intricacies, and understand why blockchain is relevant in the modern era.

## Learning Objectives

* Be able to discuss the history of blockchain at a high level
* Define and be able to explain cryptography at a high level
* Understand the main characteristics of a blockchain
* Understand why blockchain technology is needed

## Table of Contents

- [Chapter 1: History of BlockChain](#chapter-1-history-of-blockchain)
  - [Learning Objectives](#learning-objectives)
  - [Table of Contents](#table-of-contents)
  - [The Creation of Bitcoin](#the-creation-of-bitcoin)
  - [What is Cryptography?](#what-is-cryptography)
  - [What is a Blockchain](#what-is-a-blockchain)
  - [What is a Block?](#what-is-a-block)
  - [Why is Blockchain Needed](#why-is-blockchain-needed)
  - [The Blockchain Trilemma](#the-blockchain-trilemma)
    - [Decentralization](#decentralization)
    - [Scalability](#scalability)
    - [Security](#security)
  - [Characteristics of a Blockchain](#characteristics-of-a-blockchain)
    - [Immutability](#immutability)
    - [Decentralized Technology](#decentralized-technology)
    - [Enhanced Security](#enhanced-security)
    - [Distributed ledgers](#distributed-ledgers)
    - [Consensus](#consensus)
    - [Faster settlement](#faster-settlement)
  - [Resources](#resources)
  - [Glossary](#glossary)


## The Creation of Bitcoin

The year was 2009, and the entire world was beginning to dig out of "The Great Recession." During this time, a white paper with the concept of "Bitcoin" had started to take internet forums by storm. [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) published by the pseudonymous author Satoshi Nakamoto. No one knows the author's identity, or if it's a single person/group.

Satoshi Nakamoto's main intention in creating Bitcoin was to develop a peer-to-peer electronic cash system. On January 3rd, 2009, Bitcoin officially launched; Nakamoto's white paper outlined how Bitcoin would work. This detailed everything from how many Bitcoins there would be, to rules for buying and selling, minting new Bitcoins, etc. These rules helped to bring scarcity to the resource as it had a ceiling of 21 million.

## What is Cryptography?

By definition, `cryptography` is the study and practice of sending secure, encrypted messages between two or more parties. `Cryptography` isn't just used in digital currency; it's also widely used every day on our computers and other networks. With this being said, `Cryptography` can help some digital currency transactions to remain pseudonymous and secure, with no bank or other intermediary required. It can also help in securing an immutable ledger.

In simpler terms, cryptography allows outgoing message to be encrypted, which hides it from third parties. The receiver decrypts it, making it visible upon arrival at its destination. Cryptocurrencies use `cryptography` to allow transactions to be secure, anonymous, and, most conveniently, trustless. You don't need to know anything about the entity or party sending the message to make the transaction.

## What is a Blockchain

Blockchain technology is one of the hottest topics in the technology world these days, but it remains a mysterious technology to some. For now, all you need to know about a node is that it's a computer connected to a cryptocurrency network and can execute certain functions like creating, receiving, or sending information.

`Blockchain Technology` describes a decentralized set of peer-to-peer systems distributed amongst a set nodes. These nodes are used to process transactions and run a given blockchain network. A `Blockchain` stores and secures decentralized records of transactions in its respective network.

It was first proposed as a research project in 1991 by Stuart Haber and W. Scott Stornetta. These two researchers wanted to implement a system where timestamps could not be tampered with. It wasn't until Bitcoin arrived in 2009 that `blockchain` was implemented into its first real-world application.

## What is a Block?

A `block` is a data structure within A `blockchain`, this is where transaction data is permanently recorded. Different networks (Algorand, Solana, Ethereum, Bitcoin, Etc.) can have various implementations and use cases. With that being said, the following information can be found in almost all implementations of a block:

1. **Block number**: A number that identifies a block within a certain cryptocurrency network.
2.	**Transactions**: A list of all transactions within that block.
3.  **Timestamp**: A time recording when the transaction was made within the block.
4.	**Hash and previous hash**: An algorithm that produces a value for the previous hash and the hash of the previous blocks

Blocks also have specific storage capacities and can only hold a specified number of transactions. When a capacity limit or trigger event for transactions are reached, that block is submitted for processing, validated and closed. When closed, the blocks carry some of the information of the previous block (the hash of the prior block) and that is how they are linked together, hence the name `blockchain`.

## Why is Blockchain Needed

Now that we know what `blockchain` is, let's go into some of the benefits and why it's needed in today's digital age. A study done by [Pew Research Center Study in May of 2021](https://www.pewresearch.org/politics/2021/05/17/public-trust-in-government-1958-2021/), showed that American public trust in the government is at a near all-time low. Blockchain technology is slowly but surely making its way into the government sector because of its advantages. Government databases are one of the most popular targets for hackers and cyberattacks due to the nature of the content in their data, social security numbers, birthdates, addresses, etc. Blockchain technology can help enhance security within government databases by hardening networks, reducing single-point-of-failure risk, and making database breaches very difficult. It can also promote a more transparent system, allowing participants to see and verify data.

An example of this can be the voting system. Voting can be a very time-consuming process; citizens take time off work and sometimes clear a whole day out of their calendars just to make sure they can go wait in long lines at the polls. MiVote, an Australian-based startup, is developing Australia's first online voting platform utilizing `blockchain technology`. Voters can cast their votes through their smartphone, where the records are stored on the `blockchain` securely and can never be changed. MiVote is also currently on trial with the Indian and South American governments. With this `blockchain` implementation, votes are counted with high accuracy, are linked and authenticated to a single voter; Once the vote is added to a public ledger, it can never be edited or erased.

The banking industry can also benefit from `blockchain technology` as well. Most, if not all banks, carry expensive transfer fees, which is how they generate a lot of their income. Those fees add up over time and can become a big expense to the average person. Not to mention, sending and exchanging money overseas also carry hefty fees and hidden costs. `Blockchain` is currently disrupting the banking industry as we speak by providing a peer-to-peer payment and lending system with better security and low fees.

Another major issue and hurdle the world is facing right now is supply chain management. The lack of transparency, reliability, and coordination between providers and systems has been a severe pain point for the industry. `Blockchain` technology can help tackle these issues with several features and some improvements. It can help track products across the entire chain with the use of its great traceability features. The use of record transactions such as history, timestamps, dates, and auditing in the supply chain industry can be easily managed. Anyone would be able to verify the authenticity, status, and transaction of products.

## The Blockchain Trilemma

The `blockchain trilemma` is a concept created by Vitaly Buterin. Buterin is best known for being one of the co-founders of Ethereum, as well as co-founding Bitcoin Magazine in 2011. The concept addresses challenges other programmers face when creating `blockchain` implementations or applications. Those challenges are:

1. **Scalability**
2. **Decentralization**
3. **Security**

It is important to understand that the `blockchain trilemma` is only a model to visualize those challenges. There isn't anything that states that these concepts cannot be achieved simultaneously; but rather, that there are significant difficulties in achieving all three.

### Decentralization

In a `blockchain` decentralization enables us to mitigate risk associated with one entity. More importantly, trust doesn't rely on this one single entity when conducting a transaction either. Since there is no one governing authority, decisions/confirmations are made by nodes (confirmed via miners or stakeholders).

The trade-off for some systems with an emphasis on decentralization can be speed (such as bitcoin or ethereum).



### Scalability

Scalability is important in `blockchain` as systems must be able to operate efficiently as demand increases.

`Blockchain` implementation and centralized systems are both measured in `transactions per second` also known as  `TPS`. `Blockchain` projects face a challenge in the number of transactions they can process and are improving every day in this regard. Certain implementations such as `Avalanche` or `Solana` specifically focus on this need, and have improved greatly in a relatively short period of time.

### Security

It can be argued that transaction security is one of the foundations for `blockchain technology`. some `blockchain` projects have more of an emphasis than others on personal/private security than others (such as `Monero` or `Zcash`). These projects rely more on the strength of their anonymity features in order to keep transactions private. Other's focus more on solid consensus mechanisms and their decentralized emphasis to promote infrastructure security (such as `Algorand`).

## Characteristics of a Blockchain

Blockchain's emerging role is in part due to some of the significant characteristics that it embodies. `Blockchain technology` is not just a network for trading cryptocurrency; as it has more to offer than that. There are many `blockchain` features and characteristics, yet we will focus on six critical ones in this section:

1. `Immutability`
2. `Decentralized Technology`
3. Enhanced `Security`
4. `Distributed Ledgers`
5. `Consensus`
6. Faster `Settlement`

### Immutability

`Immutability` is defined as something that cannot be altered or changed. Blockchain technology works differently than our typical day-to-day banking system. Once a transaction block gets added to a ledger, no one can go back edit it; hence, it is immutable.

### Decentralized Technology

The second key characteristic of `blockchain` is `decentralized technology`. Since it doesn't have any governing authority overseeing the framework, a group of nodes maintain the network (either via stakeholders or confirmed by miners). This enables the user, to be in direct control of their assets that live on the network.

In short, decentralization provides a user control, with fewer failures, within a more transparent system. A bank is a prime example of centralized technology. As they are a central authority always in control of data and its systems. Facebook can be another example of centralized technology. Meta has complete control over their features, and they decide who can and who cannot join their platform. Also, if you are exchanging data, that data will be verified by a third party, and then transferred by said party. This information can often be kept by that third party.

### Enhanced Security

Next, we have `security`. If we refer back to `cryptography`, this is what enhances security on the `blockchain` network. No one can easily change any features or transactions on the network for their benefit (this also ties into a blockchain ledgers immutable nature).

Every block on the blockchain ledger has a different and unique hash. Cryptographic hashing is a method that is used to convert data into a unique string of text. Hashing is also a one-way function (such as ECDSA), which means the data, once entered into the algorithm, outputs a unique value. This value is difficult to decipher and is very computationally intensive to decode. Each block also has a hash that is different from the last, as even subtle changes in the data will output drastically different hashes.

### Distributed ledgers

The fourth key characteristic is `distributed ledgers`. A `distributed ledger` is a lives on the distributed blockchain network, shared and updated from nodes on the network to confirm transactions. Each node on the network has an exact copy of the ledgers which offers transparency to all parties involved. It allows significant traceability/transparency, as you are able to find any transaction confirmed on the blockchain network.

### Consensus

Another key characteristic, is `consensus`. `Consensus` mechanisms, in simple terms, are systems designed to reach agreements (on transactions) amongst a set of distributed nodes. `Consensus` mechanisms can vary wildly from `proof of work` to `proof of stake` implementations.

### Faster settlement

The last key characteristic we will cover is a fairly simple one, faster `settlement`. When it comes to traditional banking systems, we all know that asset `settlement` can be rather slow. Blockchain technology offers potentially faster `settlement` times. Users can also access or utilize their assets much quicker. This characteristic is helpful with foreign and international transactions, as well as transferring a specific asset domestically.

---


## Resources

* [Bitcoin](https://bitcoin.org/en/)
* [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf)
* [Ollie Leech](https://www.linkedin.com/in/ollie-leech-9582318a/)
* [What is `Cryptography`](https://www.coindesk.com/learn/2021/08/02/what-is-``cryptography``/)
* [What is Blockchain Technology](https://www.ibm.com/topics/what-is-blockchain)
* [Structure of a Block](https://www.youtube.com/watch?v=pHEw4Z3UgUc)
* [Pew Research Center Study in May of 2021](https://www.pewresearch.org/politics/2021/05/17/public-trust-in-government-1958-2021/)
* [MiVote](https://www.transpire.com/our-work/mivote-revolutionising-democracy-online-voting/)
* [The Blockchain Trilemma](https://academy.shrimpy.io/post/what-is-the-blockchain-trilemma)
* [What is Blockchain Security?](https://www.ibm.com/topics/blockchain-security)
* [ECDSA](https://www.hypr.com/elliptic-curve-digital-signature-algorithm/#:~:text=The%20Elliptic%20Curve%20Digital%20Signature%20Algorithm%20(ECDSA)%20is%20a%20Digital,public%20key%20cryptography%20(PKC).)

## Glossary

Block
: A data structure within the `blockchain` database, where transaction data in a cryptocurrency `blockchain` is permanently recorded.

Blockchain
: A distributed database in which a record of transactions made in a cryptocurrency is maintained across several computers that are linked in a peer-to-peer network.

Blockchain trilemma
: A concept created by programmer Vitaly Buterin, that addresses challenges programmers face when creating blockchain technology that is scalable, decentralized, and secure, without compromising any of the three.

Consensus
: A fault-tolerant mechanism that is used in computer and blockchain systems to achieve the necessary agreement on a single data value or a single state of the network among distributed processes or multi-agent systems, such as with cryptocurrencies.

Crypto
: Combining form representing Greek kryptós "hidden" or "secret," used in the formation of compound words.

Cryptography
: The study and practice of sending secure, encrypted messages between two or more parties.

Decentralized Technology
: The transfer of control and decision-making from a centralized entity (individual, organization, or group thereof) to a distributed network.

Distributed Ledger
: A consensus of replicated, shared, and synchronized digital data geographically spread across multiple sites, countries, or institutions.

Immutability
: Not capable of or susceptible to change.

Settlement
: The transfer of ownership involving the physical exchange of securities or payment.

Security
: Blockchain security is a comprehensive risk management system for a blockchain network, using cybersecurity frameworks, assurance services, and best practices to reduce risks against attacks and fraud.