"""HyperNova SDK — client library for interacting with the HyperNova network."""
import requests
from typing import Optional

class HyperNovaClient:
    def __init__(self, api_url: str = "https://api.hypernova.io", api_key: str = ""):
        self.api_url = api_url.rstrip("/")
        self.api_key = api_key
        
    def create_intent(self, source_chain: str, target_chain: str, token_in: str, token_out: str,
                      amount: int, min_amount_out: int, deadline: int, reward: int) -> dict:
        resp = requests.post(
            f"{self.api_url}/api/v1/intents",
            json={
                "source_chain": source_chain, "target_chain": target_chain,
                "token_in": token_in, "token_out": token_out,
                "amount": amount, "min_amount_out": min_amount_out,
                "deadline": deadline, "reward": reward
            },
            headers={"X-API-Key": self.api_key} if self.api_key else {}
        )
        resp.raise_for_status()
        return resp.json()
    
    def get_intent(self, intent_id: str) -> dict:
        resp = requests.get(f"{self.api_url}/api/v1/intents/{intent_id}")
        resp.raise_for_status()
        return resp.json()
    
    def get_chains(self) -> list[dict]:
        resp = requests.get(f"{self.api_url}/api/v1/chains")
        resp.raise_for_status()
        return resp.json() if isinstance(resp.json(), list) else resp.json().get("chains", [])
    
    def get_stats(self) -> dict:
        resp = requests.get(f"{self.api_url}/api/v1/stats")
        resp.raise_for_status()
        return resp.json()
    
    def estimate(self, source_chain: str, target_chain: str, amount: int, reward: int) -> dict:
        resp = requests.post(
            f"{self.api_url}/api/v1/intents/estimate",
            json={"source_chain": source_chain, "target_chain": target_chain, "amount": amount, "reward": reward}
        )
        resp.raise_for_status()
        return resp.json()
