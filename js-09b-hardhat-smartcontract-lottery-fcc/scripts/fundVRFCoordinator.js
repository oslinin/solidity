const { ethers, network, deployments } = require("hardhat")
const { verify } = require("../utils/verify")
async function fundCoordinator() {
    const { deploy, log } = deployments
    const [deployer] = await ethers.getSigners()
    const chainId = network.config.chainId
    const VRF_COORDINATOR_ADDRESS = "0x1885F9eF4102715bF31cBb804c6e722FeFf27B09"
    const SUBSCRIPTION_ID = "10058"
    if (chainId == 11155111) {
        const vrfCoordinator = await ethers.getContractAt(
            "VRFCoordinatorV2Interface",
            VRF_COORDINATOR_ADDRESS,
            deployer
        )
        const amount = ethers.utils.parseUnits("3", 18)
        const topUpTx = await vrfCoordinator.topUpSubscription(SUBSCRIPTION_ID, amount)
        await topUpTx.wait()
        console.log(`Topped up subscription with ${amount.toString()} LINK`)
    }
}
fundCoordinator()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error("Script failed:", error)
        process.exit(1)
    })
