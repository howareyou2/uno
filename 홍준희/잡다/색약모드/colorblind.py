# colorblind.py

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

# 색상 모드 함수
def color_mode(color, mode):
    if mode:
        return protanopia(color)
    else:
        return color
