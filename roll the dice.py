import random

class Dice:
    def roll(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        return die1, die2

class DiceGame:
    def __init__(self):
        self.dice = Dice()

    def start(self):
        print("Welcome to the Roll Dicing game ")
        while True:
            choice = input("Roll the dice ? (y/n) : ").strip().lower()
            if choice == 'y':
                die1, die2 = self.dice.roll()
                print(f'You rolled : ({die1}, {die2})')
            elif choice == 'n':
                print("Thanks for playing ")
                break
            else:
                print("Wrong choice. Enter either 'y' or 'n'. ")

if __name__ == '__main__':
    game = DiceGame()
    game.start()