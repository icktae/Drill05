from pico2d import *
import math
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('sonic_animation.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    global x
    global y
    global dir_lr
    global dir_ud

    # ESC 탈출
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False