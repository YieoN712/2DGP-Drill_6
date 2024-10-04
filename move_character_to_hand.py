from pico2d import *
import random

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

charSpeed = 5
charX, charY = WIDTH // 2, HEIGHT // 2
char_direction = True
handX, handY = 0, 0

def rand_hand():
    handX, handY = random.randint(50 // 2, (WIDTH - 50) // 2), random.randint(52 // 2, (HEIGHT - 52) // 2)
    pass

def move_character(charX, charY):
    if charX < handX:
        charX += charSpeed
        char_direction=True
    elif charX > handX:
        charX -= charSpeed
        char_direction = False

    if charY < handY:
        charY += charSpeed
    elif charY > handY:
        charY -= charSpeed
    pass

running = True
x, y = WIDTH // 2, HEIGHT // 2
frame = 0
hide_cursor()
rand_hand()

while running:
    clear_canvas()
    TUK_ground.draw(WIDTH // 2, HEIGHT // 2)
    hand.draw(handX, handY)

    move_character(x,y)

    if char_direction:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
       character.clip_composite_draw(frame * 100, 0, 100, 100, 0,'h', x, y)

    frame = (frame + 1) % 8
    update_canvas()

    events = get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            running = False

close_canvas()