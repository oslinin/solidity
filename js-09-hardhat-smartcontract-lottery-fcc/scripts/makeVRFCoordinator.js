const { ethers, network } = require("hardhat")
const { verify } = require("../utils/verify")

async function makeCoordinator() {
    const { deploy, log } = deployments
    const { deployer } = await getNamedAccounts()
    const chainId = network.config.chainId
    // If we are on a local development network, we need to deploy mocks!
    if (chainId == 11155111) {
        log("Local network detected! Deploying mocks...")
        const manager = await deploy("VRFv2SubscriptionManager", {
            from: deployer,
            log: true,
        })
        await verify(manager.address)

        log("VRFv2SubscriptionManager Deployed!")
        log("----------------------------------------------------------")
    }
}

makeCoordinator()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error)
        process.exit(1)
    })
