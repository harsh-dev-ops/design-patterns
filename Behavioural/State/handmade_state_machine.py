from enum import Enum, auto


class State(Enum):
    OFF_HOOK = auto()
    ON_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()


class Trigger(Enum):
    CALL_DIALED = auto()
    HUNG_UP = auto()
    CALL_CONNECTED = auto()
    PLACED_ON_HOLD = auto()
    TAKEN_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()


if __name__ == '__main__':
    rules = {
        State.OFF_HOOK: [
            (Trigger.CALL_DIALED, State.CONNECTING)
        ],
        State.CONNECTING: [
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.CALL_CONNECTED, State.CONNECTED)
        ],
        State.CONNECTED: [
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD)
        ],
        State.ON_HOLD: [
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK)
        ]
    }

    exit_state = State.ON_HOOK
    state = State.OFF_HOOK

    while state != exit_state:
        print(f"\nPhone is currently in {state}")

        for i in range(len(rules[state])):
            print(f"{i}: {rules[state][i][0]}")

        idx = int(input("Select a trigger: "))

        state = rules[state][idx][1]

    print("We are done using phone!")
