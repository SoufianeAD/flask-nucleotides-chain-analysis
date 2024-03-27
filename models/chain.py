class Chain:

    def __init__(self, chain_id, chain_name, eq_class):
        self.chain_id = chain_id
        self.chain_name = chain_name
        self.eq_class = eq_class

    def __repr__(self):
        return " ===> self.chain_id: " + str(self.chain_id) + " self.chain_name: " + str(
            self.chain_name) + " eq_class : " + str(self.eq_class)
