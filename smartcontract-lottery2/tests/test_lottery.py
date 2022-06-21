#.019 eth is $50

from brownie import Lottery, accounts, network, config
from web3 import Web3
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
def test_get_entrance_fee():
    account = get_account()
    deploy_mocks()
    addr = config["networks"][network.show_active()]["eth_usd_price_feed"];
    lottery = Lottery.deploy(addr,{"from":account} );
    #lottery = Lottery.deploy(config["networks"][network.show_active()]["eth_usd_price_feed"],{"from":accounts[0]} );
    assert(lottery.getEntranceFee() > Web3.toWei(0.018, "ether"));
    assert(lottery.getEntranceFee() > Web3.toWei(0.022, "ether"));