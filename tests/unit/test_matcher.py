import pytest
from intents.engine.matcher import IntentMatcher, Intent, Solver, ChainType

def test_solver_matching():
    matcher = IntentMatcher()
    solver = Solver("0x1", "test-solver", 5000, [ChainType.BASE, ChainType.ETHEREUM], 0.95)
    matcher.register_solver(solver)
    intent = Intent("intent-1", "0xuser", ChainType.ROBINHOOD, ChainType.BASE, "ETH", "USDC", 1000, 990, 1000000, 100)
    matcher.submit_intent(intent)
    best = matcher.find_best_solver("intent-1")
    assert best == "0x1"
