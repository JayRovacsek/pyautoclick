#!/usr/bin/env python3.7
import pyautogui
import random
import time
import argparse

parser = argparse.ArgumentParser(description='Autoclicker with semi-rand interval.')
parser.add_argument('lower', type=int, help='Lower bound for random time')
parser.add_argument('upper', type=int, help='Upper bound for random time')

args = parser.parse_args()

# Main hook
if __name__ == '__main__':
    print("Starting clicking in {} seconds.".format(args.lower * 3))
    time.sleep(args.upper * 3)
    while True:
        try:
            mouse_x, mouse_y = pyautogui.position()
            print("Clicking at: {}, {}".format(mouse_x,mouse_y))
            pyautogui.click()
            alch_click_timer = random.randint(200,400)
            print("Sleeping: {}ms".format(alch_click_timer))
            time.sleep(alch_click_timer/1000)
            mouse_x, mouse_y = pyautogui.position()
            print("Clicking at: {}, {}".format(mouse_x,mouse_y))
            click_timer = random.randint(args.lower*100,args.upper*100)
            print("Sleeping: {}s".format(click_timer/100))
            time.sleep(click_timer/100)
        except KeyboardInterrupt:
            break