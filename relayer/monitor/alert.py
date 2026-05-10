"""Relayer alerting system."""
class RelayerAlert:
    def __init__(self):
        self.alerts = []
        
    def send_alert(self, level: str, message: str, chain: str = ""):
        alert = {"level": level, "message": message, "chain": chain}
        self.alerts.append(alert)
        print(f"[{level.upper()}] {chain}: {message}" if chain else f"[{level.upper()}] {message}")
        
    def get_recent_alerts(self, n: int = 10) -> list:
        return self.alerts[-n:]
    
    def send_success(self, msg: str): self.send_alert("success", msg)
    def send_warning(self, msg: str, chain: str = ""): self.send_alert("warning", msg, chain)
    def send_error(self, msg: str, chain: str = ""): self.send_alert("error", msg, chain)
