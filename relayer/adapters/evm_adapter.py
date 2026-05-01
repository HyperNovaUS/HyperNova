"""Generic EVM chain relayer adapter."""
CHAIN_CONFIGS = {
    "ethereum": {"chain_id": 1, "rpc": "https://eth.llamarpc.com"},
    "base": {"chain_id": 8453, "rpc": "https://mainnet.base.org"},
    "arbitrum": {"chain_id": 42161, "rpc": "https://arb1.arbitrum.io/rpc"},
    "optimism": {"chain_id": 10, "rpc": "https://mainnet.optimism.io"},
}

class EVMRelayerAdapter:
    def __init__(self, chain: str):
        config = CHAIN_CONFIGS.get(chain)
        if not config:
            raise ValueError(f"Unsupported chain: {chain}")
        self.chain = chain
        self.chain_id = config["chain_id"]
        self.rpc_url = config["rpc"]
        
    async def estimate_gas(self, to: str, data: str) -> int:
        return 21000
    
    async def relay_message(self, target: str, payload: bytes, target_chain: str) -> str:
        tx_hash = f"0x{hash(target + str(payload) + target_chain):064x}"
        return tx_hash
    
    def get_chain_id(self) -> int:
        return self.chain_id
