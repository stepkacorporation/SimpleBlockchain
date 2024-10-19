from time import perf_counter
from urllib.parse import urlparse
from uuid import uuid4

import requests

from .block import Block
from .proof_of_work import ProofOfWork
from .transaction import Transaction


class Blockchain:
    def __init__(self):
        self.chain: list[Block] = []
        self.current_transactions: list[Transaction] = []
        self.proof_of_work: ProofOfWork = ProofOfWork(difficulty=5)
        self.node_id: str = str(uuid4()).replace('-', '')
        self.mining_reward: int = 1
        self.nodes: set = set()

        self.create_genesis_block()

    def create_genesis_block(self):
        """Create a genesis block and add it to the chain"""

        genesis_block = Block(
            index=1,
            timestamp=perf_counter(),
            transactions=[],
            previous_hash='0'
        )
        self.add_block(genesis_block)

    def mine_block(self) -> Block:
        """Create a new block with the addition of a mining reward"""

        # Add a mining reward transaction
        self.add_transaction(sender='0', recipient=self.node_id, amount=self.mining_reward)

        new_block = Block(
            index=len(self.chain) + 1,
            timestamp=perf_counter(),
            transactions=[tx.to_dict() for tx in self.current_transactions],
            previous_hash=self.last_block.compute_hash(),
        )

        # Perform mining a new block
        self.proof_of_work.mine(new_block)

        # Add a new block to the chain and clear current transactions
        self.add_block(new_block)
        self.current_transactions = []
        return new_block

    def add_transaction(self, sender: str, recipient: str, amount: int) -> int:
        """Add a new transaction to the current list"""

        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)

        # Return the index of the block to which the transaction will be added
        return self.last_block.index + 1

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block: Block):
        self.chain.append(block)

    def chain_to_dict(self) -> list[dict]:
        return [block.__dict__ for block in self.chain]

    def register_node(self, address: str):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def is_valid_chain(self, chain: list[dict]) -> bool:
        """Check the validity of the chain"""

        for i in range(1, len(chain)):
            block = Block(**chain[i])
            previous_block = Block(**chain[i - 1])

            # Checking for the correctness of the hash of the previous block
            if block.previous_hash != previous_block.compute_hash():
                return False

            # Checking for the correctness of Proof of Work
            if not self.proof_of_work.is_valid_nonce(block):
                return False

        return True

    def resolve_conflicts(self):
        """Consensus algorithm for node synchronization"""

        neighbours = self.nodes
        new_chain = None

        max_length = len(self.chain)

        for node in neighbours:
            try:
                response = requests.get(f'http://{node}/blockchain/chain')

                if response.status_code == 200:
                    data: dict = response.json()
                    length = data['length']
                    chain = data['chain']

                    if length > max_length and self.is_valid_chain(chain):
                        max_length = length
                        new_chain = chain
            except requests.RequestException as error:
                print(f'Error connecting to the {node} node: {error}')

        if new_chain:
            self.chain = [Block(**block) for block in new_chain]
            return True

        return False

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
