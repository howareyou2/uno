import pygame
pygame.init()
import settings

#'배경.mp3' 파일을 불러와서 재생합니다.
pygame.mixer.music.load('./이채은/sound/배경.mp3')
pygame.mixer.music.play(-1)

# Set up the window
WIN_WIDTH = 800
WIN_HEIGHT = 600
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("UNO")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Define fonts
title_font = pygame.font.SysFont('comicsansms', 80)
menu_font = pygame.font.SysFont('comicsansms', 50)
popup_menu_font = pygame.font.SysFont('comicsansms', 50)

# Create text surfaces
title_text = title_font.render('UNO', True, BLACK)

# Set up menu buttons
button_width = 200
button_height = 100
button_padding = 20


# Define menu items
menu_items = [
    {"text": "Single Player", "pos": (WIN_WIDTH//2, 200)},
    {"text": "Settings", "pos": (WIN_WIDTH//2, 320)},
    {"text": "Exit", "pos": (WIN_WIDTH//2, 440)}
]

# Set up the cursor
cursor_img = pygame.Surface((20, 20))
cursor_img.fill(WHITE)
cursor_rect = cursor_img.get_rect()

# Set up the menu
selected_item = 0

#Set up the menu in Popup
selected_in_popup_item = 0

#popup window check
popup_check = False

# Set up popup window
popup_win_width = 300
popup_win_height = 150
popup_win = pygame.Surface((popup_win_width, popup_win_height))
popup_win.fill(WHITE)
popup_win_rect = popup_win.get_rect(center=(WIN_WIDTH//2, WIN_HEIGHT//2))

# Set up popup window buttons
popup_win_button_width = 100
popup_win_button_height = 50
popup_win_button_padding = 20

popup_win_buttons = [
    {"text": "Only Play", "pos": (popup_win_width//2, popup_win_button_padding)},
    {"text": "Story Mode", "pos": (popup_win_width//2, popup_win_height//2+popup_win_button_padding)}
]

# Render button text surfaces and get their rects
popup_win_button_rects = []
for i, button in enumerate(popup_win_buttons):
    button_surface = menu_font.render(button["text"], True, BLACK)
    button_rect = button_surface.get_rect(center=button["pos"])
    popup_win_buttons[i]["surface"] = button_surface  # Add text surface to button dict
    popup_win_button_rects.append(button_rect)

# Blit button text onto popup_win surface
# for button in popup_win_buttons:
#     popup_win.blit(button["surface"], button["surface"].get_rect(center=button["pos"]))

# Define running_popup function
def running_popup():
    global popup_check, selected_in_popup_item
    popup_check = True
    selected_in_popup_item = 0
    while popup_check:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                popup_check = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup_check = False
                elif event.key == pygame.K_UP:
                    selected_in_popup_item = (selected_in_popup_item - 1) % len(popup_win_buttons)
                elif event.key == pygame.K_DOWN:
                    selected_in_popup_item = (selected_in_popup_item + 1) % len(popup_win_buttons)
                elif event.key == pygame.K_RETURN:
                    if selected_in_popup_item == 0:
                        # Only play button selected
                        import 이채은.singlegame1 as singlegame1
                        singlegame1.single_game()
                    elif selected_in_popup_item == 1:
                        # Story mode button selected
                        print("Story mode button selected")
                    popup_check = False
            elif event.type == pygame.MOUSEMOTION:
                cursor_rect.center = event.pos
            # Handle mouse button down events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("clicked!")
                # Check if the mouse click is outside of the popup_win_rect
                if not popup_win_rect.collidepoint(event.pos):
                    popup_check = False
                elif event.button == 1:
                    for i, button_rect in enumerate(popup_win_buttons):
                        if cursor_rect.collidepoint(button_rect["pos"]):
                            selected_in_popup_item = i
                            if selected_in_popup_item == 0:
                                # Only play button selected
                                import 이채은.singlegame1 as singlegame1
                                singlegame1.single_game()
                            elif selected_in_popup_item == 1:
                                print("story mode")
                            popup_check = False
        # Draw popup window
        win.blit(popup_win, popup_win_rect)

        # Draw popup window buttons
        for i, button in enumerate(popup_win_buttons):
            button_surface = popup_menu_font.render(button["text"], True, BLACK if i == selected_in_popup_item else GRAY)
            rect = button_surface.get_rect(center=button["pos"])
            if rect.collidepoint(cursor_rect.center):
                text = popup_menu_font.render(button["text"], True, BLACK if i == selected_in_popup_item else GRAY)
            #pygame.draw.rect(win, color, button["surface"].get_rect(center=button["pos"]), 3)
            #popup_win.blit(button["surface"], button["surface"].get_rect(center=button["pos"]))
            popup_win.blit(button_surface, rect)

        pygame.display.update()


# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP:
                selected_item = (selected_item - 1) % len(menu_items)
            elif event.key == pygame.K_DOWN:
                selected_item = (selected_item + 1) % len(menu_items)
            elif event.key == pygame.K_RETURN:
                if selected_item == 0:
                    running_popup()
                elif selected_item == 1:
                    settings.settings_screen()
                elif selected_item == 2:
                    running = False

        elif event.type == pygame.MOUSEMOTION:
            cursor_rect.center = event.pos
        # Handle mouse button down events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("click!")
            if event.button == 1:
                for i, item in enumerate(menu_items):
                    if cursor_rect.collidepoint(item["pos"]):
                        # text = menu_font.render(item["text"], True, BLACK if i == selected_item else GRAY)
                        selected_item = i
                        if selected_item == 0:
                            running_popup()
                        elif selected_item == 1:
                            settings.settings_screen()
                        elif selected_item == 2:
                            running = False


    # Draw the menu
    win.fill(WHITE)
    #pygame.draw.rect(win, GRAY, (WIN_WIDTH//2 - 150, 150, 300, 300))
    win.blit(title_text,((WIN_WIDTH - title_text.get_width()) / 2, 50))
    for i, item in enumerate(menu_items):
        text = menu_font.render(item["text"], True, BLACK if i == selected_item else GRAY)
        rect = text.get_rect(center=item["pos"])
        if rect.collidepoint(cursor_rect.center):
            #text=GRAY
            text = menu_font.render(item["text"], True, BLACK if i == selected_item else GRAY)
        win.blit(text, rect)

    # Draw the cursor
    win.blit(cursor_img, cursor_rect)

    # Update the display
    pygame.display.update()

pygame.quit()