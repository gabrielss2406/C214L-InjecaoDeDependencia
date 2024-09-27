from pokemon_repository import PokemonRepository
from notification_service import NotificationService
from battle_manager import BattleManager
from pokemon import Pokemon

# Criando instâncias dos serviços e repositórios
pokemon_repository = PokemonRepository()
notification_service = NotificationService()

# Adicionando Pokémons ao repositório
pokemon_repository.add_pokemon(Pokemon("Pikachu", hp=100, attack=50))
pokemon_repository.add_pokemon(Pokemon("Charmander", hp=80, attack=60))
pokemon_repository.add_pokemon(Pokemon("Squirtle", hp=90, attack=40))

# Injetando dependências no BattleManager
battle_manager = BattleManager(pokemon_repository, notification_service)

# Executando uma batalha
battle_manager.battle("Pikachu", "Charmander")
