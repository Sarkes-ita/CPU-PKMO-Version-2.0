def effectiveness(move_type, enemy_types, type_chart):

    multiplier = 1.0

    for t in enemy_types:
        multiplier *= type_chart.get(move_type, {}).get(t, 1)

    return multiplier


def move_score(move, attacker, defender, type_chart):
    eff = effectiveness(move.type, defender.types, type_chart)
    return move.power * eff


def estimated_damage(move, attacker, defender, type_chart):
    return move_score(move, attacker, defender, type_chart)


def can_ko(move, attacker, defender, type_chart):
    dmg = estimated_damage(move, attacker, defender, type_chart)
    return dmg >= defender.hp * 0.5


def risk_of_staying(defender, attacker, type_chart):
    best_enemy_move = max(
        defender.moves,
        key=lambda m: move_score(m, defender, attacker, type_chart)
    )

    return move_score(best_enemy_move, defender, attacker, type_chart)


def choose_action(trainer, enemy, type_chart):

    attacker = trainer.active
    defender = enemy.active

    
    for move in attacker.moves:
        if can_ko(move, attacker, defender, type_chart):
            return f"ATTACK:{move.name}"

  
    danger = risk_of_staying(defender, attacker, type_chart)

    
    if danger > attacker.hp * 0.4:

        best_switch = None
        best_score = -999

        for pokemon in trainer.team:

            if pokemon == attacker:
                continue

            score = 0

            for move in pokemon.moves:
                score = max(
                    score,
                    move_score(move, pokemon, defender, type_chart)
                )

            if score > best_score:
                best_score = score
                best_switch = pokemon

        return f"SWITCH:{best_switch.name}"

   
    best_move = max(
        attacker.moves,
        key=lambda m: estimated_damage(m, attacker, defender, type_chart)
    )

    return f"ATTACK:{best_move.name}"