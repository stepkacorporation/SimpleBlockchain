from fastapi import APIRouter

from src.api.schemas import TransactionRequest
from src.config import blockchain

router = APIRouter(prefix='/transactions', tags=['transactions'])


@router.post('/new')
async def new_transaction(tx: TransactionRequest):
    index = blockchain.add_transaction(tx.sender, tx.recipient, tx.amount)
    return {'message': f'Transaction will be added to block {index}'}

