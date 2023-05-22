import pygame
import settings

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Set up the window
WIN_WIDTH = 800
WIN_HEIGHT = 600

def create_menu_surface(font, text, selected):
    color = BLACK if selected else GRAY
    return font.render(text, True, color)

def pause_screen():
    # Initialize pygame
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Pause")

    # Load fonts
    title_font = pygame.font.SysFont('comicsansms', 80)
    menu_font = pygame.font.SysFont('comicsansms', 50)

    # Create text surfaces
    title_text = title_font.render('Pause!', True, BLACK)

    # Define menu items
    menu_items = [
        {"text": "Back", "pos": (WIN_WIDTH // 2, 200)},
        {"text": "Achievement", "pos": (WIN_WIDTH // 2, 260)},
        {"text": "Settings", "pos": (WIN_WIDTH // 2, 320)},
        {"text": "End Game", "pos": (WIN_WIDTH // 2, 380)},
    ]

    # Set up the cursor
    cursor_img = pygame.Surface((20, 20))
    cursor_img.fill(WHITE)
    cursor_rect = cursor_img.get_rect()

    # Set up the menu
    selected_item = 0

    running = True
    # Game loop
    while running:
        # Event handling
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    if selected_item == 0:
                        running = False
                    elif selected_item == 1:
                        print(1)
                    elif selected_item == 2:
                        settings.settings_screen()
                    elif selected_item == 3:
                        running = False
            elif event.type == pygame.MOUSEMOTION:
                cursor_rect.center = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, item in enumerate(menu_items):
                    if cursor_rect.collidepoint(item["pos"]):
                        selected_item = i
                        if selected_item == 0:
                            running = False
                        elif selected_item == 1:
                            print(1)
                        elif selected_item == 2:
                            settings.settings_screen()
                        elif selected_item == 3:
                            running = False

        # Draw the menu
        screen.fill(WHITE)
        screen.blit(title_text, ((WIN_WIDTH - title_text.get_width()) // 2, 50))

        for i, item in enumerate(menu_items):
            text_surface = create_menu_surface(menu_font, item["text"], i == selected_item)
            rect = text_surface.get_rect(center=item["pos"])
            if rect.collidepoint(cursor_rect.center):
                text_surface = create_menu_surface(menu_font, item["text"], i == selected_item)
            screen.blit(text_surface, rect)

        pygame.display.update()

    pygame.quit()

# Example usage
#pause_screen()
