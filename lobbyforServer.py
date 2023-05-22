import pygame
import json

# Set up the window
WIN_WIDTH = 800
WIN_HEIGHT = 600

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

def load_custom_keys():
    global custom_keys
    with open('keySetting.json', 'r') as f:
        custom_keys = json.load(f)

def lobby():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    win.fill(WHITE)

    pygame.display.set_caption("lobby")

    title_font = pygame.font.SysFont('comicsansms', 80)
    mode_menu_font = pygame.font.SysFont('comicsansms', 50)

    button_width = 200
    button_height = 100

    title_text = title_font.render('UNO Multi Host', True, BLACK)

    mode_items = [
        {"text": "Start", "pos": (WIN_WIDTH // 2, 350)},
        {"text": "Back", "pos": (WIN_WIDTH // 2, 440)}
    ]

    cursor_img = pygame.Surface((20, 20))
    cursor_img.set_colorkey((0, 0, 0))
    cursor_rect = cursor_img.get_rect()

    selected_item = 0

    running = True
    while running:
        load_custom_keys()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == custom_keys['up']:
                    selected_item = (selected_item - 1) % len(mode_items)
                elif event.key == custom_keys['down']:
                    selected_item = (selected_item + 1) % len(mode_items)
                elif event.key == custom_keys['return']:
                    if selected_item == 0:
                        players = 2

                        button_width = 40
                        button_height = 40
                        button_x = 450
                        button_y = 200

                        def save_players(num_players):
                            players_dict = {
                                'players': num_players
                            }

                            with open('players.json', 'w') as file:
                                json.dump(players_dict, file)

                        def draw_window(num_players):
                            win.fill(WHITE)

                            pygame.draw.rect(win, pygame.Color('red'), pygame.Rect(button_x - button_width, button_y, button_width, button_height))
                            pygame.draw.rect(win, pygame.Color('red'), pygame.Rect(button_x + button_width, button_y, button_width, button_height))
                            font = pygame.font.Font(None, 30)
                            text_minus = font.render("-", True, pygame.Color('white'))
                            text_plus = font.render("+", True, pygame.Color('white'))
                            win.blit(text_minus, (button_x - button_width + 16, button_y + 8))
                            win.blit(text_plus, (button_x + button_width + 17, button_y + 8))

                            pygame.draw.rect(win, pygame.Color('gray'), pygame.Rect(250, 200, 100, 50))
                            font = pygame.font.Font(None, 30)
                            text = font.render("Save", True, pygame.Color('black'))
                            win.blit(text, (275, 215))

                            text_players = font.render(str(num_players), True, pygame.Color('black'))
                            win.blit(text_players, (button_x - button_width + 52, button_y + 10))

                            win.blit(title_text, ((WIN_WIDTH - title_text.get_width()) / 2, 50))
                            for i, item in enumerate(mode_items):
                                menu_text = mode_menu_font.render(item["text"], True, BLACK if i == selected_item else GRAY)
                                rect = menu_text.get_rect(center=item["pos"])
                                win.blit(menu_text, rect)
                            

                        running_players = True
                        while running_players:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running_players = False
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    if pygame.Rect(250, 200, 100, 50).collidepoint(event.pos):
                                        save_players(players)
                                        running_players = False
                                        pass
                                    elif pygame.Rect(button_x - button_width, button_y, button_width, button_height).collidepoint(event.pos):
                                        players -= 1
                                        players = max(2, players)
                                    elif pygame.Rect(button_x + button_width, button_y, button_width, button_height).collidepoint(event.pos):
                                        players += 1
                                        players = min(5, players)

                            draw_window(players)
                            pygame.display.update()
                        
                    elif selected_item == 1:
                        running = False
            elif event.type == pygame.MOUSEMOTION:
                cursor_rect.center = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i, item in enumerate(mode_items):
                        button_rect = pygame.Rect(item["pos"][0] - button_width / 2, item["pos"][1] - button_height / 2, button_width, button_height)
                        if button_rect.collidepoint(event.pos):
                            selected_item = i
                            if selected_item == 0:
                                print("방생성")
                            elif selected_item == 1:
                                return

        win.fill(WHITE)
        for i, item in enumerate(mode_items):
            if i != selected_item:
                menu_text = mode_menu_font.render(item["text"], True, GRAY)
            else:
                menu_text = mode_menu_font.render(item["text"], True, BLACK)
            rect = menu_text.get_rect(center=item["pos"])
            win.blit(menu_text, rect)
            win.blit(title_text, ((WIN_WIDTH - title_text.get_width()) / 2, 50))

        win.blit(cursor_img, cursor_rect)
        pygame.display.update()
