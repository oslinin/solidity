
from brownie import (
    accounts, ZombieFeeding,
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
  
  if len(ZombieFeeding)==0:
    print("deploying first time")
    feeding = ZombieFeeding.deploy({"from":account})
    feeding.createRandomZombie("oleg", {"from":account})
    print(f"ZombieFeeding deployed to {feeding.address}")
  else:
    print("found Zombiefeeding, returning it")
    feeding = ZombieFeeding[-1]
    print("end deploy_contracts()")
  return(feeding)