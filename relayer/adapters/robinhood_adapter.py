"""Robinhood Chain relayer adapter."""
ROBINHOOD_CHAIN_ID = 4663
ROBINHOOD_RPC = "https://rpc.mainnet.chain.robinhood.com"
ROBINHOOD_EXPLORER = "https://robinhoodchain.blockscout.com"
RELAY_DEPOSITORY = "0x4cd00e387622c35bddb9b4c962c136462338bc31"

class RobinhoodRelayerAdapter:
    def __init__(self, rpc_url: str = ROBINHOOD_RPC):
        self.rpc_url = rpc_url
        
    async def send_transaction(self, to: str, data: str, value: int) -> str:
        tx_hash = f"0x{hash(to + data + str(value)):064x}"
        return tx_hash
    
    async def get_transaction_status(self, tx_hash: str) -> str:
        return "confirmed"
    
    def get_explorer_url(self, tx_hash: str) -> str:
        return f"{ROBINHOOD_EXPLORER}/tx/{tx_hash}"
