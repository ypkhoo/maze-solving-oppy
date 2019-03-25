from movement import *

try: 
    import Tkinter as tk
except ImportError: 
    import tkinter as tk

def key_input(event): 
    init() 
    print("Key: ", event.char)
    key_press = event.char 
    sleep_time = 0.030 

    if key_press.lower() == 'w': 
        forward(sleep_time)
    elif key_press.lower() == 's': 
        reverse(sleep_time)
    elif key_press.lower() == 'a': 
        turn_left(sleep_time)
    elif key_press.lower() == 'd': 
        turn_right(sleep_time)
    elif key_press.lower() == 'q': 
        pivot_left(sleep_time)
    elif key_press.lower() == 'e': 
        pivot_right(sleep_time)
    else: 
        GPIO.cleanup()

command = tk.Tk() 
command.bind('<KeyPress>', key_input)
command.mainloop() 
