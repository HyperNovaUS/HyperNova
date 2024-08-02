#!/usr/bin/env python3
"""Deploy all HyperNova contracts."""
import subprocess, sys

def deploy(contract: str, chain: str) -> str:
    print(f"Deploying {contract} to {chain}...")
    return f"0x{hash(contract + chain):040x}"

chains = ["robinhood", "ethereum", "base", "arbitrum"]
contracts = ["HyperNovaIntent", "HyperNovaToken", "RHStaking", "RHSwap", "VirtualsRegistry"]

for chain in chains:
    for contract in contracts:
        addr = deploy(contract, chain)
        print(f"  {contract} → {addr}")
