
class Pokemon:
    def __init__(self, name, types, moves, hp):
        self.name = name
        self.types = types
        self.moves = moves
        self.hp = hp


class Move:
    def __init__(self, name, move_type, power):
        self.name = name
        self.type = move_type
        self.power = power


class Trainer:
    def __init__(self, team):
        self.team = team
        self.active = team[0]  # first pokemon is active by default

class Trainer:
    def __init__(self, team):
        self.team = team
        self.active = team[0]  # first pokemon is active by default