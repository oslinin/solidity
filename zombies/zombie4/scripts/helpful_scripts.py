
from brownie import (
    accounts, ZombieAttack,
    network,
    config,
    # MockV3Aggregator,
    # VRFCoordinatorMock,
    # LinkToken,
    # Contract,
    #interface,
)

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    # accounts[0]
    # accounts.add("env")
    # accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


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
  
  if len(ZombieAttack)==0:
    print("deploying first time")
    feeding = ZombieAttack.deploy({"from":account})
    feeding.setKittyContractAddress("0x06012c8cf97BEaD5deAe237070F9587f8E7A266d",{"from":account})
    feeding.createRandomZombie("oleg", {"from":account})
    print(f"ZombieFeeding deployed to {feeding.address}")
  else:
    print("found Zombiefeeding, returning it")
    feeding = ZombieAttack[-1]
    print("end deploy_contracts()")
  return(feeding)