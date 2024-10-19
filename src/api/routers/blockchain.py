from fastapi import APIRouter

from src.config import blockchain

router = APIRouter(prefix='/blockchain', tags=['blockchain'])


@router.get('/chain')
async def get_chain():
    return {
        'length': len(blockchain.chain),
        'chain': blockchain.chain_to_dict()
    }


@router.get('/mine')
async def mine_block():
    block = blockchain.mine_block()
    return {
        'message': 'New Block mined',
        'block': block.__dict__
    }
