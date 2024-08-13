- [Vscode/markdown](#vscodemarkdown)
- [JS](#js)
- [Foundry](#foundry)
  - [Foundry-07-fundme](#foundry-07-fundme)
    - [Tools (forge/anvil/chisel)](#tools-forgeanvilchisel)
      - [forge](#forge)
      - [gas](#gas)
      - [chiesel (solidity in terminal)](#chiesel-solidity-in-terminal)
      - [other](#other)
    - [make](#make)
    - [gas](#gas-1)
      - [Gas optimization/storage](#gas-optimizationstorage)
    - [address](#address)
    - [cheats](#cheats)
    - [tests](#tests)
    - [etc](#etc)
    - [git](#git)
  - [Foundry-08-html-fund-me](#foundry-08-html-fund-me)
  - [Foundry-09-raffle](#foundry-09-raffle)
    - [VRF](#vrf)
    - [Keeper](#keeper)
    - [tests](#tests-1)
    - [subscription](#subscription)

# Vscode/markdown

Terminal Ctrl+`
send line to terminal ctrl+' thanks to https://marketplace.visualstudio.com/items?itemName=nvbn.sendtorepl

Render:
Open your Markdown file in VS Code.
Use the shortcut Ctrl+Shift+V to open the Markdown preview side-by-side with your editor.
Alternatively, you can use Ctrl+K V to open the preview in a new tab.

TOC: extension Markdown All In One; ctrl+shift+P; type create TOC

Ctrl+P: file viewer; Ctrl+Shift+P: command palette

code <file> //edit file

# JS

VRFv2SubscriptionManager is VRFConsumerBaseV2

# Foundry

https://github.com/Cyfrin/foundry-full-course-cu?tab=readme-ov-file

https://www.infura.io/faucet/sepolia great for ETH
https://faucets.chain.link/ good for LINK

extensions
solidity hardhat
better toml

settings json:
"[solidity]": {
"editor.defaultFormatter": "NomicFoundation.hardhat-solidity"
},

"[javascript]": {
"editor.defaultFormatter": "esbenp.prettier-vscode"
},

//through settings non-json
"editor.formatOnSave": true

## Foundry-07-fundme

### Tools (forge/anvil/chisel)

forge: like hardhat
anvil: like hardhat node, or ganache
chisel: like hardhat console; solidity in terminal

#### forge

forge coverage
forge coverage --fork-url $SEPOLIA_RPC_URL
forge test
forge test --match-test --v
forge test --match-test --vv
forge test --match-test --vvv
forge test --match-test --vvvv
forge test --fork-url $SEPOLIA_RPC_URL

forge install transmissions11/soulmate
remappings = ['@chainlink/contracts/=lib/chainlink-brownie-contracts/contracts/', '@solmate=lib/solmate/src/']

#### gas

forge snapshot --match-test dfdfs

#### chiesel (solidity in terminal)

!help
unit256 catANdThree = cat + 3;
catAndThree gives 4
ctrlC2x to dexit

#### other

cast --to-base 0x01 dec
cast sig "createSubscription()" //should match metamask ensuring UI isn't malicious
http://openchain.xyz/signatures

### make

Makefile
-include .env
build:; forge build
make build

```bash
NETWORK_ARGS := --rpc-url http://localhost:8545 --private-key $(DEFAULT_ANVIL_KEY) --broadcast

ifeq ($(findstring --network sepolia,$(ARGS)),--network sepolia)
	NETWORK_ARGS := --rpc-url $(SEPOLIA_RPC_URL) --account $(ACCOUNT) --broadcast --verify --etherscan-api-key $(ETHERSCAN_API_KEY) -vvvv
endif

deploy-sepolia:
	@forge script script/DeployFundMe.s.sol:DeployFundMe $(NETWORK_ARGS)
```

make deploy-spolia

### gas

Anvil gas defaults to 0

to simulate gas use vm.txGasPrice(GAS_PRICE)

```solidity
// vm.txGasPrice(GAS_PRICE);
// uint256 gasStart = gasleft();
// // Act
vm.startPrank(fundMe.getOwner());
fundMe.withdraw();
vm.stopPrank();
// uint256 gasEnd = gasleft();
// uint256 gasUsed = (gasStart - gasEnd) \* tx.gasprice;
console.log(gasused)
```

or

gas reports: https://book.getfoundry.sh/forge/gas-reports
forge snapshot
produces .gas-snapshot

private more gas efficient. View getter functions.

#### Gas optimization/storage

storage: giant list of 32 byte long slots.
blank for mappings, length for array
constants/immutable don't take slot
immutable i\_; storage s\_
local in memory.
strings are dynamically sized array. solidity needs to know whether to allocate space.

funWithStorage: script/DeployStorageFun.s.sol

forge inspect FundMe storageLayout

or

forge script script/DeployFundMe.s.sol --rpc-url http:/127.0.0.1:8545 --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 --broadcast
(contract address: 0x5FbDB2315678afecb367f032d93F642f64180aa3)
cast storage 0x5FbDB2315678afecb367f032d93F642f64180aa3 2
(gives the owner public key 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266)
cast -h
https://book.getfoundry.sh/reference/cast/cast
cast --to-int256 "0x0000000000000000000000000000000000000000000000000000000066b7995a"

opcodes http://evm.codes/ storage expensive

### address

uint160

### cheats

https://book.getfoundry.sh/forge/cheatcodes

1. vm.prank: create address
2. vm.deal(PLAYER, STARTING_USER_BALANCE): fund address vm.deal(USER, STARTING_USER_BALANCE);
3. vm.hoax: pank and fund
4. address public PLAYER = makeAddr("player");
5. vm.startPrank(msg.sender);
6. vm.expectRevert(Raffle.Raffle\_\_SendMoreToEnterRaffle.selector); //function selector
7. vm.stopPrank();
8. vm.prank(PLAYER);
9. vm.expectEmit(true, false, false, false, address(raffle));
10. vm.warp(block.timestamp + automationUpdateInterval + 1);
11. vm.roll(block.number + 1);
12. vm.startBroadcast(account);
13. vm.stopBroadcast();
14.

### tests

setUp

1. unit
2. intergation tests: interactions

arrange/act/assert

Interactions
FundFundMe is Script
foundry-devops to get last address.
forge install Cyfrin/foundry-devops --no-commit
git rm -rf lib/forge-std
rm -rf lib/forge-
forge install foundry-rs/forge-std@v1.8.2 --no-commit
import {DevOpsTools} from "foundry-devops/src/DevOpsTools.sol";
ffi = true //in toml. lets foundry run commands

forge script script/Interactions.s.sol:FundFundMe --rpc-url http://127.0.0.1:8545 --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 --broadcast

make

### etc

forge test --match-test testPriceFeedSetCorrectly
forge test --match-test testPriceFeedSetCorrectly -vvv
forge test --match-test testPriceFeedSetCorrectly -vvv --fork-url $SEPOLIA_RPC_URL
forge coverage --fork-url $SEPOLIA_RPC_URL
https://book.getfoundry.sh/forge/cheatcodes
vm.expectRevert(); //next line revert
fundMe.fund();
private more gas efficient. use getters.
prank code sets message.sender only in test
startprank/stopprank includes start/stop broadcast
standard cheat: book.getfoundry.sh/reference/forge-std/hoax
hoax(address(i), STARTING_USER_BALANCE); //FundMeTest.t.sol
startPrank/stopPrank like broadcast

```

```

readme
quick start
use templtes

### git

git init -b main
git status
git add .
git log
git commit -m "dfkj"

//github
//make repository
git config user.name ""
git remote add origin <url>
git remote -v
git push -u origin main

git clone

## Foundry-08-html-fund-me

git clone https://github.com/Cyfrin/html-fund-me-cu foundry-08-fundme-html
cd foundry-08-fundme-html; rm -rf .git

install live server

right click > inpect(Q) > console
window
window.ethereum

## Foundry-09-raffle

git clone https://github.com/Cyfrin/foundry-smart-contract-lottery-cu foundry-09-smartcontract-lottery
cd

### VRF

https://docs.chain.link/vrf/v2/subscription/examples/get-a-random-number

1. Create a subscription in subscription manager
2. Fund with LINK
3. Consumer address?
4. Deploy VRF2 compotible contract (has ConsumerBase, subscriptionID, keyhash, gaslane, callbackgaslimit for callback function, blockconfirmation speed v. secure, words)
5. add consumer address

https://docs.chain.link/vrf/v2-5/subscription/get-a-random-number

override: virtual in inheritence. VRFConsumerBaseV2
function fulfillRandomWords(uint256,uint256[] calldata randomWords
) internal override
VRFConsumerBaseV2 takes coordinator

### Keeper

https://automation.chain.link/
https://chrontab.guru human readable output from chron tabs

### tests

CEI: Checks, Effects, Interactions
//checks: requires. more gas efficient to revert early
//effect our own contract
//interactions: external with other contracts. (avoid reentrancy attacks)
put events before interactions.

arrange/act/assert

local
forked testnet
testnet

vm.startBroadcast(); //actually deploy

### subscription

forge script script/Interactions.s.sol:FundSubscription --rpc-url $SEPOLIA_RPC_URL --private-key $PRIVATE_KEY --broadcast

forge install foundary/devlops
DevOpstTools.get_most_recent_deployment


https://vrf.chain.link/sepolia/  VRF 

https://sepolia.etherscan.io/address/0x8103b0a8a00be2ddc778e6e7eaa21791cd364625 VRF
https://vrf.chain.link/sepolia/12063

https://sepolia.etherscan.io/address/0x35c6BAc0B834756670C5bcAAF36a1f2958c87efB Raffle

https://automation.chain.link/sepolia/46503602413155825590236000896645636080533299372637975538543387700694086199540 keeper


