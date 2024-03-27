class Nucleotid:
    def __init__(self, chain_id, index_chain, paired, paired_type):
        self.chain_id = chain_id
        self.index_chain = index_chain
        # paired and paired_type are  list
        if type(paired) == type(list()):
            self.paired = paired
        else:
            self.paired = []
            self.paired.append(paired)
        if type(paired_type) == type(list()):
            self.paired_type = paired
        else:
            self.paired_type = []
            self.paired_type.append(paired_type)

    def __repr__(self):
        return " ===> self.chain_id: " + str(self.chain_id) + " self.index_chain: " + str \
            (self.index_chain) + " paired : " + str(self.paired) + " self.paired_type: " + str(self.paired_type)
