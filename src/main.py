from fastapi import FastAPI

from src.api import routers

app = FastAPI()

app.include_router(routers.router_blockchain)
app.include_router(routers.router_transactions)
app.include_router(routers.router_nodes)
