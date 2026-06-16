from flask import Flask, render_template, request
from engine import choose_action
from loader import load_types
from models import Pokemon, Trainer, Move

app = Flask(__name__) #it creates the web server
type_chart = load_types()


def build_team(prefix):
    team = []

    for i in range(6):
        name = request.form.get(f"{prefix}_name_{i}")

        # skip if name is empty or only whitespace
        if not name or name.strip() == "":
            continue

        types = request.form.get(f"{prefix}_types_{i}", "")
        hp = request.form.get(f"{prefix}_hp_{i}")
        atk = request.form.get(f"{prefix}_atk_{i}")
        spa = request.form.get(f"{prefix}_spa_{i}")
        spd = request.form.get(f"{prefix}_spd_{i}")
        dfs = request.form.get(f"{prefix}_dfs_{i}")

        moves = []
        for j in range(4):
            move_name = request.form.get(f"{prefix}_move_name_{i}_{j}", "").strip()
            move_type = request.form.get(f"{prefix}_move_type_{i}_{j}", "").strip().lower() #lower bcs of the type chart
            move_power = request.form.get(f"{prefix}_move_power_{i}_{j}")
            move_category = request.form.get(f"{prefix}_move_category_{i}_{j}", "").strip().lower()

            if not move_name:
                continue

            try:
                power = int(move_power) if move_power else 0
                moves.append(Move(move_name, move_type, power, move_category))
            except ValueError:
                continue

        if not moves:
            continue

        try:
            pokemon = Pokemon(
                name,
                types.split() if types else [], #it splits the types by space, if there are no types it gives an empty list
                moves,
                int(hp) if hp else 0,
                int(atk) if atk else 0,
                int(spa) if spa else 0,
                int(spd) if spd else 0,
                int(dfs) if dfs else 0,
            )
        except ValueError:
            continue  # if invalid datas are given, skip this pokemon

        team.append(pokemon)

    return team



@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    player_team = []
    enemy_team = []

    if request.method == "POST":
        player_team = build_team("p") #to distinct the player team from the enemy team
        enemy_team = build_team("e")

        if len(player_team) == 0 or len(enemy_team) == 0:
            return render_template("index.html", result="Error: input at least 1 Pokémon for each team.")

        player = Trainer(player_team)
        enemy = Trainer(enemy_team)

        player.active = player.team[0] if player.team else None
        enemy.active = enemy.team[0] if enemy.team else None

        result = choose_action(player, enemy, type_chart)

    return render_template("index.html", result=result) #passes the variable result to the template, which will display it in the browser


if __name__ == "__main__": #it runs the web server, debug=True means that it will automatically reload if you change the code and it will show you error messages in the browser
    app.run(debug=True)


