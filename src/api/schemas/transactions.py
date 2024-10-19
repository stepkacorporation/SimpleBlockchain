from pydantic import BaseModel


class TransactionRequest(BaseModel):
    sender: str
    recipient: str
    amount: int
