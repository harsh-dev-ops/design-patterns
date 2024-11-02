from abc import ABC
from collections.abc import Iterable
from typing import Iterator


class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name: str):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __iter__(self) -> Iterator:
        yield self

    def __str__(self) -> str:
        return f"{self.name}, {len(self.inputs)} inputs," + \
            f"{len(self.outputs)} outputs"


class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for i in range(1, count+1):
            neuron = Neuron(f"{name}_neuron_{i}")
            self.append(neuron)

    def __str__(self) -> str:
        return f"{self.name} with {len(self)} neuron"


if __name__ == "__main__":
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')
    output_neuron = Neuron('output_neuron')

    neuron_layer1 = NeuronLayer('l1', 4)
    neuron_layer2 = NeuronLayer('l2', 10)

    neuron1.connect_to(neuron2)
    neuron2.connect_to(neuron_layer1)
    neuron_layer1.connect_to(neuron_layer2)
    neuron_layer2.connect_to(output_neuron)

    print(neuron1)
    print(neuron2)
    print(neuron_layer1)
    print(neuron_layer2)
    print(output_neuron)
