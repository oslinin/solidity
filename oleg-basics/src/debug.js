require("@nomiclabs/hardhat-waffle");
const { expect, assert } = require("chai");
const { network, getNamedAccounts, deployments, ethers } = require("hardhat");
const {
  developmentChains,
  INITIAL_SUPPLY,
} = require("../helper-hardhat-config");

const toWei = (value) => ethers.utils.parseEther(value.toString());

// module.exports = async ({ getNamedAccounts, deployments }) => {
async function oleg_debug() {
  const accounts = await getNamedAccounts();
  const deployer = accounts.deployer;
  const user1 = accounts.user1;

  const { deploy, log } = deployments;
  // const { deployer } = await getNamedAccounts();
  // const ourToken = await deploy("Token", {
  //   from: deployer,
  //   args: ["OurToken", "OT", INITIAL_SUPPLY],
  //   log: true,
  //   // we need to wait if on a live network so we can verify properly
  //   waitConfirmations: network.config.blockConfirmations || 1,
  // });
  // log(`ourToken deployed at ${ourToken.address}`);
  // await deployments.fixture("all");

  const token = await ethers.getContract("Token", deployer);
  console.log("Token deployed at", token.address);
}

oleg_debug()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("Script failed:", error);
    process.exit(1);
  });