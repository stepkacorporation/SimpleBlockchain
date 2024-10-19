from time import perf_counter

from .block import Block
from .proof_of_work import ProofOfWork
from .transaction import Transaction


class Blockchain:
    def __init__(self):
        self.chain: list[Block] = []
        self.current_transactions: list[Transaction] = []
        self.proof_of_work = ProofOfWork(difficulty=5)

        # Create the genesis block
        self.create_block(previous_hash='x')

    def create_block(self, previous_hash: str = None) -> Block:
        """Create a new block and add it to the chain"""

        block = Block(
            index=len(self.chain) + 1,
            timestamp=perf_counter(),
            transactions=[tx.to_dict() for tx in self.current_transactions],
            previous_hash=previous_hash or self.chain[-1].compute_hash(),
        )

        # Find the nonce value using the Proof of Work algorithm
        self.proof_of_work.mine(block)

        # After finding the nonce, add the block to the chain
        self.current_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender: str, recipient: str, amount: int) -> int:
        """Add a new transaction to the current list"""

        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)

        # Return the index of the block to which the transaction will be added
        return self.last_block.index + 1

    @property
    def last_block(self):
        return self.chain[-1]

    def print_chain(self):
        for block in self.chain:
            print(f'{"Genesis " if block.index == 1 else ""}Block {block.index}')
            print(f'\tBlock Hash: {block.compute_hash()}')
            print(f'\tTimestamp: {block.timestamp}')
            print(f'\tNonce: {block.nonce}')
            print(f'\tTransactions:')

            if block.transactions:
                for tx in block.transactions:
                    print(f'\t\t- {tx["sender"]} -> {tx["recipient"]}: {tx["amount"]}')
            else:
                print('\t\tNo transactions')

            print(f'\tPrevious Hash: {block.previous_hash}')
            print('-' * 40)
