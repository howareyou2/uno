import pygame
pygame.init()
import settings

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
                    print("Single player selected")
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
                            print("Single player selected")
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