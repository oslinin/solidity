from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]
    #account = accounts.load("freecodecamp-account")
    #account = accounts.add(os.getenv("PRIVATE_KEY"))
    #account = accounts.add(config["wallets"]["from_key"]) #brwonie-config.yaml
    simple_storage = SimpleStorage.deploy({"from": account})
    print(account)


def main():
    deploy_simple_storage()

#brownie accounts new freecodecamp-account
#password og
#brownie accounts list
#brownie accounts delete

#third way brownie-config.yaml from .env