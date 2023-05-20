import pygame
import json

# 전역 변수로 선언
custom_keys = {
    'return': pygame.K_RETURN,
    'up': pygame.K_UP,
    'down': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT
}

class Button:
    def __init__(self, text, font, color, hover_color, x, y, width, height, action=None):
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)

        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def click(self):
        if self.action:
            self.action()


def draw_text(text, font, color, surface, x, y, align="center"):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()

    if align == "center":
        text_rect.center = (x, y)
    elif align == "top":
        text_rect.topleft = (x, y)
    elif align == "bottom":
        text_rect.bottomleft = (x, y)

    surface.blit(text_obj, text_rect)

def get_user_input():
    waiting = True
    key_labels = list(custom_keys.keys())
    selected_key = None

    clock = pygame.time.Clock()
    font = pygame.font.SysFont('comicsansms', 24) 
    screen = pygame.display.set_mode((800, 600))
    screen_center = screen.get_rect().center

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #running = False
                return
            elif event.type == pygame.KEYDOWN:
                if selected_key:
                    custom_keys[selected_key] = event.key
                    selected_key = None  # 선택된 키 초기화

                else:
                    if event.key == pygame.K_ESCAPE:
                        waiting = False
                    elif event.key == pygame.K_BACKSPACE:
                        selected_key = None
                    elif pygame.key.name(event.key) in key_labels:
                        selected_key = pygame.key.name(event.key)

            # 클릭 이벤트 처리
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 마우스 왼쪽 버튼 클릭
                    if back_button2.rect.collidepoint(event.pos):
                        return

        screen.fill((255, 255, 255))  # 흰색 창

        draw_text('Press the arrow keys and enter keys ', font, (0, 0, 0), screen, screen_center[0], screen_center[1] - 250)
        draw_text('to change them to the desired key', font, (0, 0, 0), screen, screen_center[0], screen_center[1] - 220)

        draw_text('Key Settings', font, (0, 0, 0), screen, screen_center[0], screen_center[1] - 80)

        draw_text('Enter Key:', font, (0, 0, 0), screen, screen_center[0] - 120, screen_center[1] - 50, align="top")
        draw_text(pygame.key.name(custom_keys['return']), font, (0, 0, 0), screen, screen_center[0] + 70, screen_center[1] - 50, align="top")
        draw_text('Up Key:', font, (0, 0, 0), screen, screen_center[0] - 120, screen_center[1] - 10, align="top")
        draw_text(pygame.key.name(custom_keys['up']), font, (0, 0, 0), screen, screen_center[0] + 70, screen_center[1] - 10, align="top")
        draw_text('Down Key:', font, (0, 0, 0), screen, screen_center[0] - 120, screen_center[1] + 30, align="top")
        draw_text(pygame.key.name(custom_keys['down']), font, (0, 0, 0), screen, screen_center[0] + 70, screen_center[1] + 30, align="top")
        draw_text('Left Key:', font, (0, 0, 0), screen, screen_center[0] - 120, screen_center[1] + 70, align="top")
        draw_text(pygame.key.name(custom_keys['left']), font, (0, 0, 0), screen, screen_center[0] + 70, screen_center[1] + 70, align="top")
        draw_text('Right Key:', font, (0, 0, 0), screen, screen_center[0] - 120, screen_center[1] + 110, align="top")
        draw_text(pygame.key.name(custom_keys['right']), font, (0, 0, 0), screen, screen_center[0] + 70, screen_center[1] + 110, align="top")

        back_button2 = Button("Back", font, (200, 200, 200), (150, 150, 150),0,0,80,40)

        if selected_key:
            if selected_key != 'return':
                draw_text('Press a new key for ' + selected_key + '...', font, (255, 0, 0), screen, screen_center[0], screen_center[1] - 170)
            else:
                draw_text('Press a new key for 엔터...', font, (255, 0, 0), screen, screen_center[0], screen_center[1] - 170)
        else:
            draw_text('Press ESC or Click Back to exit.', font, (0, 0, 0), screen, screen_center[0], screen_center[1] - 170)

        back_button2.draw(screen)
        pygame.display.update()
        clock.tick(60)


