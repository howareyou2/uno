import pygame
import colorblind
import keySetting
import json
from soundsetting import SoundSettingsWindow

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Set up the window
WIN_WIDTH = 800
WIN_HEIGHT = 600

def load_custom_keys():
    global custom_keys
    with open('keySetting.json', 'r') as f:
        custom_keys = json.load(f)

# 버튼 액션 함수
def change_screen_size(c):
    # 화면 크기와 배경색 설정
    screen_size1 = (800, 600)
    screen_size2 = (1600, 800)

    background_color = (255, 255, 255)  # 흰색

    # 화면 크기 변경 코드 작성
    # 0작은창 1중간창 2풀화면
    if cnt == 0:
        screen = pygame.display.set_mode(screen_size2)
    elif cnt==1:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(screen_size1)




def change_key_setting():
    # 키설정 변경 코드 작성
    keySetting.run()


def toggle_color_blind_mode(t):
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

    # Define menu items
    menu_items = [
        {"text": "Screen Size", "pos": (WIN_WIDTH // 2, 200)},
        {"text": "Key Setting", "pos": (WIN_WIDTH // 2, 260)},
        {"text": "Color Blind Mode", "pos": (WIN_WIDTH // 2,320)},
        {"text": "Reset Settings", "pos": (WIN_WIDTH // 2, 380)},
        {"text": "Sound Settings", "pos": (WIN_WIDTH // 2, 440)},
        {"text": "return", "pos": (WIN_WIDTH // 2, 500)}
    ]


    # Set up the cursor
    cursor_img = pygame.Surface((20, 20))
    cursor_img.fill(WHITE)
    cursor_rect = cursor_img.get_rect()


    # Set up the menu
    selected_item = 0

    #화면 크기 위한 변수
    cnt = 0

    #색약모드 토글 변수
    toggle = 1

    running = True
    # 게임 루프
    while running:
        # 이벤트 처리
        load_custom_keys()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # 키보드 키 입력받는 부분
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == custom_keys['up']:
                    selected_item = (selected_item - 1) % len(menu_items)
                elif event.key == custom_keys['down']:
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.key == custom_keys['return']:
                    # 키보드로 박스 선택 , 위치순서대로
                    if selected_item == 0:
                        change_screen_size(cnt)
                        cnt = (cnt + 1) % 3

                    elif selected_item == 1:
                        change_key_setting()

                    elif selected_item == 2:
                        if toggle == 0:
                            toggle_color_blind_mode(toggle)
                            toggle = 1
                        else:
                            toggle_color_blind_mode(toggle)
                            toggle = 0

                    elif selected_item == 3:
                        reset_settings()

                    elif selected_item == 4:
                        sound_window = SoundSettingsWindow()
                        # 사운드 설정 창 실행
                        sound_window.run()
                        
                    elif selected_item == 5:
                        running = False
            #마우스 커서이동
            elif event.type == pygame.MOUSEMOTION:
                cursor_rect.center = event.pos

            # 마우스 이벤트 처리
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("click!")
                # 마우스 왼쪽 버튼을 누르면 버튼 클릭 처리
                if event.button == 1:
                    for i, item in enumerate(menu_items):
                        if cursor_rect.collidepoint(item["pos"]):
                            # 세팅 버튼 클릭 시 처리, 위치 순서대로
                            selected_item = i
                            if selected_item == 0:
                                change_screen_size(cnt)
                                cnt = (cnt+1)%3
                            elif selected_item == 1:
                                change_key_setting()
                            elif selected_item == 2:
                                toggle_color_blind_mode()
                            elif selected_item == 3:
                                reset_settings()
                            elif selected_item == 4:
                                sound_window = SoundSettingsWindow()
                                # 사운드 설정 창 실행
                                sound_window.run()
                            elif selected_item == 5:
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
