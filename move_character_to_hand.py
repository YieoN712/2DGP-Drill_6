from pico2d import *
import random
import math

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

charSpeed = 2
x, y = WIDTH // 2, HEIGHT // 2
char_direction = True

def rand_hand():
    global handX, handY
    handX, handY = random.randint(50 // 2, WIDTH - 50 // 2), random.randint(52 // 2, HEIGHT - 52 // 2)

def move_character():
    global x, y, char_direction
    dx = handX - x
    dy = handY - y
    distance = math.sqrt(dx**2 + dy**2)

    if distance > 0:
        move_x = (dx / distance) * charSpeed
        move_y = (dy / distance) * charSpeed
        x += move_x
        y += move_y

        char_direction = move_x > 0

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
        character.clip_draw(frame * 100, 0, 100, 100, x, y, 150, 150)

    frame = (frame + 1) % 8

    if math.sqrt((x - handX)**2 + (y - handY)**2) < 50:
        rand_hand()

    update_canvas()

    events = get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            running = False

close_canvas()