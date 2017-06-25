import numpy as np

from blif.Neuron import Neuron
from blif.Cluster import Cluster

"""
Contains the state of a blif network

Uses factory pattern to generate
"""
class Network:

    """
    :param nin number of inputs to the network
    :param nout number of outputs from the network
    """
    def __init__(self, nin, nout):
        self.nin = nin
        self.nout = nout
        self.current_time = 0
        pass


    def run(self):

        idx = 0

        for i, dt in range(0, np.max(self.phi)):
            if len(self.phi) > idx and dt > self.phi[idx]:
                self.input_cluster.fire_inputs(self.A[idx])


    def set_inputs(self, phi, A):
        assert phi.shape == A.shape[0], "first dimension of A must match the length of phi"
        assert self.nin == A.shape[1], "second dimension of A must match number of inputs"

        self.phi = np.array(phi)
        self.A = np.array(A)

    def set_input_cluster(self, cluster):
        assert self.nin == cluster.num_neurons, "Cannot set input cluster of %d neurons in network expecting %d inputs" % (cluster.num_neurons, self.nin)
        self.input_cluster = cluster

    def new_cluster(self, neurons):
        return Cluster(self, neurons)

    def new_neuron(self, epsilon, threshold):
        return Neuron(self, epsilon, threshold)

    def new_axon(self):
        pass


