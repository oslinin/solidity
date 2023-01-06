#from brownie import zombieFactory0, network, config, accounts
from brownie import accounts, ZombieFactory, ZombieFeeding
from scripts.helpful_scripts import (
    get_account
)


def deploy_contracts(account):
  print("start deploy_contracts()")
  # if len(ZombieFactory)==0:
  #   zz = ZombieFactory.deploy({"from":account})
  #   print(f"zombiefactory deployed to {zz.address}")
  #   zz.createRandomZombie("oleg", {"from":account})
  #   #zz.createRandomZombie("slinin", {"from":account})
  # else:
  #   zz = ZombieFactory[-1]
  #   print(f"Contract found on  {zz.address}")   
  
  if len(ZombieFeeding)==0:
    feeding = ZombieFeeding.deploy({"from":account})
    feeding.createRandomZombie("oleg", {"from":account})
    print(f"ZombieFeeding deployed to {feeding.address}")
  else:
    feeding = ZombieFeeding[-1]
  
  print("end deploy_contracts()")
  return(feeding)

def main():
    print("main()")
    account = get_account(0)
    print(account)

    feeding = deploy_contracts(account)   

    for i in range(1):
      print(f"zombie {i}: {feeding.zombies(i)} owner: {feeding.zombieToOwner(i)}")  

    print("finally")

    #feeding.feedOnKitty(0, 15,{"from":account})
    #for i in range(2):
    #  print(f"zombie {i}: {feeding.zombies(i)} owner: {feeding.zombieToOwner(i)}")  