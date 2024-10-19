from fastapi import APIRouter, HTTPException, status

from src.api.schemas import NodeList
from src.config import blockchain

router = APIRouter(prefix='/nodes', tags=['nodes'])


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_nodes(node_list: NodeList):
    nodes = node_list.nodes
    if not nodes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid node list'
        )

    for node in nodes:
        blockchain.register_node(node.address)

    return {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes)
    }


@router.get('/resolve')
async def resolve_conflicts():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        return {'message': 'Our chain was replaced', 'new_chain': blockchain.chain_to_dict()}
    else:
        return {'message': 'Our chain is authoritative', 'chain': blockchain.chain_to_dict()}
