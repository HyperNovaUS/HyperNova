#!/usr/bin/env python3
"""Multi-step agent-driven intent example using Virtuals Protocol."""
from sdk.client.hypernova_client import HyperNovaClient
from intents.solvers.virtuals_solver import VirtualsSolver

client = HyperNovaClient()
agent = VirtualsSolver(agent_id="nova-agent-1", api_key="...")

# Complex intent: bridge RH→Base, swap, provide liquidity
intent = client.create_intent(
    source_chain="robinhood", target_chain="base",
    token_in="ETH", token_out="ETH",
    amount=5 * 10**18, min_amount_out=4.95 * 10**18,
    deadline=7200, reward=5 * 10**15
)

plan = agent.generate_execution_plan(intent)
print(f"Execution plan: {plan}")
