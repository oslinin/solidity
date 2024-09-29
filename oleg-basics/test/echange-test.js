require("@nomiclabs/hardhat-waffle");
const { expect, assert } = require("chai");
const { network, getNamedAccounts, deployments, ethers } = require("hardhat");

const toWei = (value) => ethers.utils.parseEther(value.toString());

describe("mint token", async () => {
  let tiken, deployer, user1;
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
    exchange = await ExchangeFactory.deploy(token);
  });
  it("ethers signers", async () => {
    const [deployer1] = await ethers.getSigners();
    expect(await deployer).to.equal(await deployer1.getAddress());
  });

  it("adds liquidity", async () => {
    await token.approve(exchange.address, toWei(200));
    await exchange.addLiquidity(toWei(200), { value: toWei(100) });

    // expect(await getBalance(exchange.address)).to.equal(toWei(100));
    // expect(await exchange.getReserve()).to.equal(toWei(200));
  });
});
