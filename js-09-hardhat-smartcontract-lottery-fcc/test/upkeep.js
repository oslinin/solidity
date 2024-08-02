const { network } = require("hardhat")
const { verify } = require("../utils/verify")

async function makeCoordinator() {
    const { deploy, log } = deployments
    const { deployer } = await getNamedAccounts()
    const chainId = network.config.chainId
    // If we are on a local development network, we need to deploy mocks!
    if (chainId == 11155111) {
        log("Local network detected! Deploying mocks...")
        raffle = await ethers.getContract("Raffle") // Returns a new connection to the Raffle contract
        const { upkeepNeeded } = await raffle.checkUpkeep("0x") // upkeepNeeded = (timePassed && isOpen && hasBalance && hasPlayers)
        log("upkeepNeeded", upkeepNeeded)
        if (upkeepNeeded == true) {
            const tx2 = await raffle.performUpkeep("0x", { gasLimit: 3000000 })
        }

        log("----------------------------------------------------------")
    }
}

makeCoordinator()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error)
        process.exit(1)
    })
