from transaction import Transaction

class ForenBlock():
    """
    This is a block that represents a series of transactions. These transactions are gathered by participating "nodes". In this context, nodes are the devices of individuals involved in the investigation of the case (ie a police force unit). These nodes broadcast "Transactions" and validate them to form a consensus "custody" chain. 
    """
    def __init__(self):
        self.case_id = None
        self.hash_prev_block = None
        self.hash_merkle_root = None
        self.timestamp = None
        self.transactions = None 
