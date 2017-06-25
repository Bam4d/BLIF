from blif.NetworkComponent import NetworkComponent


"""

"""
class Axon(NetworkComponent):

    def __init__(self, network, originating_neuron, target_neuron, alpha=1):
        super().__init__(network)

        originating_neuron.output_axons.append(self)
        target_neuron.input_axons.append(self)
        self.post_synaptic_neuron = target_neuron
        self.alpha = alpha
        pass

    def fire(self):
        self.post_synaptic_neuron.activate(self.alpha)