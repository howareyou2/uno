import pygame
import colorblind

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Set up the window
WIN_WIDTH = 800
WIN_HEIGHT = 600
'''
# Define setting menu items
settingmenu_items = [
    {"text": "Single Player", "pos": (WIN_WIDTH//2, 200)},
    {"text": "Settings", "pos": (WIN_WIDTH//2, 320)},
    {"text": "Exit", "pos": (WIN_WIDTH//2, 440)}
]
'''

# 버튼 액션 함수
def change_screen_size():
    # 화면 크기 변경 코드 작성
    pass


def change_key_setting():
    # 키설정 변경 코드 작성
    pass


def toggle_color_blind_mode():
    # 색약모드 전환 코드 작성
    if colorblind.color_mode != colorblind.protanopia:
        color_mode = colorblind.protanopia
    elif colorblind.color_mode == colorblind.protanopia:
        color_mode = colorblind.RED, colorblind.GREEN, colorblind.BLUE


def reset_settings():
    # 모든설정 기본설정으로 되돌리기 코드 작성
    pass


def settings_screen():
    # 게임화면의 크기 설정
    WIDTH = 800
    HEIGHT = 600

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)

    # 게임화면 생성
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    pygame.display.set_caption("settings")

    title_font = pygame.font.SysFont('comicsansms', 80)
    menu_font = pygame.font.SysFont('comicsansms', 50)



    # Create text surfaces
    title_text = title_font.render('settings', True, BLACK)

    # Set up menu buttons
    button_width = 200
    button_height = 100
    button_padding = 20


    # Define menu items
    menu_items = [
        {"text": "Screen Size", "pos": (WIN_WIDTH // 2, 200)},
        {"text": "Key Setting", "pos": (WIN_WIDTH // 2, 260)},
        {"text": "Color Blind Mode", "pos": (WIN_WIDTH // 2,320)},
        {"text": "Reset Settings", "pos": (WIN_WIDTH // 2, 380)},
        {"text": "return", "pos": (WIN_WIDTH // 2, 440)}
    ]


    # Set up the cursor
    cursor_img = pygame.Surface((20, 20))
    cursor_img.fill(WHITE)
    cursor_rect = cursor_img.get_rect()


    # Set up the menu
    selected_item = 0

    running = True
    # 게임 루프
    while running:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    if selected_item == 0:
                        change_screen_size()

                    elif selected_item == 1:
                        change_key_setting()

                    elif selected_item == 2:
                        toggle_color_blind_mode()

                    elif selected_item == 3:
                        reset_settings()

                    elif selected_item == 4:
                        running = False

            elif event.type == pygame.MOUSEMOTION:
                cursor_rect.center = event.pos

            # 마우스 이벤트 처리
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("click!")
                # 마우스 왼쪽 버튼을 누르면 버튼 클릭 처리
                if event.button == 1:
                    for i, item in enumerate(menu_items):
                        if cursor_rect.collidepoint(item["pos"]):
                            # 세팅 버튼 클릭 시 처리
                            selected_item = i
                            if selected_item == 0:
                                change_screen_size()
                            elif selected_item == 1:
                                change_key_setting()
                            elif selected_item == 2:
                                toggle_color_blind_mode()
                            elif selected_item == 3:
                                reset_settings()
                            elif selected_item == 4:
                                running = False
        # Draw the menu
        win.fill(WHITE)

        win.blit(title_text, ((WIN_WIDTH - title_text.get_width()) / 2, 50))
        for i, item in enumerate(menu_items):
            text = menu_font.render(item["text"], True, BLACK if i == selected_item else GRAY)
            rect = text.get_rect(center=item["pos"])
            if rect.collidepoint(cursor_rect.center):
                # text=GRAY
                text = menu_font.render(item["text"], True, BLACK if i == selected_item else GRAY)
            win.blit(text, rect)

        # 게임화면 업데이트

        pygame.display.update()
