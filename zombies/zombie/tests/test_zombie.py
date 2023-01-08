from brownie import accounts, ZombieFactory0
from scripts.helpful_scripts import (
    get_account
)

def test_1():
  account = get_account(0)
  f = ZombieFactory0[-1]
  f = f.zombies(0)
  assert(f[0] == "oleg")
  assert(f[1] == 4186893168218264)

  
  # if len(ZombieFeeding)==0:
  #   feeding = ZombieFeeding.deploy({"from":account})
  #   feeding.createRandomZombie("oleg", {"from":account})
  #   print(f"ZombieFeeding deployed to {feeding.address}")
  # else:
  #feeding = ZombieFeeding[-1]

  #z = feeding.zombies(0)
  #assert(z[0] == "oleg")