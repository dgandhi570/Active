# #!/usr/bin/env python

# import argparse
# import time
# from datetime import datetime
# from pynput.mouse import Controller as MouseController
# from pynput.keyboard import Key, Controller as KeyboardController
# import random
# import pyautogui

# mouse = MouseController()
# keyboard = KeyboardController()

# MOVE_MOUSE = False
# PRESS_SHIFT_KEY = False
# RANDOM_MODE = False
# PIXELS_TO_MOVE = 1
# MOUSE_DIRECTION_DELTA = 0
# RAND_INTERVAL_START = 0
# RAND_INTERVAL_STOP = 0

# move_mouse_every_seconds = 300
# mouse_direction = 0


# def define_custom_seconds():
#     global move_mouse_every_seconds, PIXELS_TO_MOVE, PRESS_SHIFT_KEY, MOVE_MOUSE, \
#         MOUSE_DIRECTION_DELTA, RANDOM_MODE, RAND_INTERVAL_START, RAND_INTERVAL_STOP

#     parser = argparse.ArgumentParser(
#         description="This program moves the mouse or press a key when it detects that you are away. "
#                     "It won't do anything if you are using your computer. "
#                     "Useful to trick your machine to think you are still working with it.")


#     parser.add_argument(
#         "-m", "--mode",
#         help="Available options: keyboard, mouse, both; default is mouse. "
#              "This is the action that will be executed when the user is idle: "
#              "If keyboard is selected, the program will press the shift key. "
#              "If mouse is selected, the program will move the mouse. "
#              "If both is selected, the program will do both actions. ")

#     parser.add_argument(
#         "-r", "--random", type=int, nargs=2,
#         help="Usage: two numbers (ex. -r 3 10). "
#              "Execute actions based on a random interval between start and stop seconds. "
#              "Note: Overwrites the seconds argument.")

#     args = parser.parse_args()
#     mode = args.mode
#     random_seconds_interval = args.random

#     if random_seconds_interval:
#         RAND_INTERVAL_START = int(random_seconds_interval[0])
#         RAND_INTERVAL_STOP = int(random_seconds_interval[1])

#         # prevents initialize random.randint() with invalid numbers:
#         if RAND_INTERVAL_START > RAND_INTERVAL_STOP:
#             print("Error: Random initial number needs to be lower than random limit number.")
#             exit()

#     is_both_enabled = 'both' == mode
#     is_keyboard_enabled = 'keyboard' == mode or is_both_enabled
#     is_mouse_enabled = 'mouse' == mode or is_both_enabled or mode is None

#     print('--------')
#     if is_keyboard_enabled:
#         PRESS_SHIFT_KEY = True
#         print(get_now_timestamp(), "Keyboard is enabled")

#     if random_seconds_interval:
#         RANDOM_MODE = True
#         print(get_now_timestamp(), "Random timing is enabled.")
#     else:
#         print(get_now_timestamp(), 'Running every', str(move_mouse_every_seconds), 'seconds')

#     print('--------')



# def press_shift_key():

#     # pressing shift key
#     keyboard.press(Key.shift)
#     keyboard.release(Key.shift)

#     # For changing Tab
#     keyboard.press(Key.ctrl_l)
#     keyboard.press(Key.page_down)
#     keyboard.release(Key.page_down)
#     keyboard.release(Key.ctrl_l)

#     # Adding ctr+P
#     # keyboard.press(Key.ctrl_l)
#     # keyboard.press(Key.p)
#     # keyboard.release(Key.p)
#     # keyboard.release(Key.ctrl_l)

#     # pressing left-click
#     pyautogui.leftClick()
    
#     print(get_now_timestamp(), 'Mouse clicked, keys added')


# def get_now_timestamp():
#     now = datetime.now()
#     return now.strftime("%H:%M:%S")


# def execute_keep_awake_action():
#     print(get_now_timestamp(), 'Idle detection')

#     press_shift_key()


# define_custom_seconds()
# lastSavePosition = (0, 0)

# try:
#     while 1:
#         currentPosition = mouse.position
#         is_user_away = currentPosition == lastSavePosition

#         if is_user_away:
#             execute_keep_awake_action()
#             currentPosition = mouse.position

#         if not is_user_away:
#             print(get_now_timestamp(), 'User activity detected')

#         lastSavePosition = currentPosition

#         if RANDOM_MODE:
#             rand_delay = random.randint(RAND_INTERVAL_START, RAND_INTERVAL_STOP)
#             print(get_now_timestamp(), f"Delay: {str(rand_delay)}")
#             time.sleep(rand_delay)
#         else:
#             time.sleep(move_mouse_every_seconds)

#         print('--------')

# except KeyboardInterrupt:
#     print("\nBye bye ;-)")
#     exit()
