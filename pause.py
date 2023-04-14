import pygame

def run_pause_screen(screen):
    #배경색 설정
    screen.fill((255, 255, 255))
    
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render("Continue: ESC", True, (220, 20, 60))
    #텍스트 위치 설정, 좌측 상단 기준으로 10, 10만큼 떨어진 곳에 텍스트 출력
    text_rect = text.get_rect(top = 10, left = 10)
    screen.blit(text, text_rect)
    pygame.display.flip()
