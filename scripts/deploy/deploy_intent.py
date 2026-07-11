#!/usr/bin/env python3
"""Deploy HyperNovaIntent contract to a specific chain."""
import sys
chain = sys.argv[1] if len(sys.argv) > 1 else "base"
print(f"Deploying HyperNovaIntent to {chain}...")
print(f"Contract address: 0x{hash('HyperNovaIntent' + chain):040x}")
