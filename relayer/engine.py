"""Cross-chain relayer engine — monitors and relays intents across chains."""
import asyncio
import aiohttp
from dataclasses import dataclass
from enum import Enum
import time

class RelayStatus(Enum):
    PENDING = "pending"
    IN_FLIGHT = "in_flight"
    CONFIRMED = "confirmed"
    FAILED = "failed"

@dataclass
class RelayTx:
    intent_id: str
    source_chain: str
    target_chain: str
    status: RelayStatus
    source_tx: str = ""
    target_tx: str = ""
    created_at: float = 0.0
    confirmed_at: float = 0.0

class CrossChainRelayer:
    def __init__(self):
        self.relays: dict[str, RelayTx] = {}
        self.confirmed: list[RelayTx] = []
        
    async def relay_intent(self, intent_id: str, source_chain: str, target_chain: str) -> RelayTx:
        tx = RelayTx(intent_id, source_chain, target_chain, RelayStatus.PENDING, created_at=time.time())
        self.relays[intent_id] = tx
        return tx
    
    async def confirm_relay(self, intent_id: str, target_tx: str) -> bool:
        if intent_id in self.relays:
            tx = self.relays[intent_id]
            tx.status = RelayStatus.CONFIRMED
            tx.target_tx = target_tx
            tx.confirmed_at = time.time()
            self.confirmed.append(tx)
            return True
        return False
    
    async def monitor_relays(self) -> list[RelayTx]:
        pending = [r for r in self.relays.values() if r.status == RelayStatus.PENDING]
        for tx in pending:
            tx.status = RelayStatus.IN_FLIGHT
        return pending
    
    def get_stats(self) -> dict:
        return {
            "total": len(self.relays),
            "confirmed": len(self.confirmed),
            "pending": sum(1 for r in self.relays.values() if r.status == RelayStatus.PENDING),
            "failed": sum(1 for r in self.relays.values() if r.status == RelayStatus.FAILED)
        }
