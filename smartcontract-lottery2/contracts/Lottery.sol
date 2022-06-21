// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;
//https://docs.chain.link/docs/get-the-latest-price/
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract Lottery {
    address payable[] public players;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUsdPriceFeed;

    constructor(address _priceFeedAddress) public {
        usdEntryFee = 50 * (10**18);
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    function getfeed() public view returns (AggregatorV3Interface) {
        return ethUsdPriceFeed;
    }

    function getVersion() public view returns (uint256) {
        return ethUsdPriceFeed.version();
    }

    function enter() public payable {
        //$50 min
        //require()
        //players.push(msg.sender);
    }

    // https://docs.chain.link/docs/ethereum-addresses/ 8 decimals
    function getEntranceFee() public view returns (uint256) {
        (, int256 price, , , ) = ethUsdPriceFeed.latestRoundData();
        uint256 adjustedPrice = uint256(price) * 10**10; // 18 decimals
        // $50, $2,000 / ETH
        // 50/2,000
        // 50 * 100000 / 2000
        uint256 costToEnter = (usdEntryFee * 10**18) / adjustedPrice;
        return costToEnter;
    }

    function startLottery() public {}

    function endLottery() public {}
}
