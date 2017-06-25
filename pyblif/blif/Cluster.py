from blif.NetworkComponent import NetworkComponent
from blif.Neuron import Neuron

"""
Container for groups of neurons
"""
class Cluster(NetworkComponent):

    def __init__(self, network, num_neurons):
        super().__init__(network)

        self.num_neurons = num_neurons
        self.neurons = []

    def initialize(self):

        for i in range(0, self.num_neurons):
            #TODO: initialization functions for epsilon and threshold

            epsilon = 30
            threshold = 1
            self.neurons.append(Neuron(self.network, epsilon, threshold))

    def add_neuron(self, neuron):
        self.neurons.append(neuron)

    def fire_inputs(self, alphas):
        assert alphas.shape[0] == len(self.neurons), "the array of input spikes [alpha] must have the same length as " \
                                                    "the number of neurons in the cluster"

        for i, alpha in alphas:
            self.neurons[i].activate(alpha)
