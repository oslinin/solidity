const { ethers } = require("hardhat")

async function fundCoordinator() {
    const { deploy, log } = deployments
    // const { deployer } = await getNamedAccounts()
    const [deployer] = await ethers.getSigners()
    const chainId = network.config.chainId
    // If we are on a local development network, we need to deploy mocks!
    if (chainId == 11155111) {
        console.log("Local network detected! Deploying mocks...")
        const contract0 = await ethers.getContract("VRFv2SubscriptionManager") // Returns a new connection to the Raffle contract
        const contract = contract0.connect(deployer)
        // const bal = await contract.provider.getBalance(contract.address)
        const accountBalance = await deployer.provider.getBalance(deployer.address)
        console.log(deployer)
        console.log(contract.provider.address)
        console.log(accountBalance.toString())
        // VRFv2SubscriptionManager = raffleContract.connect(deployer)
        const tx2 = await contract.topUpSubscription("3000000000000000000", {
            gasLimit: 3000000,
        })
        log("----------------------------------------------------------")
    }
}

fundCoordinator()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error)
        process.exit(1)
    })
