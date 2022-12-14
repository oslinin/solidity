#from brownie import zombieFactory0, network, config, accounts
#from brownie import accounts, ZombieFactory, ZombieFeeding
from brownie import accounts, ZombieHelper
from scripts.helpful_scripts import (
    get_account, deploy_contracts
)




def main():
    acc = [get_account(x) for x in (0,1)]

    feeding = deploy_contracts(acc[0])   
    feeding.createRandomZombie("Bob", {"from":acc[1]})

    #feeding.feedOnKitty(0, 15,{"from":account})
    #feeding.changeName(1, "Bob the zombie")
    
    for i in feeding.getZombiesByOwner(acc[0]):
      print(f"zombie {i}: {feeding.zombies(i)} owner: {feeding.zombieToOwner(i)}")  
    for i in feeding.getZombiesByOwner(acc[1]):
      print(f"zombie {i}: {feeding.zombies(i)} owner: {feeding.zombieToOwner(i)}")  
    
    feeding.attack(0, 1, {"from":acc[0]})

    #winners = list(map(lambda n: feeding.zombies(n)[2]>1, (0,1)))
    winner = [x for x in (0,1) if feeding.zombies(x)[4]>0][0]
    #print("winner = "+str(winner))
    feeding.changeName(winner, "Winner zombie",{"from":acc[winner]})

    
    for i in feeding.getZombiesByOwner(acc[0]):
      print(f"zombie {i}: {feeding.zombies(i)} owner: {feeding.zombieToOwner(i)}")  
    for i in feeding.getZombiesByOwner(acc[1]):
      print(f"zombie {i}: {feeding.zombies(i)} owner: {feeding.zombieToOwner(i)}")  
    

