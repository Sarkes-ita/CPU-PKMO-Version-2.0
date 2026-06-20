from damage import calculate_damage

def best_move(attacker, defender, type_chart):

    best = None
    best_damage = -1

    for move in attacker.moves:
        dmg = calculate_damage(move, attacker, defender, type_chart)

        if dmg > best_damage:
            best_damage = dmg
            best = move

    return best, best_damage


def choose_action(trainer, enemy, type_chart):

    if not trainer.team or not enemy.team:
        return "INVALID TEAM"

    attacker = trainer.active
    defender = enemy.active

    if not attacker or not defender:
        return "INVALID ACTIVE POKEMON"

    if not attacker.moves:
        return "INVALID TEAM: attacker has no moves"

    best_move = max(
        attacker.moves,
        key=lambda m: calculate_damage(m, attacker, defender, type_chart)
    ) #it tries every move and calculates the damage, then it takes the one that does the most damage

    dmg = calculate_damage(best_move, attacker, defender, type_chart)

    remaining_hp = max(0, defender.current_hp - dmg)

    return f"USE {best_move.name} -> enemy HP: {int(remaining_hp)}"