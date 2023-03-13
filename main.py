from curses import *
from datetime import datetime
import time
from pyfiglet import figlet_format

def main(stdscr):

    stdscr.clear()
    init_pair(1,COLOR_CYAN,0) # Initialize color pair
    curs_set(False) # Removes blinking curser

    def tick(): # Recursively draws clock every second
        stdscr.clear()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        stdscr.addstr(f'{figlet_format(current_time)}  \n', color_pair(1))
        stdscr.addstr('Ctrl + C to exit')
        time.sleep(1)
        stdscr.refresh()
        tick()
    
    tick()

if __name__=='__main__':
    wrapper(main) 
    print("Exited")