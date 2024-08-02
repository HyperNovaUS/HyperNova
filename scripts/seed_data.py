#!/usr/bin/env python3
"""Seed demo data."""
import json
data = {
    "intents": [
        {"id": "0x1a2b3c", "user": "0xabcd", "source": "robinhood", "target": "base", "amount": "2.5", "status": "fulfilled"},
        {"id": "0x4d5e6f", "user": "0xef01", "source": "ethereum", "target": "arbitrum", "amount": "1.2", "status": "pending"},
    ],
    "solvers": [
        {"address": "0x1111", "name": "alpha-solver", "stake": 10000},
        {"address": "0x2222", "name": "beta-solver", "stake": 5000},
    ]
}
with open("/tmp/hypernova_seed.json", "w") as f:
    json.dump(data, f, indent=2)
print("Seed data written")
