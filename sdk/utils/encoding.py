import hashlib

def encode_intent_id(user: str, nonce: int) -> str:
    return '0x' + hashlib.sha256(f'{user}:{nonce}'.encode()).hexdigest()
