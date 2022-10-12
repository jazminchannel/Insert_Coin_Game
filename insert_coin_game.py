class Player:
    def __init__(self):
        self.level = 1
        self.health = 10
        self.gold_coins = 0

    def __repr__(self):
        return f'You are at level {self.level}, have {self.gold_coins} gold, and {self.health} health points!'

    def level_up(self):
        self.level += 1

    def collect_treasure(self):
        self.gold_coins += 1
        for i in range((int(self.gold_coins / 10) + 1) - self.level):
            return self.level_up()

    def restart(self):
        return self.__init__()

    def do_battle(self, num_of_battles):
        self.health -= 1 * num_of_battles
        if self.health <= 0:
            return self.restart()
        else:
            return


def main():
    player_1 = Player()
    print(player_1)

    # Testing that the player can collect_treasure 9 times
    for i in range(9):
        player_1.collect_treasure()
    print(player_1)

    # This final treasure should cause the player to level up
    player_1.collect_treasure()
    print(player_1)

    # The player should level up again
    for i in range(10):
        player_1.collect_treasure()
    print(player_1)

    # Testing do_battle
    player_1.do_battle(9)
    print(player_1)

    # This final damage should cause a restart of the game
    player_1.do_battle(1)
    print(player_1)


# Run the game
main()
