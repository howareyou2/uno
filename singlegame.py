import pygame

# 파이게임 초기화
pygame.init()

def start_game():

    # 창 생성
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # 배경 이미지 불러오기
    background_image = pygame.image.load("./이채은/image/Sback.png")
    #배경이미지 크기 조정
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))  
    
    
    # 게임 루프
    while True:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
        # 화면에 배경 이미지 그리기
        screen.blit(background_image, (0, 0))
    
        # 화면 업데이트
        pygame.display.update()
    