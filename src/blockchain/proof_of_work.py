from .block import Block


class ProofOfWork:
    def __init__(self, difficulty: int = 2):
        self.difficulty = difficulty

    def mine(self, block: Block) -> int:
        """Solving the POW problem for this block"""

        nonce = 0
        prefix_str = '0' * self.difficulty

        while True:
            block.nonce = nonce
            block_hash = block.compute_hash()
            if block_hash.startswith(prefix_str):
                print(f'Block {block.index} mined'
                      f'\tBlock Hash: {block_hash}'
                      f'\tNonce: {nonce}')
                return nonce
            nonce += 1
