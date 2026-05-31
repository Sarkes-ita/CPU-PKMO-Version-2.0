
from loader import load_types
from engine import choose_action
from input_builder import create_pokemon
from models import Trainer, Move, Pokemon

# -----------------------------

type_chart = load_types()

print("--- CREATE YOUR TEAM ---")

team_size = int(input("How many pokemons? "))

team = []

for _ in range(team_size):
    team.append(create_pokemon())

player = Trainer(team)
player.active = player.team[0]


print("\n--- CREATE ENEMY'S TEAM ---")

enemy_team = [create_pokemon()]

enemy = Trainer(enemy_team)
enemy.active = enemy.team[0]

# -----------------------------
# ▶️ RUN
# -----------------------------

print("\n--- CPU RESPONE ---")

print(
    choose_action(player, enemy, type_chart)
)