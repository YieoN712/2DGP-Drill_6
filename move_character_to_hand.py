from pico2d import *
import random

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

charSpeed = 3
x, y = WIDTH // 2, HEIGHT // 2
char_direction = True

def rand_hand():
    global handX, handY
    handX, handY = random.randint(50 // 2, (WIDTH - 50) // 2), random.randint(52 // 2, (HEIGHT - 52) // 2)
    pass

def move_character():
    global x, y, char_direction
    if x < handX:
        x += charSpeed
        char_direction=True
    elif x > handX:
        x -= charSpeed
        char_direction = False

    if y < handY:
        y += charSpeed
    elif y > handY:
        y -= charSpeed
    pass

running = True
frame = 0
hide_cursor()
rand_hand()

while running:
    clear_canvas()
    TUK_ground.draw(WIDTH // 2, HEIGHT // 2)
    hand.draw(handX, handY)

    move_character()

    if char_direction:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y, 150, 150)
    else:
       character.clip_composite_draw(frame * 100, 0, 100, 100, 0,'h', x, y, 150, 150)

    frame = (frame + 1) % 8

    if abs(x - handX) < 100 // 2 and abs(y - handY) < 100 // 2:
        rand_hand()

    update_canvas()

    events = get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            running = False

close_canvas()