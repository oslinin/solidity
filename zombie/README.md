https://training.github.com/downloads/github-git-cheat-sheet.pdfs
cd ~/Documents/solidity
git pull origin main --rebase
git add .
git commit -m "new"
git push -u origin main

https://eth-brownie.readthedocs.io/en/stable/interaction.html


brownie run scripts/deploy1.py

infusa sucks, use alchemy
brownie networks delete mainnet-fork
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.alchemyapi.io/v2/ccflHgva8zos70u5kPgbSpAZbrEKXLB- accounts=10 mnemonic=brownie port=8545
brownie run scripts/deploy1.py --network mainnet-fork

brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork=’https://eth-rinkeby.alchemyapi.io/v2/5EvZEewTogBMQUViUZMvOT6_Mb7VL8aW’ accounts=10 mnemonic=brownie port=8545
brownie test --network brownie test --network mainnet-fork-dev
