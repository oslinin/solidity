// SPDX-License-Identifier: MIT

pragma solidity ^0.8.19;

import {DeployToken} from "../deploy/DeployOurToken.s.sol";
import {Token} from "../contracts/Token.sol";
import {Test, console} from "forge-std/Test.sol";
import {ZkSyncChainChecker} from "lib/foundry-devops/src/ZkSyncChainChecker.sol";

interface MintableToken {
    function mint(address, uint256) external;
}

contract TokenTest is Test, ZkSyncChainChecker {
    uint256 BOB_STARTING_AMOUNT = 100 ether;
    uint256 public constant INITIAL_SUPPLY = 1_000 ether; // 1 million tokens with 18 decimal places

    Token public ourToken;
    DeployToken public deployer;
    address public deployerAddress;
    address bob;
    address alice;

    function setUp() public {
        deployer = new DeployToken();
        if (!isZkSyncChain()) {
            ourToken = deployer.run();
        } else {
            ourToken = new Token("Token", "TOK", INITIAL_SUPPLY);
            ourToken.transfer(msg.sender, INITIAL_SUPPLY);
        }

        bob = makeAddr("bob");
        alice = makeAddr("alice");

        vm.prank(msg.sender);
        ourToken.transfer(bob, BOB_STARTING_AMOUNT);
    }

    function testInitialSupply() public view {
        assertEq(ourToken.totalSupply(), deployer.INITIAL_SUPPLY());
    }

    function testUsersCantMint() public {
        vm.expectRevert();
        MintableToken(address(ourToken)).mint(address(this), 1);
    }

    function testAllowances() public {
        uint256 initialAllowance = 1000;

        // Bob approves Alice to spend tokens on his behalf

        vm.prank(bob);
        ourToken.approve(alice, initialAllowance);
        uint256 transferAmount = 500;

        vm.prank(alice);
        ourToken.transferFrom(bob, alice, transferAmount);
        assertEq(ourToken.balanceOf(alice), transferAmount);
        assertEq(ourToken.balanceOf(bob), BOB_STARTING_AMOUNT - transferAmount);
    }

    // can you get the coverage up?
}