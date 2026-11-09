from pygame import *
from settings import *

init()

screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Fortepiano")

while 1:
    for e in event.get():
        if e.type == QUIT:
            quit()

    screen.fill(WHITE)
    display.update()