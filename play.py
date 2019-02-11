## algos to try

#1 find best merge
#2 find most merges
#3 #1 + #2
#4 


import time
import random

from pyautogui import press as keyboard_press

from capture import capture, cnvt2grid
from game_rules import print_grid, generate_rand_grid, generate_zero_grid, determine_best_move



def random_keypress():
    print('playing random......')
    keyboard_press(['up', 'down', 'left', 'right'][random.randint(0,3)])

    
state = []
prev_state = []


if __name__ == '__main__':
    while 1:
        prev_state = state
        state = cnvt2grid(capture())
        if prev_state == state:
            random_keypress()

        print('\n')
        print_grid(state)

        keyboard_press(determine_best_move(state))
        time.sleep(0.5)

        
        
    
