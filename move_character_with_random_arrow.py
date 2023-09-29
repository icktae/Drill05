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

    # ESC 탈출
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# 캐릭터 형상 변환 함수
def character_image(z) :
    character.clip_draw(frame * 100, z, 100, 100, x, y)

#거리 계산 함수
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)



running = True
x = 1280 // 2
y = 1024 // 2
frame = 0

# hand_arrow 랜덤 설정 (0 ~ 크기)
hand_x = random.randint(0, TUK_WIDTH)
hand_y = random.randint(0, TUK_HEIGHT)

while running :
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    # 화살표 그리기
    hand_arrow.draw(hand_x, hand_y)

    speed = 10
    dx = hand_x - x
    dy = hand_y - y

    move_arrow = distance(x, y, hand_x, hand_y)

    if move_arrow > 0:
        x += (dx / move_arrow) * speed
        y += (dy / move_arrow) * speed

    # hand_arrow 업데이트
    if distance(x, y, hand_x, hand_y) < 10:
        hand_x = random.randint(0, TUK_WIDTH)
        hand_y =  random.randint(0, TUK_HEIGHT)

    if hand_x > x :
            character_image(100)
    elif hand_x < x :
            character_image(0)


    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()