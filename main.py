from pygame import *
from settings import *
from keys import *
from sounds import *

init()

screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Fortepiano")

keys_rects = create_keys(len(KEYS))
pressed_keys = set()
sounds = Load_sounds(KEYS)
keys_list = list(KEYS.keys())

while 1:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == MOUSEBUTTONDOWN:
            pos = e.pos
            for i, rect in enumerate(keys_rects):
                if rect.collidepoint(pos):
                    sounds[keys_list[i]].play()
                    pressed_keys.add(i)
            if e.type == MOUSEBUTTONUP:
                pos = e.pos
                for i, rect in enumerate(keys_rects):
                    if i in pressed_keys and rect.collidepoint(pos):
                        pressed_keys.remove(i)
            if e.type == KEYDOWN:
                k = key.name(e.key)
                if k in sounds:
                    sounds[k].play()
                    idx = keys_list.index(k)
                    if idx in pressed_keys:
                        pressed_keys.remove(idx)
            if e.type == KEYUP:
                k = key.name(e.kay)
                if k in sounds:
                    idx = keys_list.index(k)
                    if idx in pressed_keys:
                        pressed_keys.remove(idx)
                    
    screen.fill(WHITE)
    draw_keys(screen, keys_rects, pressed_keys,)
    display.update()