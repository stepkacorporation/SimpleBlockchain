from .block import Block


class ProofOfWork:
    def __init__(self, difficulty: int = 2):
        self.difficulty = difficulty

    def mine(self, block: Block) -> int:
        """Solving the POW problem for this block"""

        nonce = 0

        while True:
            block.nonce = nonce
            if self.is_valid_nonce(block):
                print(f'Block {block.index} mined'
                      f'\tBlock Hash: {block.compute_hash()}'
                      f'\tNonce: {nonce}')
                return nonce
            nonce += 1

    def is_valid_nonce(self, block: Block) -> bool:
        """Check if a block's hash is valid based on the PoW difficulty"""

        prefix_str = '0' * self.difficulty
        return block.compute_hash().startswith(prefix_str)
