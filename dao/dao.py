import sqlite3
import pandas as pd


class Dao:

    def __init__(self, datasource):
        self.datasource = datasource

    def load_chain_by_id(self, chain_id):
        connection = sqlite3.connect(self.datasource)
        df = pd.read_sql_query('SELECT chain_id,index_chain, paired,pair_type_LW FROM nucleotide where chain_id =?;',
                               connection, params=[str(chain_id)])
        df.to_csv("nucleotides.csv")
        connection.close()

    def load_chains(self):
        connection = sqlite3.connect(self.datasource)
        df = pd.read_sql("""SELECT chain_id, chain_name, eq_class
                                FROM chain ;""", con=connection)
        df.to_csv("chains.csv")
        connection.close()



