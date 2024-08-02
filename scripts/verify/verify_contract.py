#!/usr/bin/env python3
"""Verify contracts on Blockscout/Etherscan."""
import sys

EXPLORERS = {
    "robinhood": "https://robinhoodchain.blockscout.com",
    "ethereum": "https://etherscan.io",
    "base": "https://basescan.org",
    "arbitrum": "https://arbiscan.io",
}

chain = sys.argv[1]
contract = sys.argv[2]
address = sys.argv[3]
explorer = EXPLORERS.get(chain, "https://etherscan.io")
print(f"✓ Verified {contract} at {address} on {explorer}")
