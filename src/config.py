import uuid
from src.blockchain import Blockchain

blockchain = Blockchain()

# ID of the current node
node_id = str(uuid.uuid4()).replace('-', '')

