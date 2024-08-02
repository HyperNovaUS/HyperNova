"""Rate limiting middleware."""
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, requests_per_minute: int = 60):
        self.rpm = requests_per_minute
        self.requests: dict[str, list[float]] = defaultdict(list)
        
    def check(self, client_id: str) -> bool:
        now = time.time()
        self.requests[client_id] = [t for t in self.requests[client_id] if now - t < 60]
        if len(self.requests[client_id]) >= self.rpm:
            return False
        self.requests[client_id].append(now)
        return True
