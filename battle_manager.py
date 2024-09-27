from pokemon_repository import PokemonRepository
from notification_service import NotificationService


class BattleManager:
    def __init__(
        self,
        pokemon_repository: PokemonRepository,
        notification_service: NotificationService,
    ):
        self.pokemon_repository = pokemon_repository
        self.notification_service = notification_service

    def battle(self, pokemon1_name: str, pokemon2_name: str):
        pokemon1 = self.pokemon_repository.get_pokemon(pokemon1_name)
        pokemon2 = self.pokemon_repository.get_pokemon(pokemon2_name)

        if not pokemon1 or not pokemon2:
            self.notification_service.send_notification(
                "Um ou ambos os Pokémons não foram encontrados."
            )
            return

        self.notification_service.send_notification(
            f"Batalha iniciada: {pokemon1.name} vs {pokemon2.name}"
        )

        while not pokemon1.is_fainted() and not pokemon2.is_fainted():
            pokemon2.take_damage(pokemon1.attack)
            self.notification_service.send_notification(
                f"{pokemon1.name} atacou {pokemon2.name} causando {pokemon1.attack} de dano."
            )

            if pokemon2.is_fainted():
                self.notification_service.send_notification(
                    f"{pokemon2.name} desmaiou! {pokemon1.name} venceu!"
                )
                break

            pokemon1.take_damage(pokemon2.attack)
            self.notification_service.send_notification(
                f"{pokemon2.name} atacou {pokemon1.name} causando {pokemon2.attack} de dano."
            )

            if pokemon1.is_fainted():
                self.notification_service.send_notification(
                    f"{pokemon1.name} desmaiou! {pokemon2.name} venceu!"
                )
                break
