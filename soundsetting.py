import pygame

pygame.init()

def sound():



    # 화면 크기 설정
    screen = pygame.display.set_mode((800,600))
    screen.fill((255,255,255))
    # 화면 타이틀 설정
    pygame.display.set_caption("sound setting")

    title_font = pygame.font.SysFont('comicsansms', 80)

    # Create text surfaces
    title_text = title_font.render('Sound setting', True,(0,0,0))

    screen.blit(title_text, (100, 100))
    


    
    pygame.display.flip()
sound()
