import numpy as np
from blif.Neuron import Neuron
from blif.Axon import Axon

def test_axon_constrcutor():
    n1 = Neuron(1, 1)
    n2 = Neuron(1, 1)

    axon = Axon(n1, n2)

    assert axon in n1.output_axons
    assert axon in n2.input_axons


def test_neuron_recieves_fire():
    n1 = Neuron(1, 1)
    n2 = Neuron(1, 1)

    axon = Axon(n1, n2)

    n1.fire()

    assert n2.activation > 0
    assert n2.current_UHat() > 0