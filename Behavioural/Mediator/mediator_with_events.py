from typing import Any


class Events(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)


class GoalScoredInfo:
    def __init__(self, player, total_goals: int):
        self.player = player
        self.total_goals = total_goals


class Game:
    def __init__(self) -> None:
        self.events = Events()

    def fire(self, args):
        self.events(args)


class Player:
    def __init__(self, name: str, game: Game):
        self.name = name
        self.game = game
        self.goal_scored = 0

    def score(self):
        self.goal_scored += 1
        goal_scored_info = GoalScoredInfo(self, self.goal_scored)
        self.game.fire(goal_scored_info)


class Coach:
    def __init__(self, game: Game):
        self.game = game
        self.game.events.append(self.celebrate_goal)

    def celebrate_goal(self, goal_scored_info: GoalScoredInfo):
        if isinstance(goal_scored_info, GoalScoredInfo):
            if goal_scored_info.total_goals < 3:
                print(
                    f'Coach says: well done, {goal_scored_info.player.name}!')
            else:
                print(
                    f'Thumbs up! from coach'
                )


if __name__ == '__main__':
    game = Game()
    player = Player('Messi', game)
    coach = Coach(game)

    player.score()
    player.score()
    player.score()
