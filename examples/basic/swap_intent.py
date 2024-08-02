#!/usr/bin/env python3
"""Basic cross-chain swap intent example."""
from sdk.client.hypernova_client import HyperNovaClient

client = HyperNovaClient(api_url="https://api.hypernova.io")

# Create a cross-chain swap intent: swap ETH on Robinhood Chain for USDC on Base
intent = client.create_intent(
    source_chain="robinhood",
    target_chain="base",
    token_in="ETH",
    token_out="USDC",
    amount=10**18,  # 1 ETH
    min_amount_out=2500 * 10**6,  # min 2500 USDC
    deadline=3600,
    reward=10**15  # 0.001 ETH reward for solver
)
print(f"Intent created: {intent['intent_id']}")
