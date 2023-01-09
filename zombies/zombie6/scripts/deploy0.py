from brownie import accounts, PriceConsumerV3# ZombieFactory
from scripts.helpful_scripts import (
    get_account, deploy_contracts
)

def main():
  acc  = get_account() 
  if len(PriceConsumerV3)==0:
    feeding = PriceConsumerV3.deploy({"from":acc})
  else:
    feeding = PriceConsumerV3[-1]
  a=feeding.getLatestPrice({"from":acc})
  b=feeding.getDecimals({"from":acc})
  c=a/b
  print(c)
