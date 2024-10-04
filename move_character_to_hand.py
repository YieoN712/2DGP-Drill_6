from pico2d import *

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def rand_hand():
    pass

def move_character():
    pass

running = True
x, y = WIDTH // 2, HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(WIDTH // 2, HEIGHT // 2)
    update_canvas()