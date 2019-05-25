#!/usr/bin/env python3

# Add . to pythonpath
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

# spiral class
from spiral import Spiral

# curses stuff
from mycurse import Curse

# Use is_prime from gmpy2 (alternatively write your own)
from gmpy2 import is_prime

# Catch Ctrl-c
import signal
cc_pressed = False
def cc_handler(sig, frame):
    global cc_pressed
    cc_pressed = True
signal.signal(signal.SIGINT, cc_handler)

# --- main ---

c = Curse()
heigth, width = c.get_yx()
s = Spiral(width // 2, heigth // 2)

i = 2
while True:
    x, y = s.coords()
    # Exit if outside screen boundaries
    if x >= width or x < 0 or y >= heigth or y < 0:
        break
    # Output X or .
    if is_prime(i):
        c.str_at('X', x, y)
    else:
        c.str_at('.', x, y)
    # Next spiral coordinate
    s.next_step()
    i += 1

    if not cc_pressed:
        c.waitkey()

# Wait for another keypress to see the full spiral before exit
c.waitkey()
c.waitkey()
c.cleanup()
