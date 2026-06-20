document.addEventListener("DOMContentLoaded", () => { /* only run after the DOM is fully loaded */
    buildTeams();
});

function buildTeams() {
    createTeam("player-team", "p", "Player Pokémon");
    createTeam("enemy-team", "e", "Enemy Pokémon");
}

/*Creates 6 Pokémon input cards for either player or enemy team */

function createTeam(containerId, prefix, label) {
    const container = document.getElementById(containerId);

    for (let i = 0; i < 6; i++) { /* let because we want to create a new variable and with the scope of the for loop */
        const pokemonCard = createPokemonCard(prefix, i, label);
        container.appendChild(pokemonCard);
    }
}

/**
 * Creates a single Pokémon input card
 */
function createPokemonCard(prefix, index, label) {
    const card = document.createElement("div");
    card.className = "pokemon-card";

    const title = document.createElement("h3");
    title.textContent = `${label} ${index + 1}`;
    card.appendChild(title); /* because they are element inside other elements, we use appendChild to add them to the card */

    const stats = createStatsSection(prefix, index);
    const moves = createMovesSection(prefix, index);

    card.appendChild(stats);
    card.appendChild(moves);

    return card;
}

/**
 * Creates basic stats inputs
 */
function createStatsSection(prefix, index) {
    const section = document.createElement("div");
    section.className = "stats-section";

    const fields = [
        createInput(prefix, index, "name", "Name"),
        createInput(prefix, index, "types", "Types"),
        createInput(prefix, index, "hp", "HP"),
        createInput(prefix, index, "atk", "ATK"),
        createInput(prefix, index, "spa", "SPA"),
        createInput(prefix, index, "spd", "SPD"),
        createInput(prefix, index, "dfs", "DEF")
    ];

    fields.forEach(el => section.appendChild(el));

    return section;
}

/**
 * Creates moves section (4 moves per Pokémon)
 */

function createMovesSection(prefix, index) {
    const section = document.createElement("div");
    section.className = "moves-section";

    const title = document.createElement("h4");
    title.textContent = "Moves";
    section.appendChild(title);

    for (let i = 0; i < 4; i++) {
        section.appendChild(
            createMoveInputRow(prefix, index, i)
        );
    }

    return section;
}

/**
 * Creates a single stat input
 */
function createInput(prefix, index, field, placeholder) {
    const input = document.createElement("input");
    input.name = `${prefix}_${field}_${index}`;
    input.placeholder = placeholder;
    return input;
}

/**
 * Creates a single move row
 */
function createMoveInputRow(prefix, pokemonIndex, moveIndex) {
    const wrapper = document.createElement("div");
    wrapper.className = "move-row";

    wrapper.innerHTML = `
        <input name="${prefix}_move_name_${pokemonIndex}_${moveIndex}" placeholder="Move Name">
        <input name="${prefix}_move_type_${pokemonIndex}_${moveIndex}" placeholder="Type">
        <input name="${prefix}_move_power_${pokemonIndex}_${moveIndex}" placeholder="Power">
        <input name="${prefix}_move_category_${pokemonIndex}_${moveIndex}" placeholder="Category">
    `;

    return wrapper;
}