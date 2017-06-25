import numpy as np

from blif.NetworkComponent import NetworkComponent

class Neuron(NetworkComponent):
    def __init__(self, network, epsilon, threshold):
        super().__init__(network)

        self.prev_fire_time = 0
        self.prev_activation_time = 0

        self.activation = 0
        self.epsilon = epsilon
        self.threshold = threshold

        self.input_axons = []
        self.output_axons = []
        pass

    def current_UHat(self):
        tf = self.network.current_time() - self.prev_fire_time
        return 1 / (1 - np.exp(-tf / self.epsilon))

    def activate(self, alpha):
        tf = self.network.current_time() - self.prev_activation_time

        self.activation = self.activation*np.exp(-tf / self.epsilon) + alpha

        pass

    def fire(self):
        self.prev_fire_time = self.network.current_time()
        for output_axon in self.output_axons:
            output_axon.fire()
        pass

