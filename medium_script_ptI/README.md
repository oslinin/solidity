# Summary

## index.js

### init()

1. defi_array_of_objects = await get_all_defi_liquidty_pools
   build_uniswap_V3_USD_volume_and_transaction_object(1)

1. for (const {path,token_ids,pool_addresses,} of
   proftiable_opportunities_intial_check) {
   const loan_pools = determine_loan_pools_of_path(
   token_ids,pool_addresses);
   path_and_loan_pools.push({path, loan_pools});
   }
   profitablity_checks(path_and_loan_pools)
1. proftiable_opportunities_intial_check = check_all_structured_paths(possible_profitable_paths);

V3_Query_USD_volume =
get_uniswap_transactions_by_the_hour_V3
V3_transactions_HourlyObject =
uniswapSubgraph_V3_Api(V3_Query_transactions)
V3_USD_volume_HourlyObject =
uniswapSubgraph_V3_Api(V3_Query_USD_volume)
uniswap_v2 = build_uniswap_V2_USD_volume_and_transaction_object
sushiswap = build_sushiswap_USD_volume_and_transaction_object

madge ./ -i img.png
depcruise --output-type dot apis | dot -T svg > dependency-graph.svg

create doxyfile: doxygen -g

PROJECT*NAME = "Arbitrage Finder"
OUTPUT_DIRECTORY = ./docs
INPUT = ./src ./apis ./profitability_checks
RECURSIVE = YES
EXTRACT_ALL = YES
EXTRACT_PRIVATE = YES
EXTRACT_STATIC = YES
EXTRACT_LOCAL_CLASSES = YES
EXTRACT_LOCAL_METHODS = YES
FILE_PATTERNS = *.js \_.sol
EXTENSION_MAPPING = js=JavaScript
doxygen Doxyfile

# Arbitrage Finder

<br/>

This repository serves as an example of how we implement the search functionality for an arbitrage trading bot using JavaScript. Our primary bot is built on the same principles and tatics outlined in this repository, which are discussed in more detail in our Medium articles. Through this repository, you can learn how to create an effective search function that enables your bot to identify profitable trading opportunities in real-time. So if you're looking to take your arbitrage trading game to the next level, this repository is an excellent resource to help you get started.

<br/>

### Medium Articles

[Intro](https://medium.com/@bgskinner3/flash-loans-the-graph-and-triangular-arbitrage-your-quick-guide-to-profit-in-decentralized-2e1c03aec82)

[Mapping The Trade](https://medium.com/@bgskinner3/flash-loans-the-graph-and-triangular-arbitrage-spot-opportunities-like-tony-soprano-pt-i-3ddc32a08aba)

[Vetting The Trade](https://medium.com/@bgskinner3/flash-loans-the-graph-and-triangular-arbitrage-spot-opportunities-like-tony-soprano-pt-ii-d931cca210ce)

<br/>
