import curses
import time
from functions import move

player = [0, 0]

def main(stdscr):
    curses.curs_set(0)
    while True:
        move(stdscr.getch(), player, stdscr)
        stdscr.refresh()

curses.wrapper(main)