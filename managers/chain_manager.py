import pandas as pd
from models.chain import Chain


class Chain_Manager:

    def __init__(self, datasource):
        self.datasource = datasource
        self.list_chain = []
        self.load_model()

    def load_model(self):
        df = pd.read_csv(self.datasource)
        for index, row in df.iterrows():
            chain = Chain(row['chain_id'], row['chain_name'], row['eq_class'])
            self.list_chain.append(chain)

