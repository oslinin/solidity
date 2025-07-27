# Prediction Market Smart Contracts

This project contains the Solidity smart contracts for a prediction market.

It uses [Hardhat](https://hardhat.org/) for development and testing.

## Getting Started

1.  Install dependencies:
    ```bash
    yarn install
    ```

2.  Compile the contracts:
    ```bash
    yarn hardhat compile
    ```

## Usage

*   Run tests:
    ```bash
    yarn hardhat test
    ```

*   Start a local Hardhat node:
    ```bash
    yarn hardhat node
    ```

*   Deploy the contracts to a local network:
    ```bash
    yarn hardhat deploy --network localhost
    ```

## Contracts

### `MintableERC20.sol`

A standard ERC20 token with an added `mint` function, allowing the contract owner to create new tokens.

**Functions:**
- `mint(address to, uint256 amount)`: Creates `amount` new tokens and assigns them to the `to` address. Only callable by the owner.

### `PredictionMarket.sol`

The core contract for a single prediction market with a binary outcome (YES/NO). It manages the automated market maker (AMM), allows users to bet, and handles the resolution and claiming of funds.

**Public Variables:**
- `usdcToken`: The ERC20 token used for betting (e.g., USDC).
- `yesToken`: The ERC20 token representing a "YES" outcome.
- `noToken`: The ERC20 token representing a "NO" outcome.
- `K`: The constant product for the AMM.
- `category`: The market's category (e.g., ELECTION, SPORTS).
- `question`: The question the market is predicting.
- `oracle`: The address responsible for resolving the market.
- `resolved`: A boolean indicating if the market has been resolved.
- `outcome`: The final outcome of the market (true for YES, false for NO).

**Functions:**
- `initialize()`: Mints the initial liquidity for the AMM.
- `getProbability()`: Returns the current probability of a "YES" outcome, based on the token balances in the AMM.
- `bet(uint256 amount, bool onYes)`: Allows a user to bet `amount` of USDC on a "YES" or "NO" outcome.
- `resolve(bool _outcome)`: Resolves the market with a final outcome. Only callable by the oracle.
- `claim()`: Allows users to claim their winnings after the market has been resolved.

### `PredictionMarketFactory.sol`

A factory contract for creating new `PredictionMarket` instances.

**Functions:**
- `createMarket(...)`: Deploys and initializes a new `PredictionMarket` contract with the specified parameters.
- `getAllMarkets()`: Returns an array of all created `PredictionMarket` contract addresses.
- `getMarketsByCategory(PredictionMarket.Category _category)`: Returns an array of all markets within a specific category.

### `PredictionMarketNWay.sol`

A contract for a prediction market with multiple possible outcomes (N-way).

**Public Variables:**
- `usdcToken`: The ERC20 token used for betting.
- `outcomeTokens`: An array of ERC20 tokens, each representing a possible outcome.
- `category`: The market's category.
- `question`: The question the market is predicting.
- `oracle`: The address responsible for resolving the market.
- `resolved`: A boolean indicating if the market has been resolved.
- `winningOutcome`: The index of the winning outcome.

**Functions:**
- `getProbabilities()`: Returns an array of probabilities for each outcome.
- `bet(uint256 amount, uint256 outcomeIndex)`: Allows a user to bet `amount` of USDC on a specific outcome.
- `resolve(uint256 _winningOutcome)`: Resolves the market with a final outcome. Only callable by the oracle.
- `claim()`: Allows users to claim their winnings after the market has been resolved.

### `PredictionMarketFactoryNWay.sol`

A factory contract for creating new `PredictionMarketNWay` instances.

**Functions:**
- `createMarket(...)`: Deploys and initializes a new `PredictionMarketNWay` contract.
- `getAllMarkets()`: Returns an array of all created `PredictionMarketNWay` contract addresses.
- `getMarketsByCategory(...)`: Returns an array of all N-way markets within a specific category.

## Testing

The project includes a comprehensive test suite to ensure the correctness of the smart contracts. The Hardhat development environment is configured to run as a **mainnet fork**. This means that when you run `yarn hardhat test`, the tests are executed in an environment that mirrors the live Ethereum mainnet.

A key advantage of this setup is that we do not need to deploy mock contracts for external dependencies like USDC. Instead, our tests interact directly with the official, deployed [USDC contract on mainnet](https://etherscan.io/address/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48).

### Unit Tests

The unit tests in the `test/unit/` directory are designed to run on this forked mainnet environment. They cover the core logic of each contract. For example, `test/unit/test.predictionmarket.js` verifies the betting and resolution mechanics, using the actual mainnet USDC contract for transactions.

### Staging Tests

Staging tests in `test/staging/` are designed to test interactions with deployed contracts on the forked network.

#### `test/staging/test.usdc.interaction.js`

This test verifies that the `PredictionMarket` contract can correctly interact with the real USDC contract on the forked mainnet. It includes logic to impersonate a known USDC holder to acquire funds for testing, demonstrating a powerful feature of forked testing.

To run this specific test:
```bash
yarn hardhat test test/staging/test.usdc.interaction.js
```

## Deployment

To deploy the contracts, you can use the `deploy` scripts in the `deploy/` directory.

### Localhost

To deploy to a local network, run:
```bash
yarn hardhat deploy --network localhost
```

### Sepolia Testnet

To deploy to the Sepolia testnet, run:
```bash
yarn hardhat deploy --network sepolia
```

### Sepolia Deployments

You can get test USDC from the [Circle faucet](https://faucet.circle.com/).

The following contracts have been deployed to the Sepolia testnet:

*   **PredictionMarket:** [`0xD4636d7CC71bDd3e01a3AF9A65C110046a3FE06E`](https://sepolia.etherscan.io/address/0xD4636d7CC71bDd3e01a3AF9A65C110046a3FE06E)
*   **PredictionMarketFactory:** [`0x14BF6D8f65b9e4b11919C3E9D4aC53C7b6bE21f0`](https://sepolia.etherscan.io/address/0x14BF6D8f65b9e4b11919C3E9D4aC53C7b6bE21f0)
*   **PredictionMarketFactoryNWay:** [`0x909F71Fc1B1cdb6Bf90d0ffF3C11Fd1aA4Ef98d6`](https://sepolia.etherscan.io/address/0x909F71Fc1B1cdb6Bf90d0ffF3C11Fd1aA4Ef98d6)
*   **PredictionMarketNWay:** [`0xCa90fA9E2Ca9B1113f6811A6832e082c3DD2C906`](https://sepolia.etherscan.io/address/0xCa90fA9E2Ca9B1113f6811A6832e082c3DD2C906)

To deploy to a live network (e.g., mainnet or a testnet), you will need to configure the network in `hardhat.config.js` and provide an account with sufficient funds.

## Copying ABI to Frontend

After deploying the contracts, you need to copy the ABI (Application Binary Interface) and contract addresses to the frontend application. This can be done automatically by running the `04-copy-to-frontend.js` script:
```bash
yarn hardhat deploy --network localhost
```
This script will copy the necessary files to the `prediction-market-nodejs/abi/` directory.