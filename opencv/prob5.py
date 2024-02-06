import random

def chose_color(all, color):
    while(True):
        print(all)
        choice = input("Guess a color: ")
        if color == choice:
            print("Well Done")
            return
        else:
            print("I ber you are {} in envy!".format(choice))

color = ['Red', 'Green', 'Blue', 'Yellow', 'Pink', 'Purple']

choice = random.choice(color)

chose_color(color, choice)
