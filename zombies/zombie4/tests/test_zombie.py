from brownie import accounts, ZombieFeeding
from scripts.helpful_scripts import (
    get_account, deploy_contracts
)

def test_1():
  account = get_account(0)
  f = ZombieFeeding[-1]
  f = f.zombies(0)
  assert(f[0] == "oleg")
  assert(f[1] == 4186893168218264)

def test_2():
  account = get_account(0)
  f = ZombieFeeding[-1]
  assert(f.zombieToOwner(0)==account)


  # if len(ZombieFeeding)==0:
  #   feeding = ZombieFeeding.deploy({"from":account})
  #   feeding.createRandomZombie("oleg", {"from":account})
  #   print(f"ZombieFeeding deployed to {feeding.address}")
  # else:
  #feeding = ZombieFeeding[-1]

  #z = feeding.zombies(0)
  #assert(z[0] == "oleg")