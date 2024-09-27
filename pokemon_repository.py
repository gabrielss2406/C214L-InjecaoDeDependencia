from pokemon import Pokemon


class PokemonRepository:
    def __init__(self):
        self.pokemons = {}

    def add_pokemon(self, pokemon: Pokemon):
        """Adiciona um Pokémon ao repositório."""
        self.pokemons[pokemon.name] = pokemon

    def get_pokemon(self, name: str) -> Pokemon:
        """Recupera um Pokémon pelo nome, ou None se não existir."""
        return self.pokemons.get(name)
