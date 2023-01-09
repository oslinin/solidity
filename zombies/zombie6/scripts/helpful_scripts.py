
from brownie import (
    accounts, 
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

def get_contract(contract_name):
    """This function will grab the contract addresses from the brownie config
    if defined, otherwise, it will deploy a mock version of that contract, and
    return that mock contract.

        Args:
            contract_name (string)

        Returns:
            brownie.network.contract.ProjectContract: The most recently deployed
            version of this contract.
    """
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:
            # MockV3Aggregator.length
            deploy_mocks()
        contract = contract_type[-1]
        # MockV3Aggregator[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        # address
        # ABI
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
        # MockV3Aggregator.abi
    return contract


DECIMALS = 8
INITIAL_VALUE = 200000000000


def print1(feeding,acc):
  for j in range(3):
      for i in feeding.getZombiesByOwner(acc[j]):
        print(f"zombie {i}: {feeding.zombies(i)} owner: {feeding.zombieToOwner(i)}")  
    
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
  
  if len(ZombieOwnership)==0:
    print("deploying first time")
    feeding = ZombieOwnership.deploy({"from":account})
    feeding.setKittyContractAddress("0x06012c8cf97BEaD5deAe237070F9587f8E7A266d",{"from":account})
    feeding.createRandomZombie("oleg", {"from":account})
    print(f"ZombieFeeding deployed to {feeding.address}")
  else:
    print("found Zombiefeeding, returning it")
    feeding = ZombieOwnership[-1]
    print("end deploy_contracts()")
  return(feeding)


  