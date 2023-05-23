import pygame
import achievement

pygame.init()

def achiev():
    WIN_WIDTH = 800
    WIN_HEIGHT = 600
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)
    YELLOW = (200,200,0)

    title_font = pygame.font.SysFont('comicsansms', 50)
    menu_font = pygame.font.SysFont('comicsansms', 25)
    docu_font = pygame.font.SysFont('comicsansms', 15)

    title_text = title_font.render('ACHIEVEMENT', True, BLACK)

    achiev1_menu = menu_font.render('Singlegame WIN', True, BLACK)
    achiev1_docu = docu_font.render('Player wins singlegame', False, BLACK)
    achiev2_menu = menu_font.render('Story A Clear', True, BLACK)
    achiev2_docu = docu_font.render('Player cleared story A', False, BLACK)
    achiev3_menu = menu_font.render('Story B Clear', True, BLACK)
    achiev3_docu = docu_font.render('Player cleared story B', False, BLACK)
    achiev4_menu = menu_font.render('Story C Clear', True, BLACK)
    achiev4_docu = docu_font.render('Player cleared story C', False, BLACK)
    achiev5_menu = menu_font.render('Story D Clear', True, BLACK)
    achiev5_docu = docu_font.render('Player cleared story D', False, BLACK)
    achiev6_menu = menu_font.render('In 10 turn', True, BLACK)
    achiev6_docu = docu_font.render('Player wins a game in 10 turn', False, BLACK)
    achiev7_menu = menu_font.render('Not Use Skill Card', True, BLACK)
    achiev7_docu = docu_font.render('Player wins a game not using skill card', False, BLACK)
    achiev8_menu = menu_font.render('Use One color', True, BLACK)
    achiev8_docu = docu_font.render('Player wins a game using one color', False, BLACK)
    achiev9_menu = menu_font.render('Use Two colors', True, BLACK)
    achiev9_docu = docu_font.render('Player wins a game using two colors', False, BLACK)
    achiev10_menu = menu_font.render('Use 10seconds', True, BLACK)
    achiev10_docu = docu_font.render('Player wins a game using 10 seconds', False, BLACK)


    back_arrow = pygame.image.load('./img/back_arrow.png')
    back_arrow = pygame.transform.scale(back_arrow,(40,40))

    achiev1=pygame.image.load('./img/ahv1.png')
    achiev1=pygame.transform.scale(achiev1, (30,50))
    achiev2=pygame.image.load('./img/ahv2.png')
    achiev2=pygame.transform.scale(achiev2, (30,50))
    achiev3=pygame.image.load('./img/ahv3.png')
    achiev3=pygame.transform.scale(achiev3, (30,50))
    achiev4=pygame.image.load('./img/ahv4.png')
    achiev4=pygame.transform.scale(achiev4, (30,50))
    achiev5=pygame.image.load('./img/ahv5.png')
    achiev5=pygame.transform.scale(achiev5, (30,50))
    achiev6=pygame.image.load('./img/ahv6.png')
    achiev6=pygame.transform.scale(achiev6, (30,50))
    achiev7=pygame.image.load('./img/ahv7.png')
    achiev7=pygame.transform.scale(achiev7, (30,50))
    achiev8=pygame.image.load('./img/ahv8.png')
    achiev8=pygame.transform.scale(achiev8, (30,50))
    achiev9=pygame.image.load('./img/ahv9.png')
    achiev9=pygame.transform.scale(achiev9, (30,50))

    notachiev1=pygame.image.load('./img/nahv1.png')
    notachiev1=pygame.transform.scale(notachiev1, (30,50))
    notachiev2=pygame.image.load('./img/nahv2.png')
    notachiev2=pygame.transform.scale(notachiev2, (30,50))
    notachiev3=pygame.image.load('./img/nahv3.png')
    notachiev3=pygame.transform.scale(notachiev3, (30,50))
    notachiev4=pygame.image.load('./img/nahv4.png')
    notachiev4=pygame.transform.scale(notachiev4, (30,50))
    notachiev5=pygame.image.load('./img/nahv5.png')
    notachiev5=pygame.transform.scale(notachiev5, (30,50))
    notachiev6=pygame.image.load('./img/nahv6.png')
    notachiev6=pygame.transform.scale(notachiev6, (30,50))
    notachiev7=pygame.image.load('./img/nahv7.png')
    notachiev7=pygame.transform.scale(notachiev7, (30,50))
    notachiev8=pygame.image.load('./img/nahv8.png')
    notachiev8=pygame.transform.scale(notachiev8, (30,50))
    notachiev9=pygame.image.load('./img/nahv9.png')
    notachiev9=pygame.transform.scale(notachiev9, (30,50))

    achieve_text=menu_font.render('Complete', False, YELLOW)
    notachieve_text=menu_font.render('Proceed', False, BLACK)

    achieve=achievement.Achievement()

    singleWin=achieve.getSingleWin()
    storyAWin=achieve.getStoryAWin()
    storyBWin=achieve.getStoryBWin()
    storyCWin=achieve.getStoryCWin()
    storyDWin=achieve.getStoryDWin()
    in10Turn=achieve.getIn10Turn()
    notUseSkill=achieve.getNotUseSkil()
    oneColor=achieve.getOneColor()
    twoColors=achieve.getTwoColors()
    in10seconds=achieve.getin10seconds()


    achieve1_time=menu_font.render(singleWin['time'], False, BLACK)
    achieve2_time=menu_font.render(storyAWin['time'], False, BLACK)
    achieve3_time=menu_font.render(storyBWin['time'], False, BLACK)
    achieve4_time=menu_font.render(storyCWin['time'], False, BLACK)
    achieve5_time=menu_font.render(storyDWin['time'], False, BLACK)
    achieve6_time=menu_font.render(in10Turn['time'], False, BLACK)
    achieve7_time=menu_font.render(notUseSkill['time'], False, BLACK)
    achieve8_time=menu_font.render(oneColor['time'], False, BLACK)
    achieve9_time=menu_font.render(twoColors['time'], False, BLACK)
    achieve10_time=menu_font.render(in10seconds['time'], False, BLACK)







    running=True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = event.pos
                if back_arrow_rect.collidepoint(position):
                    running = False
        win.fill(WHITE)
        #pygame.draw.rect(win, GRAY, (WIN_WIDTH//2 - 150, 150, 300, 300))
        win.blit(title_text,((WIN_WIDTH - title_text.get_width()) / 2, 10))

        win.blit(achiev1_menu, (100, 100))
        win.blit(achiev1_docu, (130, 130))
        win.blit(achieve1_time,(600, 125))
    
        if(singleWin['achieve']=='True'):
            win.blit(achiev1, (20, 100))
            win.blit(achieve_text,(600,100))
        else:
            win.blit(notachiev1,(20,100))
            win.blit(notachieve_text,(600,100))
        
        win.blit(achiev2_menu, (100, 150))
        win.blit(achiev2_docu, (130, 180))
        win.blit(achieve2_time,(600, 175))

        if(storyAWin['achieve']=='True'):
            win.blit(achiev2, (20, 150))
            win.blit(achieve_text,(600,150))
       
        else:
            win.blit(notachiev2,(20,150))
            win.blit(notachieve_text,(600,150))
        
        win.blit(achiev3_menu, (100, 200))
        win.blit(achiev3_docu, (130, 230))
        win.blit(achieve3_time,(600, 225))

        if(storyBWin['achieve']=='True'):
            win.blit(achiev3, (20, 200))
            win.blit(achieve_text,(600,200))
        
        else:
            win.blit(notachiev3,(20,200))
            win.blit(notachieve_text,(600,200))
        
        win.blit(achiev4_menu, (100, 250))
        win.blit(achiev4_docu, (130, 280))
        win.blit(achieve4_time,(600, 275))

        if(storyCWin['achieve']=='True'):
            win.blit(achiev4, (20, 250))
            win.blit(achieve_text,(600,250))
        
        else:
            win.blit(notachiev4,(20,250))
            win.blit(notachieve_text,(600,250))

        win.blit(achiev5_menu, (100, 300))
        win.blit(achiev5_docu, (130, 330))
        win.blit(achieve5_time,(600, 325))

        if(storyDWin['achieve']=='True'):
            win.blit(achiev5, (20, 300))
            win.blit(achieve_text,(600,300))
        
        else:
            win.blit(notachiev5,(20,300))
            win.blit(notachieve_text,(600,300))

        win.blit(achiev6_menu, (100, 350))
        win.blit(achiev6_docu, (130, 380))
        win.blit(achieve6_time,(600, 375))

        if(in10Turn['achieve']=='True'):
            win.blit(achiev6, (20, 350))
            win.blit(achieve_text,(600,350))

        else:
            win.blit(notachiev6,(20,350))    
            win.blit(notachieve_text,(600,350))
    
        win.blit(achiev7_menu, (100, 400))
        win.blit(achiev7_docu, (130, 430))
        win.blit(achieve7_time,(600, 425))

        if(notUseSkill['achieve']=='True'):
            win.blit(achiev7, (20, 400))
            win.blit(achieve_text,(600,400))
        
        else:
            win.blit(notachiev7,(20,400))    
            win.blit(notachieve_text,(600,400))
        
        win.blit(achiev8_menu, (100, 450))
        win.blit(achiev8_docu, (130, 480))
        win.blit(achieve8_time,(600, 475))

        if(notUseSkill['achieve']=='True'):
            win.blit(achiev8, (20, 450))
            win.blit(achieve_text,(600,450))
        
        else:
            win.blit(notachiev8,(20,450))    
            win.blit(notachieve_text,(600,450))
        
        win.blit(achiev9_menu, (100, 500))
        win.blit(achiev9_docu, (130, 530))
        win.blit(achieve9_time,(600, 525))

        if(notUseSkill['achieve']=='True'):
            win.blit(achiev8, (20, 500))
            win.blit(achieve_text,(600,500))
        
        else:
            win.blit(notachiev8,(20,500))    
            win.blit(notachieve_text,(600,500))
        
        win.blit(achiev10_menu, (100, 550))
        win.blit(achiev10_docu, (130, 580))
        win.blit(achieve10_time,(600, 570))

        if(notUseSkill['achieve']=='True'):
            win.blit(achiev9, (20, 550))
            win.blit(achieve_text,(600,550))
        
        else:
            win.blit(notachiev9,(20,550))    
            win.blit(notachieve_text,(600,550))
                           
        win.blit(back_arrow,(730,30))                       
        back_arrow_rect = back_arrow.get_rect()
        back_arrow_rect.center = (750, 50)
                                    
        pygame.display.update()
