
import random


def montychoose(toSwitch):
    correct = random.randint(0, 2)
    choose = random.randint(0, 2)

    if toSwitch:
        if correct == choose:
            return 0
        else:
            return 1

    if choose == correct:
        return 1
    else:
        return 0


def simulate(n=10000):
    correct = 0
    for i in range(n):
        correct += montychoose(False)

    print("Correct Stay: ", correct/n * 100)

    correct = 0
    for i in range(n):
        correct += montychoose(True)

    print("Correct Switch: ", correct/n * 100)


simulate()
