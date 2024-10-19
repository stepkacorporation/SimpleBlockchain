from pydantic import BaseModel


class NodeAddress(BaseModel):
    address: str


class NodeList(BaseModel):
    nodes: list[NodeAddress]
