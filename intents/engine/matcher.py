"""Intent matching engine — matches user intents to solver capabilities."""
from dataclasses import dataclass
from typing import Optional
from enum import Enum

class ChainType(Enum):
    ROBINHOOD = "robinhood"
    ETHEREUM = "ethereum"
    BASE = "base"
    ARBITRUM = "arbitrum"
    OPTIMISM = "optimism"
    POLYGON = "polygon"
    VIRTUALS = "virtuals"

@dataclass
class Intent:
    id: str
    user: str
    source_chain: ChainType
    target_chain: ChainType
    token_in: str
    token_out: str
    amount_in: int
    min_amount_out: int
    deadline: int
    reward: int

@dataclass
class Solver:
    address: str
    name: str
    stake: int
    supported_chains: list[ChainType]
    success_rate: float
    
class IntentMatcher:
    def __init__(self):
        self.intents: dict[str, Intent] = {}
        self.solvers: dict[str, Solver] = {}
        
    def register_solver(self, solver: Solver):
        self.solvers[solver.address] = solver
        
    def submit_intent(self, intent: Intent):
        self.intents[intent.id] = intent
        
    def find_best_solver(self, intent_id: str) -> Optional[str]:
        intent = self.intents.get(intent_id)
        if not intent:
            return None
        best = None
        best_score = 0
        for addr, solver in self.solvers.items():
            if intent.target_chain not in solver.supported_chains:
                continue
            if solver.stake < 1000:
                continue
            score = solver.success_rate * 100 + min(solver.stake // 1000, 100)
            if score > best_score:
                best_score = score
                best = addr
        return best
    
    def match_intents(self) -> list[tuple[str, str]]:
        matches = []
        for intent_id in list(self.intents.keys()):
            solver = self.find_best_solver(intent_id)
            if solver:
                matches.append((intent_id, solver))
                del self.intents[intent_id]
        return matches
