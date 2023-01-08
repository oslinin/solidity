https://training.github.com/downloads/github-git-cheat-sheet.pdfs
cd ~/Documents/solidity
git pull origin main --rebase
git add .
git commit -m "new"
git push -u origin main

https://eth-brownie.readthedocs.io/en/stable/interaction.html

brownie console
brownie run scripts/deploy1.py

brownie networks delete ganache-local
brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=5777
brownie run scripts/deploy1.py --network ganache-local
brownie test --network ganache-local
brownie console --network ganache-local




infusa sucks, use alchemy
brownie networks delete mainnet-fork
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.alchemyapi.io/v2/ccflHgva8zos70u5kPgbSpAZbrEKXLB- accounts=10 mnemonic=brownie port=8545
brownie run scripts/deploy1.py --network mainnet-fork


brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork=’https://eth-rinkeby.alchemyapi.io/v2/5EvZEewTogBMQUViUZMvOT6_Mb7VL8aW’ accounts=10 mnemonic=brownie port=8545
brownie test --network brownie test --network mainnet-fork-dev
