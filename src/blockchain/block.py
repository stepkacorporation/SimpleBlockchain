import hashlib
import json


class Block:
    def __init__(
            self,
            index: int,
            timestamp: float,
            transactions: list[dict],
            previous_hash: str,
            nonce: int = 0,
    ):
        self.index = index
        self.timestamp = timestamp
        self.nonce = nonce
        self.transactions = transactions
        self.previous_hash = previous_hash

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
