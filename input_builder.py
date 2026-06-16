from models import Pokemon, Move

def create_move():
    name = input("Move name: ")
    move_type = input("Move type: ").lower()
    power = int(input("Power: "))
    category = input("Category (physical/special): ").lower()

    return Move(name, move_type, power, category)

def create_pokemon():
    name = input("\nPokémon name: ")
    types = input("Types (space separated): ").lower().split()

    hp = int(input("HP: "))
    atk = int(input("Attack: "))
    spa = int(input("Sp. Attack: "))
    spd = int(input("Sp. Defense: "))
    spe = int(input("Speed: "))

    moves = []

    n = int(input("How many moves? "))

    for _ in range(n):
        moves.append(create_move())

    return Pokemon(name, types, moves, hp, atk, spa, spd, spe)