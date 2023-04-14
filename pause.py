import pygame

def run_pause_screen(screen):
    #배경색 설정
    screen.fill((255, 255, 255))
    
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render("Close : space", True, (0, 0, 0))
    #텍스트 위치 설정, 우측 하단에 위치
    text_rect = text.get_rect(center=(screen.get_width() - 100, screen.get_height() - 50))
    screen.blit(text, text_rect)
    pygame.display.flip()
