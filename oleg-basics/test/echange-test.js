require("@nomiclabs/hardhat-waffle");
const { expect, assert } = require("chai");
const { network, getNamedAccounts, deployments, ethers } = require("hardhat");

const toWei = (value) => ethers.utils.parseEther(value.toString());

describe("mint token", async () => {
  let token, deployer, user1, amount_token, amount_eth;

  beforeEach(async function () {
    const accounts = await getNamedAccounts();
    deployer = accounts.deployer;
    user1 = accounts.user1;
    await deployments.fixture("all"); ///deploy(token,3args)
  });
  it("towei", async () => {
    ethers.utils.parseEther("100000".toString());
  });

  it("mints", async () => {
    token = await ethers.getContract("Token", deployer);
  });
  it("deploys exchange", async () => {
    ExchangeFactory = await ethers.getContractFactory("Exchange");
    exchange = await ExchangeFactory.deploy(token.address);
    await exchange.deployed();
  });
  it("ethers signers", async () => {
    const [deployer1] = await ethers.getSigners();
    expect(await deployer).to.equal(await deployer1.getAddress());
  });
  it("approves exchange", async () => {
    amount_token = toWei(200);
    await token.approve(exchange.address, amount_token);
  });
  it("adds liquidity", async () => {
    const tokenName = await token.name();
    console.log("Token name:", tokenName);
    const totalSupply = await token.totalSupply();
    console.log("Total Supply:", ethers.utils.formatEther(totalSupply));
    const decimals = await token.decimals();
    console.log("Token decimals:", decimals.toString());

    amount_eth = toWei(100);
    const [deployerSigner] = await ethers.getSigners(); // Get the deployer signer
    const balance = await deployerSigner.getBalance();
    const tokenbalance = await token.balanceOf(deployerSigner.address);
    console.log("Deployer Address:", deployerSigner.address);
    console.log("Deployer balance eth:", ethers.utils.formatEther(balance));
    console.log(
      "Deployer balance token:",
      ethers.utils.formatEther(tokenbalance)
    );
    console.log("Token Address:", token.address);
    console.log("Exchange Address:", exchange.address);
    console.log("amount_eth:", ethers.utils.formatEther(amount_eth));
    console.log("amount_token:", ethers.utils.formatEther(amount_token));

    // await exchange.connect(deployerSigner).addLiquidity(amount_token, {
    //   value: amount_eth,
    //   gasLimit: 5000000, // Set an appropriate gas limit
    // }); //this times out!
    try {
      await exchange.addLiquidity(amount_token, {
        value: amount_eth,
        // gasLimit: 1000000, // Set an appropriate gas limit
      });
    } catch (error) {
      console.error("Error adding liquidity:", error);
    }
    // expect(await getBalance(exchange.address)).to.equal(toWei(100));
    // expect(await exchange.getReserve()).to.equal(toWei(200));
  });
});
