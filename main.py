from pygame import *
from settings import *
from keys import *

init()

screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Fortepiano")

keys_rects = create_keys(len(KEYS))
pressed_keys = set()
while 1:
    for e in event.get():
        if e.type == QUIT:
            quit()

    screen.fill(WHITE)
    draw_keys(screen, keys_rects, pressed_keys,)
    display.update()