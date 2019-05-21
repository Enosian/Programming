import keyboard
# import mouse
import time
import random


def in_game():
    end_time = time.time() + 900
    while(time.time() < end_time):
        keys = {0: "a", 1: "s", 2: "d"}
        key = keys[random.randint(0, 2)]
        duration = random.randint(0, 5)
        # press key
        keyboard.press(key)
        time.sleep(duration)
        keyboard.release(key)
        keyboard.press("w")
        time.sleep(duration)
        keyboard.release("w")


def bus_game():
    pass


def restart_game():


in_game()
