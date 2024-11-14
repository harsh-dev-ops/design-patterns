from abc import ABC


class Switch:
    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


class State(ABC):
    def on(self, switch: Switch):
        print("Light is already on!")

    def off(self, switch: Switch):
        print("Light is already off!")


class OffState(State):
    def on(self, switch: Switch):
        print("Turning Light on...")
        switch.state = OnState()


class OnState(State):
    def off(self, switch: Switch):
        print("Turning Light off...")
        switch.state = OffState()


if __name__ == '__main__':
    sw = Switch()

    sw.on()

    sw.off()

    sw.on()

    sw.on()
    sw.off()
    sw.off()
