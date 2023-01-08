#from brownie import zombieFactory0, network, config, accounts
from brownie import accounts, ZombieFactory, ZombieFeeding
from scripts.helpful_scripts import (
    get_account, deploy_contracts
)




def main():
    account = get_account(0)
    feeding = deploy_contracts(account)   
    feeding.kitty(15,{"from":account})
    feeding.feedOnKitty(0, 15,{"from":account})

    for i in range(2):
      print(f"zombie {i}: {feeding.zombies(i)} owner: {feeding.zombieToOwner(i)}")  