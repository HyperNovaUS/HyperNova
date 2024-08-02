"""Dashboard chart components."""
import json

def volume_chart(data: list[dict]) -> str:
    return json.dumps({"type": "volume", "data": data})

def solver_chart(data: list[dict]) -> str:
    return json.dumps({"type": "solver_performance", "data": data})
