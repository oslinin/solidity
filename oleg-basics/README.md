# book

https://jeiwan.net/posts/programming-defi-uniswap-1/

## uniswap V1

```
mkdir zuniswap && cd $_
yarn add -D hardhat
yarn hardhat
yarn add --dev hardhat-deploy
// copy hardhat.config.js
yarn add --dev dotenv

//getcontract
yarn add --dev hardhat @nomiclabs/hardhat-ethers@npm:hardhat-deploy-ethers

//ethers should be <6, t hen toWei works
yarn list ethers

npm install -g yarn

yarn add --dev hardhat @nomiclabs/hardhat-ethers@npm:hardhat-deploy-ethers ethers

```

# Sample Hardhat Project

This project demonstrates a basic Hardhat use case. It comes with a sample contract, a test for that contract, and a Hardhat Ignition module that deploys that contract.

Try running some of the following tasks:

```shell
npx hardhat help
npx hardhat test
REPORT_GAS=true npx hardhat test
npx hardhat node
npx hardhat ignition deploy ./ignition/modules/Lock.js
```
