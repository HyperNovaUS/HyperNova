"""Proximity solver — finds optimal execution paths using on-chain liquidity proximity."""
from dataclasses import dataclass

@dataclass
class SolverBid:
    solver_id: str
    amount_out: int
    fee: int
    estimated_time: int
    confidence: float

class ProximitySolver:
    def __init__(self):
        self.liquidity_sources = {}
        
    def add_liquidity(self, chain: str, token: str, amount: int):
        key = f"{chain}:{token}"
        self.liquidity_sources[key] = amount
        
    def calculate_best_path(self, token_in: str, token_out: str, amount: int, chains: list) -> list:
        paths = []
        for chain in chains:
            liq_in = self.liquidity_sources.get(f"{chain}:{token_in}", 0)
            liq_out = self.liquidity_sources.get(f"{chain}:{token_out}", 0)
            if liq_in >= amount and liq_out >= amount:
                paths.append({"chain": chain, "slippage": 0.003, "steps": 1})
        return sorted(paths, key=lambda p: p["slippage"])
    
    def generate_bid(self, intent, solver_address: str) -> SolverBid:
        path = self.calculate_best_path(
            intent.token_in, intent.token_out, intent.amount_in,
            ["robinhood", "base", "ethereum"]
        )
        if not path:
            return None
        return SolverBid(
            solver_id=solver_address,
            amount_out=int(intent.amount_in * (1 - path[0]["slippage"])),
            fee=intent.reward,
            estimated_time=path[0]["steps"] * 30,
            confidence=0.95
        )
