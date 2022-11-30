<p align="center">
  <img
  src="https://camo.githubusercontent.com/e4ac909b3da508a9e5f8f5276359dd0d8a484a30dc58daf2b29755d87aa09b57/68747470733a2f2f67656d737461636b2e696f2f7374617469632f31626135356364376237663639393165633965646262386331343332323533342f30656261302f6c6f676f5f7072696d6172795f737461636b65642e61766966"
  alt="GemStack's Logo"
  />
</p>

# Chapter 12.2: Installations

## What We Are Going To Do
In this section we will walkthrough the different tools you will need to install to get your Algorand development environment up and running.

## Learning Objective
* By the end of this section student should have the following tools installed:
  * Python 3
  * Docker Desktop
  * WSL (Window Users Only)
  * Git
  * Visual Studio Code
  * Algorand Sandbox

## Getting Started

Just showcase the following installers:

### 1. Python 3

* Go to the [python 3](https://www.python.org/downloads/) website and download the installer
### 2. Docker Desktop

* Go to the [Docker Desktop](https://www.docker.com/products/docker-desktop/) website and download the installer

### 3. Windows Sub-System for Linux (WSL)

This section is **only for windows users**.
* Follow Option 1 for [installation instructions](https://github.com/algorand/sandbox#windows)

### 4. Git
This section is **only for windows users**.

* Go to the [Git](https://git-scm.com/downloads) website and download the installer

### 5. Visual Studio Code

For reference, this text editor is just a recommendation. Feel free to you whichever text editor you would like.

1. Go to the [Visual Studio Code](https://code.visualstudio.com/) website and download the installer
2. Once installed we also recommend installing the [Algorand VS Code Extension](https://marketplace.visualstudio.com/items?itemName=obsidians.vscode-algorand)

### 6. Algorand Sandbox
All users must download this regardless of OS system.

The Algorand Sandbox allows us to install and configure an Algorand development environment.

[Docker Compose](./ch-12-environment-setup.md#2-docker-desktop) **MUST** be installed before attempting to complete this installation process.

1. Go to the [Algorand Sandbox](https://github.com/algorand/sandbox) repo and follow the instructions provided.

<!-- These are our (GemStack's) Instructions; not sure if we should leave this due to the possibility of the Algorand Sandbox docs changing. -->

1. Make a `algorand-development` directory:

```sh
mkdir algorand-development;

cd algorand-development;
```
2. Clone down the repo:
```sh
git clone https://github.com/algorand/sandbox.git
```