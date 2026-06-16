class Move:
    def __init__(self, name, move_type, power, category):
        self.name = name
        self.type = move_type
        self.power = power
        self.category = category  # "physical" or "special"


class Pokemon:
    def __init__(self, name, types, moves, hp, atk, spa, spd, def_):
        self.name = name
        self.types = types
        self.moves = moves

        self.max_hp = hp
        self.current_hp = hp

        self.atk = atk
        self.spa = spa
        self.spd = spd
        self.def_ = def_


class Trainer:
    def __init__(self, team):
        if len(team) == 0:
            raise ValueError("Team cannot be empty")

        self.team = team
        self.active = team[0]