# SimpleBlockchain

Welcome to **SimpleBlockchain**, a fun (and simple) blockchain project built
with Python and FastAPI! This project is an attempt at creating a basic 
blockchain from scratch, inspired by concepts like Proof of Work (PoW),
decentralized node communication, and transaction handling.

## Features

- **Basic Blockchain**: We’ve implemented a working blockchain with blocks
containing transactions and the previous block’s hash.
- **Proof of Work (PoW)**: The blockchain uses a simple PoW algorithm with
adjustable difficulty to ensure secure block mining.
- **Mining**: You can mine blocks and be rewarded with newly minted coins 
(or tokens)!
- **Transaction Handling**: Create transactions between different "wallets"
and track them in the blockchain.
- **Node Communication**: Nodes can register themselves in the network and
exchange their chains, resolving conflicts by choosing the longest valid chain.
- **FastAPI Integration**: Our blockchain is exposed through a RESTful API
for easy interaction, with endpoints for mining blocks, submitting
transactions, viewing the blockchain, and more.

## Installation

1. Clone the repo:

    ```bash
    git clone https://github.com/stepkacorporation/SimpleBlockchain.git
    cd SimpleBlockchain
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the FastAPI app**:

    ```bash
    uvicorn src.main:app --reload
    ```

## API documentation

API documentation is available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Future Plans

Well... let's be honest. Building a fully functional decentralized blockchain
is **hard**! This project is more like a "blockchain-lite". Who knows, maybe
someday I’ll come back to this project and take it to new heights 🚀! But for
now, let's just say the project is "parked in development" 🙃

Feel free to fork this project and explore new possibilities. Who knows, 
you might be the one to bring SimpleBlockchain to life in exciting new
ways!

Happy coding! ❤️