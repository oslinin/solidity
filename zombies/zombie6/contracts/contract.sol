pragma solidity ^0.6.0;

//import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";
/*
contract PriceConsumerV3 {
  AggregatorV3Interface public priceFeed;

  constructor() public {
    priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
  }

  function getLatestPrice() public view returns (int) {
    (,int price,,,) = priceFeed.latestRoundData();
    return price;
  }

  function getDecimals() public view returns (uint8) {
    uint8 decimals = priceFeed.decimals();
    return decimals;
  }
}
*/
contract ZombieFactory is VRFConsumerBase {

    uint dnaDigits = 16;
    uint dnaModulus = 10 ** dnaDigits;
    bytes32 public keyHash;
    uint256 public fee;
    uint256 public randomResult;
    struct Zombie {
        string name;
        uint dna;
    }

    Zombie[] public zombies;

    constructor() VRFConsumerBase (
        0x2Ca8E0C643bDe4C2E08ab1fA0da3401AdAD7734D, // VRF Coordinator
        0x326C977E6efc84E512bB9C30f76E30c160eD06FB  // LINK Token
    ) public {
        keyHash = 0x2ed0feb3e7fd2022120aa84fab1945545a9f2ffc9076fd6156fa96eaff4c1311;
        fee = 250000000000000000;
    }

    function _createZombie(string memory _name, uint _dna) private {
        zombies.push(Zombie(_name, _dna));
    }

    function getRandomNumber() public returns (bytes32 requestId) {
        return requestRandomness(keyHash, fee);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        randomResult = randomness;
    }



}
