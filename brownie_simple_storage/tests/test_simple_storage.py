

from brownie import SimpleStorage, accounts

def test_deploy():
    #arrange
    account = accounts[0]
    #act
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve() #view , not ransaction
    expected = 0
    #assert
    assert stored_value == expected

def test_updating_storage():
    #arrange
    account = accounts[0]
    #act
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve() #view , not ransaction
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    expected = 15
    #assert
    assert simple_storage.retrieve() == expected


