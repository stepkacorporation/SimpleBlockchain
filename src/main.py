from src.blockchain import Blockchain


def main():
    blockchain = Blockchain()

    blockchain.add_transaction('Alice', 'Bob', 10)
    blockchain.add_transaction('Bob', 'Charlie', 15)

    blockchain.create_block()

    blockchain.add_transaction('Charlie', 'Alice', 5)

    blockchain.create_block()

    blockchain.print_chain()


if __name__ == '__main__':
    main()
