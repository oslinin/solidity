#from brownie import zombieFactory0, network, config, accounts
#from brownie import accounts, ZombieFactory, ZombieFeeding
from brownie import accounts, ZombieHelper
from scripts.helpful_scripts import (
    get_account, deploy_contracts
)




def main():
    account = get_account(0)
    feeding = deploy_contracts(account)   
    feeding.feedOnKitty(0, 15,{"from":account})
    feeding.changeName(1, "Bob the zombie")

    for i in feeding.getZombiesByOwner(account):
      print(f"zombie {i}: {feeding.zombies(i)} owner: {feeding.zombieToOwner(i)}")  
    
    