from brownie import zombieFactory0, network, config, accounts
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

def deploy_fund_me():
    account = accounts[0]
    if len(zombieFactory0)==0:
        fund_me = zombieFactory0.deploy({"from": account})
    else:
        fund_me=zombieFactory0[-1]
    return fund_me

def main():
    zombieFactory0 = deploy_fund_me()
    zombieFactory0.createRandomZombie({"_name": "zombie1", "from": account})
    zombieFactory0.createRandomZombie({"_name": "zombie2", "from": account})



