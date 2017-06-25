"""
A super class of components within a blif network
"""
class NetworkComponent:

    def __init__(self, network):
        self.network = network
        pass

    def initialize(self):
        pass

    def get_params(self):
        pass

    def load_params(self):
        pass