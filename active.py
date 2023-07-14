#!/usr/bin/env python3

import argparse
import time
from datetime import datetime
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import random
import pyautogui

mouse = MouseController()
keyboard = KeyboardController()

def press_keys():
    keys = [Key.shift, Key.alt_l, Key.ctrl_l, Key.down, Key.end, Key.home, Key.left]  # list of keys
    num_key_presses = random.randint(1, 30)  # choose a random number of key presses (between 1 and 7)

    for _ in range(num_key_presses):
        key_to_press = random.choice(keys)  # select random key from list
        keyboard.press(key_to_press)
        keyboard.release(key_to_press)
        time.sleep(0.2)  # sleep for a while between key presses

    # For changing Tab
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.page_down)
    keyboard.release(Key.page_down)
    keyboard.release(Key.ctrl_l)

    num_clicks = random.randint(1, 30)  # choose a random number of mouse clicks (between 1 and 3)

    for _ in range(num_clicks):
        # pressing left-click at random position
        x_rand = random.randint(0, pyautogui.size().width)
        y_rand = random.randint(0, pyautogui.size().height)
        pyautogui.leftClick(x_rand, y_rand)
        time.sleep(0.2)  # sleep for a while between clicks

    print(get_now_timestamp(), 'Mouse clicked, keys added')

def get_now_timestamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def execute_keep_awake_action():
    print(get_now_timestamp(), 'Idle detection')
    press_keys()
    move_mouse()

def move_mouse():
    current_pos = mouse.position
    mouse.move(1, 0)
    mouse.position = current_pos

def define_custom_seconds():
    global  MOVE_MOUSE, RANDOM_MODE, RAND_INTERVAL_START, RAND_INTERVAL_STOP

    RAND_INTERVAL_START = 10
    RAND_INTERVAL_STOP = 20

    MOVE_MOUSE = True
    RANDOM_MODE = True
    print(get_now_timestamp(), "This Script uses random time interval between 10-20 seconds for pressing keys. \nKeys pressed will be (Move mouse position, Shift, Ctrl+Down, left-click) after random intervals.")
    print ("--- Started ---")

try:
    define_custom_seconds()

    while True:
        last_position = mouse.position
        time.sleep(1)
        current_position = mouse.position

        if current_position == last_position:
            execute_keep_awake_action()
            current_position = mouse.position
        else:
            print(get_now_timestamp(), 'User activity detected')

        last_position = current_position

        rand_delay = random.randint(RAND_INTERVAL_START, RAND_INTERVAL_STOP)
        print(get_now_timestamp(), f"Delay: {str(rand_delay)}")
        time.sleep(rand_delay)

except KeyboardInterrupt:
    print("\nCredits: Deepak, buy me a coffee: dgandhi570@oksbi")
    exit()
