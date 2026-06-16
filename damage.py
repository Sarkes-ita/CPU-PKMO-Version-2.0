def type_effectiveness(move_type, defender_types, type_chart):
    multiplier = 1.0

    for t in defender_types:
        multiplier *= type_chart.get(move_type, {}).get(t, 1) # i go inside the dict of types.json and  inside the dict of the move type
 
    return multiplier


def get_attack_stat(move, attacker):
    if move.category == "physical":
        return attacker.atk
    else:
        return attacker.spa


def get_defense_stat(move, defender):
    return defender.def_ if move.category == "physical" else defender.spd


def calculate_damage(move, attacker, defender, type_chart):

    attack = get_attack_stat(move, attacker)
    defense = get_defense_stat(move, defender)

    base = ((2 * 50 / 5 + 2) * move.power * (attack / max(defense, 1))) / 50 + 2 # how dmg works

    stab = 1.5 if move.type in attacker.types else 1.0
    
    type_mult = type_effectiveness(move.type, defender.types, type_chart)

    return base * stab * type_mult