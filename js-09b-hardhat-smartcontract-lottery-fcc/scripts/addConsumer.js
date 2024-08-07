const { ethers } = require("hardhat")
async function addRaffleAsConsumer() {
    const deployer = (await getNamedAccounts()).deployer
    const raffle = await ethers.getContract("Raffle", deployer)
    const vrfCoordinatorAddress = "0x1885f9ef4102715bf31cbb804c6e722feff27b09" // Replace with actual VRFCoordinator address
    const subscriptionId = "12059" // Replace with actual subscription ID
    const vrfCoordinator = await ethers.getContractAt(
        "VRFCoordinatorV2Interface",
        vrfCoordinatorAddress,
        deployer
    )
    const tx = await vrfCoordinator.addConsumer(subscriptionId, raffle.address, {
        gasLimit: 500000,
    })
    await tx.wait()
    console.log(
        `Raffle contract added as consumer to VRFCoordinator with subscription ID: ${subscriptionId}`
    )
    const isValid = await raffle.checkVRFCoordinator()
    console.log(`VRF Coordinator is valid: ${isValid}`)
}

addRaffleAsConsumer()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error("Script failed:", error)
        process.exit(1)
    })
