import networkx as nx

import pandas as pd
from models.nucleotide import Nucleotid
from pyvis.network import Network


class Nucleotide_Manager:
    def __init__(self, datasource):
        self.datasource = datasource
        self.list_nucleotide = []
        self.tuples = []
        self.load_model()

    def get_pair_type_LW(self, types):
        ll = []
        for item in types:
            sublist = str(item).split(',')
            if (len(sublist) > 1):
                for item2 in sublist:
                    if (str(item2)) not in ll:
                        ll.append(str(item2))
            else:
                if (str(item)) not in ll:
                    ll.append(str(item))
        return ll

    def get_items(self, types):
        ll = list()
        tab = str(types).split(',')

        if (len(tab) > 1):
            return tab
        return str(types)

    def load_model(self):
        df = pd.read_csv(self.datasource)
        for index, row in df.iterrows():
            nucleotid = Nucleotid(row['chain_id'], row['index_chain'], self.get_items(
                row['paired']), self.get_items(row['pair_type_LW']))
            self.list_nucleotide.append(nucleotid)
            # it's better to create tuples the first time when we are creating our nucleotides = earn of N iterations
            if nucleotid.index_chain != 1:
                self.tuples.append(tuple((str(nucleotid.index_chain - 1), str(nucleotid.index_chain))))
            pairs = self.get_pairs(nucleotid)
            for pair in pairs:
                if (None != pair and not self.check_if_exist(pair.index_chain)):
                    self.tuples.append(
                        tuple((str(nucleotid.index_chain), str(pair.index_chain))))

    def get_nucleotid_by_chain_index(self, index):
        for item in self.list_nucleotide:
            if (str(item.index_chain) == str(index)):
                return item
        return None

    def check_if_exist(self, tup):
        return tup in self.tuples

    def get_pairs(self, nucleotide):
        pairs = nucleotide.paired
        ll = []
        for item in pairs:
            ll.append(self.get_nucleotid_by_chain_index(item))
        return ll

    def drw_nucleotides(self):
        nx_graph = nx.DiGraph()
        nx_graph.add_edges_from(self.tuples)
        # nx_graph.add_edge(20, 21, weight=10)
        nt = Network("90%", "99.96%")
        # populates the nodes and edges data structures
        nt.from_nx(nx_graph)
        nt.heading = "Nucleotids"
        nt.show_buttons(filter_=['physics'])
        nt.show("nx.html")