def save_settings():
    # 설정 정보를 JSON 파일로 저장
    with open('keySetting.json', 'w') as file:
        json.dump(custom_keys, file)
    
    print("Settings saved successfully.")


def load_settings():
    global custom_keys
    # 설정 정보를 JSON 파일에서 로드
    try:
        with open('keySetting.json', 'r') as file:
            loaded_settings = json.load(file)
            custom_keys.update(loaded_settings)
    except FileNotFoundError:
        # 파일이 존재하지 않을 경우 기본 설정 사용
        custom_keys = {
            'return': pygame.K_RETURN,
            'up': pygame.K_UP,
            'down': pygame.K_DOWN,
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT
        }

def reset_settings():
    global custom_keys
    custom_keys = {
        'return': pygame.K_RETURN,
        'up': pygame.K_UP,
        'down': pygame.K_DOWN,
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT
    }

def back():
    return


def run():
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('comicsansms', 24)
    screen = pygame.display.set_mode((800, 600))
    screen_center = screen.get_rect().center

    load_settings()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #running = False
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    get_user_input()
                elif event.key == pygame.K_r:
                    reset_settings()
                elif event.key == pygame.K_ESCAPE:
                    return

            # 클릭 이벤트 처리
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 마우스 왼쪽 버튼 클릭
                    if save_button.rect.collidepoint(event.pos):
                        save_button.click()
                    elif reset_button.rect.collidepoint(event.pos):
                        reset_button.click()
                    elif back_button.rect.collidepoint(event.pos):
                        return

        screen.fill((255, 255, 255))  # 흰색 창

        draw_text('Press SPACE to change key settings', font, (0, 0, 0), screen, screen_center[0], screen_center[1] - 250)
        draw_text('Click Save to save key settings', font, (0, 0, 0), screen, screen_center[0], screen_center[1] - 200)
        draw_text('Press R or Click Reset to reset key settings', font, (0, 0, 0), screen, screen_center[0], screen_center[1] - 150)

        draw_text('<Key Settings>', font, (0, 0, 0), screen, screen_center[0], screen_center[1] - 80)

        draw_text('Enter Key:', font, (0, 0, 0), screen, screen_center[0] - 120, screen_center[1] - 50, align="top")
        draw_text(pygame.key.name(custom_keys['return']), font, (0, 0, 0), screen, screen_center[0] + 70, screen_center[1] - 50, align="top")
        draw_text('Up Key:', font, (0, 0, 0), screen, screen_center[0] - 120, screen_center[1] - 10, align="top")
        draw_text(pygame.key.name(custom_keys['up']), font, (0, 0, 0), screen, screen_center[0] + 70, screen_center[1] - 10, align="top")
        draw_text('Down Key:', font, (0, 0, 0), screen, screen_center[0] - 120, screen_center[1] + 30, align="top")
        draw_text(pygame.key.name(custom_keys['down']), font, (0, 0, 0), screen, screen_center[0] + 70, screen_center[1] + 30, align="top")
        draw_text('Left Key:', font, (0, 0, 0), screen, screen_center[0] - 120, screen_center[1] + 70, align="top")
        draw_text(pygame.key.name(custom_keys['left']), font, (0, 0, 0), screen, screen_center[0] + 70, screen_center[1] + 70, align="top")
        draw_text('Right Key:', font, (0, 0, 0), screen, screen_center[0] - 120, screen_center[1] + 110, align="top")
        draw_text(pygame.key.name(custom_keys['right']), font, (0, 0, 0), screen, screen_center[0] + 70, screen_center[1] + 110, align="top")

        # 버튼 생성
        save_button = Button("Save", font, (200, 200, 200), (150, 150, 150), screen_center[0] - 120, screen_center[1] + 180, 80, 40, action=save_settings)
        reset_button = Button("Reset", font, (200, 200, 200), (150, 150, 150), screen_center[0] + 40, screen_center[1] + 180, 80, 40, action=reset_settings)
        back_button = Button("Back", font, (200, 200, 200), (150, 150, 150),0,0,80,40)

        save_button.draw(screen)
        reset_button.draw(screen)
        back_button.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 600))
    run()