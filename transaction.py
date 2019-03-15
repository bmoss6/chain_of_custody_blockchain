import hashlib
import json
class Transaction():
    """
This class represents the artifact being transitioned from one state to another. At the beginning of evidence collection, a genesis "block" is created with one or more "Transactions" with no inputs and only outputs relating to the public key ID of the collecting individual/entity. Subsequently, as the evidence is transitioned to other individuals/entities, it is "released" by the current owner of the artifact via another "transaction" that transitions "ownership" of the artifact to another individual/entity by specifying that individual/entity's public key(s) in the output of the transaction.     
    """
    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.artifact_hash = None
        self.artifact_description = None   
        self.id = self.hash()

    def __str__(self):
        return json.dumps({"id":self.id, "ins":self.inputs, "outs":self.outputs, "artifact_hash":self.artifact_hash})

    def hash(self):
        m = hashlib.sha256()
        m.update(str(self).encode('utf-8'))
        return m.hexdigest()

