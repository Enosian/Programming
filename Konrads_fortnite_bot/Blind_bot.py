import keyboard
# import mouse
import time
import random


def in_game():
    end_time = time.time() + 9
    while(time.time() < end_time):
        keys = {0: "a", 1: "s", 2: "d"}
        key = keys[random.randint(0, 2)]
        duration = random.randint(0, 5)
        # press key
        keyboard.press(key)
        time.wait(duration)


def bus_game():
    pass


def restart_game():
    pass


in_game()
