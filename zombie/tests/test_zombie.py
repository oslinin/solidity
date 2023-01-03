from brownie import accounts, ZombieFactory, ZombieFeeding
from scripts.helpful_scripts import (
    get_account
)

def test_1():
  account = get_account(0)
  # if len(ZombieFeeding)==0:
  #   feeding = ZombieFeeding.deploy({"from":account})
  #   feeding.createRandomZombie("oleg", {"from":account})
  #   print(f"ZombieFeeding deployed to {feeding.address}")
  # else:
  feeding = ZombieFeeding[-1]

  z = feeding.zombies(0)
  assert(z[0] == "oleg")