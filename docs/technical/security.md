# Security Model

## Multi-Sig
Core contracts require 3/5 multi-sig for upgrades.

## Solver Staking
Min stake: 1000 NOVA
Slashing conditions:
- Failed execution: 10% stake
- Malicious behavior: 100% slashing

## Rate Limiting
API: 60 req/min per key
Solver: 100 executions/day
