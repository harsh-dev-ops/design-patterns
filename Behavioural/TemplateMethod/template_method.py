from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.current_player = 0

    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()

        print(f"We have a winner Player {self.winning_player}")

    @property
    @abstractmethod
    def have_winner(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def take_turn(self):
        pass

    @property
    @abstractmethod
    def winning_player(self):
        pass


class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.max_turns = 11
        self.turn = 1

    def start(self):
        print(f"Starting the Game of Chess with {self.number_of_players}")

    @property
    def have_winner(self):
        return self.turn == self.max_turns

    @property
    def winning_player(self):
        return self.current_player

    def take_turn(self):
        print(f"Player {self.current_player} took turn {self.turn}")

        self.turn += 1

        self.current_player = 1 - self.current_player


if __name__ == '__main__':
    chess = Chess()
    chess.run()
