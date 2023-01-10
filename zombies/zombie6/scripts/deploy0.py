from brownie import (
    accounts, network, MockV3Aggregator, 
    PriceConsumerV3# ZombieFactory

)
from scripts.helpful_scripts import (
    get_account, deploy_mocks, 
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
)

def main():
  acc  = get_account() 
  if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    deploy_mocks()
    price_feed_address = MockV3Aggregator[-1].address
  else:
    price_feed_address = config["networks"][
      network.show_active()]["eth_usd_price_feed"]
  if len(PriceConsumerV3)==0:
    feeding = PriceConsumerV3.deploy({"from":acc})
  else:
    feeding = PriceConsumerV3[-1]

  a=feeding.getLatestPrice({"from":acc})
  b=feeding.getDecimals({"from":acc})
  c=a/b

  print(c)
