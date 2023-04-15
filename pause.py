import pygame
import singlegame


# Set up the window
WIN_WIDTH = 800
WIN_HEIGHT = 600



def run_pause_screen(screen):

      # 게임화면의 크기 설정
    WIDTH = 800
    HEIGHT = 600

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)

    background_color = (255, 255, 255)  # 흰색

    # 게임화면 생성
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    pygame.display.set_caption("pause")

    title_font = pygame.font.SysFont('comicsansms', 80)
    menu_font = pygame.font.SysFont('comicsansms', 50)

    # Create text surfaces
    title_text = title_font.render('pause!', True, BLACK)
    
    # Define menu items
    menu_items = [
        {"text": "Restart", "pos": (WIN_WIDTH // 2, 280)},
        {"text": "EndGame", "pos": (WIN_WIDTH // 2,360)},
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
            # 키보드 키 입력받는 부분
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    # 키보드로 박스 선택 , 위치순서대로
                    if selected_item == 0:
                        singlegame.start_game()
                    elif selected_item == 1:
                        print(1)


                        
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
                                singlegame.start_game()
                            elif selected_item == 1:
                                print(1)
                                
                            
                                
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

#defining font
            font = pygame.font.SysFont('comicsansms', 20)
            text = font.render("Continue : ESC", True, (220, 20, 60))
    #텍스트 위치 설정, 좌측 상단에 위치
            text_rect = text.get_rect(left=10, top=10)
            screen.blit(text, text_rect)

        # 게임화면 업데이트

        pygame.display.update()

