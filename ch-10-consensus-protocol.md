<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 10: The Consensus Protocol

Consensus protocols form the backbone of any blockchain. Their fundamental purpose is to help nodes in a blockchain network verify transactions. For review, there are two main types of consensus protocols:

1. `Proof-of-Work (PoW)`
2. `Proof of stake (PoS)`

The problem with standard implementations today is that they often sacrifice one of three fundamental elements of the Blockchain Trilemma: **security**, **scalability**, **decentralization**.

To help alleviate this problem, Silvio Micali created a **Pure-Proof-of-Stake Protocol (PPoS)**, which the Algorand network uses.

## Table of Contents

- [Chapter 10: The Consensus Protocol](#chapter-10-the-consensus-protocol)
  - [Table of Contents](#table-of-contents)
  - [What is Pure-Proof-of-Stake (PPoS)](#what-is-pure-proof-of-stake-ppos)
  - [How PPoS Works](#how-ppos-works)
    - [Verifiable Random Function (VRF)](#verifiable-random-function-vrf)
    - [Participation Key](#participation-key)
    - [Ephemeral Key](#ephemeral-key)
  - [PPoS Stages of Consensus](#ppos-stages-of-consensus)
    - [Stage 1: Transaction Submission](#stage-1-transaction-submission)
    - [Stage 2: Block Proposal](#stage-2-block-proposal)
    - [Stage 3: Block Verification](#stage-3-block-verification)
    - [Stage 4: Block Certification](#stage-4-block-certification)
  - [Resources](#resources)
  - [Glossary:](#glossary)

## What is Pure-Proof-of-Stake (PPoS)

Algorand's Pure-Proof-of-Stake protocol securely and efficiently achieves consensus in a fully decentralized network by placing the network's security in the hands of the community.

Stakeholders are chosen randomly and secretly to propose, verify, and certify new blocks. Any online stakeholder has the potential opportunity to be selected. The more stake (or Algos) a user has, the higher their chances of being selected and the great weight their votes and proposals have.

The genius of the PPoS protocol is that it empowers the majority of users within the Algorand Network to be the bedrock of its security rather than a minority. This makes it impossible for owners of a small stake to harm the whole system. The majority of stakeholders are naturally inclined to behave; otherwise, it would diminish their entire holding and the overall network.

## How PPoS Works

So how exactly is consensus achieved on the Algorand Network?

At a high-level, based on a stakeholder's stake in the network, they are selected to vote on consensus. Their stake equates to the number of Algos they hold. The more Algos, a user has, the better their chance at being selected to vote.

There are four stages to achieving consensus on the Algorand Network:
1. Block Creation
2. Block Proposal
3. Block Verification
4. Block Certification

Before exploring the stages in more detail, some terminology needs to be understood.

### Verifiable Random Function (VRF)

Algorand's `Verifiable Random Function (VRF)` executes an unpredictable yet verifiably random lottery selection that determines which stakeholders can participate in proposing, verifying, and or certifying a block. This is a weighted lottery selection process since every Algo in a stakeholder's account increases their chances of being selected.

### Participation Key

`Participation keys` are a node-specific set of specialized keys that allow stakeholders to vote and propose blocks. `Participation keys`, are sometimes referred to as `partkeys` and are located on a single node.

Stakeholders must generate and register their own `participation keys`. During the generation of a `participation key`, a stakeholder may specify the number of rounds their key is valid. An' ephemeral key' is generated for every round that a `participation key` is valid.

For example, if a stakeholder were to generate a `Participation key` and set it valid for 1,000 voting rounds, then 1,000 `ephemeral keys` would also be generated.

### Ephemeral Key

An `Ephemeral Key` is a single-use key for signing vote and proposal messages. They provide an added layer of security to the voting and proposal process on the Algorand network.

Each time a stakeholder participates in a vote, they sign their message with an ephemeral key, after which the key is deleted. Using a different `ephemeral key` every voting round and deleting it ensures stakeholder messages are secure. Say somehow, in the future, a participating node is compromised and exposes a stakeholder's previously used `ephemeral key` it could not be used for any malicious purposes.

## PPoS Stages of Consensus

Let's say Alice wants to send Bob 1 Algo; how would consensus be achieved? How would their transaction be written to the Algorand Network?

The Pure-Proof-of-Stake protocol allows a transaction is to achieve finality.

There are four stages to the achieving consensus:
1. **Transaction Submission**
2. **Block Proposal**
3. **Block Verification**
4. **Block Certification**

### Stage 1: Transaction Submission

The transaction submission stage kicks off when Alice sends a transaction to Bob, which is then submitted to an Algorand node.

Once the node receives the transaction it places it in a queue with other transactions that have been received.

All the queued transactions are then propagated to every other node in the Algorand network.

Once propagated each node executes a VRF.

### Stage 2: Block Proposal

If a user on a node is selected by the VRF executed during the transaction submission stage that node will then select a group of transactions from its queue to place within a newly created block.

The node will then take the VRF proof that was generated when a user was selected and propagates it along with the newly create block to all other node in the network as a block proposal.

While this is happening other nodes in the network who have also had users selected during the transaction submission stage VRF will also perform the same action and propagate blocks proposals to the network.

At this point you have nodes that are in one of two situations:

1. Nodes that have had a user selected from the initial VRF and propagated a block proposal to the network.

or

2. Nodes that did not have a user selected from the initial VRF.

This is important to remember because Nodes in either situation at this time are receiving block proposals from other nodes.

As a Node receives a block proposal it is held as the nodes primary proposal.

If a node has received multiple proposals it compares the accompanying VRF proof for each.

Whichever proposal has the lowest proof is kept as the node's primary proposal and is then propagated to the rest of the network.

Eventually every Node in the network will have received and compared block proposals until they all have received, stored, and propagated the one with the lowest proof.

### Stage 3: Block Verification

Once every node has identified which block proposal has the lowest proof the network must verify agreement on it.

This kicks off the block verification stage.

The stage is started with another VRF being executed against the stake holdings of every participating user in the network.

All selected users are then placed into a committee which will vote to verify the block proposal.

A user's voting power is calculated based on how many times they were selected by the VRF.

The committee then propagates their votes to the entire network.

Each node in the network collects and tallies the votes.

Once a super majority of vote is reached the block proposal is considered verified and now has to be certified.

### Stage 4: Block Certification

The block certification stage begins with a third VRF being executed, which selects a committee of users to certify the verified block proposal.

After each member in the committee votes to certify the block, their votes is then propagated to the network.

Once a super majority is reached the block is written to the blockchain.

At this point Alice's transaction to Bob has achieved finality.

The amazing part is that all four stages of achieving consensus take less than 5 seconds.

After which the process begins again.

---

## Resources

 * [Algorand Developer Docs - Algorand consensus](https://developer.algorand.org/docs/get-details/algorand_consensus/)
* [YouTube - Algorand Blockchain Core Protocol Overview](https://www.youtube.com/watch?v=gACVKaNqxPs)
* [Algorand Developer Docs - Why Algorand](https://developer.algorand.org/docs/get-started/basics/why_algorand/)
* [Technical WhitePaper On Consensus](https://www.algorand.com/technology/white-papers)
* [Algorand - Scaling Byzantine Agreements for Cryptocurrencies](https://people.csail.mit.edu/nickolai/papers/gilad-algorand-eprint.pdf)
* [Algorand Releases First Open-Source Code: Verifiable Random Function](https://medium.com/algorand/algorand-releases-first-open-source-code-of-verifiable-random-function-93c2960abd61)

## Glossary:

* `Ephemeral Key`: single-use key utilize for signing vote and proposal messages
* `Participation keys`: are a node-specific set of specialized keys that allow stakeholders to participate in voting and proposing blocks
* `Spending keys`: An individual accounts private key
* `Verifiable random function (VRF)`: executes an unpredictable yet verifiably random lottery selection that determines which stakeholders can participate in proposing, verifying, and or certifying a block