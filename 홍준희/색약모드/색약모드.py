import pygame
import sys

WHITE = (255, 255, 255)


# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
LIGHT_GREEN = (144, 238, 144)
LIGHT_RED = (255, 182, 193)
LIGHT_BLUE = (173, 216, 230)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)


# 색약 모드용 색 정의
NEW_GREEN = (170, 255, 170)
NEW_RED = (190, 75, 75)
NEW_BLUE = (75, 75, 190)
NEW_YELLOW = (255, 255, 128)
NEW_ORANGE = (255, 200, 128)
NEW_PINK = (255, 175, 175)


# 색약 모드 함수
def protanopia(color):
    r, g, b = color
    new_r = (0.56667 * g) + (0.43333 * b)
    new_g = (0.55833 * r) + (0.44167 * b)
    new_b = (0.0 * r) + (1.0 * g)
    return (int(new_r), int(new_g), int(new_b))

# 초기화
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Color Blindness Simulator")

# 루프
done = False
clock = pygame.time.Clock()

while not done:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 배경 설정
    screen.fill(WHITE)

    # 모드 설정
    mode = pygame.key.get_pressed()
    if mode[pygame.K_SPACE]:
        color_mode = protanopia
    else:
        color_mode = lambda x: x

        # 사각형 그리기
    pygame.draw.rect(screen, color_mode(RED), [50, 50, 50, 50])
    pygame.draw.rect(screen, color_mode(GREEN), [110, 50, 50, 50])
    pygame.draw.rect(screen, color_mode(BLUE), [170, 50, 50, 50])
    pygame.draw.rect(screen, color_mode(GRAY), [230, 50, 50, 50])
    pygame.draw.rect(screen, color_mode(LIGHT_GREEN), [290, 50, 50, 50])
    pygame.draw.rect(screen, color_mode(LIGHT_RED), [350, 50, 50, 50])
    pygame.draw.rect(screen, color_mode(LIGHT_BLUE), [410, 50, 50, 50])
    pygame.draw.rect(screen, color_mode(YELLOW), [470, 50, 50, 50])
    pygame.draw.rect(screen, color_mode(ORANGE), [530, 50, 50, 50])
    pygame.draw.rect(screen, color_mode(PINK), [590, 50, 50, 50])

    # 그리기 업데이트
    pygame.display.flip()
    clock.tick(60)

# 파이게임 종료
pygame.quit()
sys.exit()
