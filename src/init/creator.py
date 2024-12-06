from objects.creature import Creature

class Creator:
    @staticmethod
    def create_creator(entity) -> Creature:
        player = entity()
        # Логируем
        print(f"{player} Создан")
        return player
