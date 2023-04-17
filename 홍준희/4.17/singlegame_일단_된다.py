import pygame
import sys
import shuffle
from loadcard import Card
import Computerplay
from config import Configset
import pause

pygame.init()




def start_game():
    # 카드뽑기 함수, top에서
    def drawCards(numCards):
        cardsDrawn = []
        for x in range(numCards):
            cardsDrawn.append(card.pop(0))

        return cardsDrawn

    # 플레이어가 플레이 가능한지 판단, 버린카드보고
    def canPlay(colour, value, playerHand):
        for card in playerHand:
            if "Black" in card:
                return True
            elif colour in card or value in card:
                return True
        return False

    # 버리는카드
    discards = []
    colours = ["RED", "GREEN", "YELLOW", "BLUE"]
    # 플레이어
    players = []

    # 플레이어 인원 입력받기

    #일단 7명으로 임의로 지정
    numPlayers = 7

    # 플레이어 점수
    playerscore = []
    for i in range(numPlayers):
        playerscore.append(0)

    # 덱만들고 섞기
    unodeck = shuffle.UNODeck()
    temp = unodeck.deal(numPlayers)
    for hand in temp:
        players.append(hand)

    card = unodeck.getCards()

    #이전 저장파일 불러오기
    cf = Configset()
    default = cf.getChange()
    screen_width = int(default[0])
    screen_height = int(default[1])
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("UNO Game")

    # 다음 턴
    playerTurn = 0
    # 시계방향1 반시계방향 -1
    playDirection = 1



    # 처음 카드 1장 버리기
    discards.append(unodeck.cards.pop(0))

    # 와일드 드로우 4인거 체크하기
    while discards[-1] == 'BLACK_DRAW4':
        card.append(discards.pop(0))
        discards.append(card.pop(0))

    splitCard = discards[-1].split("_", 1)

    # 처음 카드색
    curruntcolour = splitCard[0]
    if curruntcolour != "BlACK":
        cardVal = splitCard[1]
    else:
        cardVal = "Any"

    # 승자
    winner = -1


    #'배경1.mp3' 파일 재생
    pygame.mixer.music.load('./이채은/sound/배경1.mp3')
    pygame.mixer.music.play(-1)
    '''
    # 전체화면 설정
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("UNO Game")
    '''
    # 색 정의
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    LIGHT_PINK = (255, 182, 193)
    GRAY = (128, 128, 128)
    RED = (255, 0, 0)
    LIGHT_YELLOW = (255, 255, 153)

    #섹션1 크기, 테두리 설정, 배경사진'background.png'
    section1_width = int(screen_width*0.80)
    section1_height = int(screen_height*0.60)
    section1 = pygame.Surface((section1_width, section1_height))

    background = pygame.image.load('./이채은/image/singleBG_c.png')
    background = pygame.transform.scale(background, (section1_width, section1_height))
    section1.blit(background, (0, 0, 10, 10))
    pygame.draw.rect(section1, LIGHT_YELLOW, (0, 0, section1_width, section1_height), 3)

    #섹션1 왼쪽에 'BACK.png' 이미지 띄우기
    back = pygame.image.load('./최회민/img/BACK.png')
    back = pygame.transform.scale(back, (int(section1_width*0.20), int(section1_height*0.45)))
    section1.blit(back, (120, 110, 10, 10))

    # 섹션1 왼쪽에 'BACK.png' 옆에 top카드 이미지 띄우기
    top = pygame.image.load('./최회민/img/{}.png'.format(discards[-1]))
    top = pygame.transform.scale(top, (int(section1_width * 0.20), int(section1_height * 0.45)))
    section1.blit(top, (300, 110, 10, 10))

    #'BACK.png' 이미지 누르면 ~기능 구현?

    # 현재 색 표시 칸 구현
    pygame.draw.circle(section1, WHITE, (int(section1_width*0.8), int(section1_height*0.45)), int(section1_width*0.05), 0)
    pygame.draw.circle(section1, LIGHT_YELLOW, (int(section1_width*0.8), int(section1_height*0.45)), int(section1_width*0.05), 3)

    # 색 표시 기능 구현

    #섹션2 크기, 배경색, 테두리 설정
    section2_width = int(screen_width*0.25)
    section2_height = section1_height
    section2 = pygame.Surface((section2_width, section2_height))
    section2.fill((LIGHT_YELLOW))
    pygame.draw.rect(section2, LIGHT_YELLOW, (0, 0, section2_width, section2_height), 3)

    #플레이어별 위치 구현
    p_width = int(section2_width / 1.0) # Width of each rectangle, slightly smaller than section2
    p_height = int((section2_height - 10) / 6) # Height of each rectangle, spaced apart by 2
    p_spacing = 3 # Spacing between rectangles

    p1_rect = pygame.Rect((section2_width - p_width) / 2, p_spacing, p_width*0.789, p_height)
    p2_rect = pygame.Rect((section2_width - p_width) / 2, p_height + p_spacing * 2, p_width*0.789, p_height)
    p3_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 2 + p_spacing * 3, p_width*0.789, p_height)
    p4_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 3 + p_spacing * 4, p_width*0.789, p_height)
    p5_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 4 + p_spacing * 5, p_width*0.789, p_height)
    p6_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 5 + p_spacing * 6, p_width*0.789, p_height*0.87)

    #p에 모두 'se2.png' 이미지 띄우기
    se2 = pygame.image.load('./이채은/image/se2.png')
    se2 = pygame.transform.scale(se2, (int(p_width*0.789), int(p_height)))
    section2.blit(se2, (p1_rect.x, p1_rect.y, 10, 10))
    section2.blit(se2, (p2_rect.x, p2_rect.y, 10, 10))
    section2.blit(se2, (p3_rect.x, p3_rect.y, 10, 10))
    section2.blit(se2, (p4_rect.x, p4_rect.y, 10, 10))
    section2.blit(se2, (p5_rect.x, p5_rect.y, 10, 10))
    section2.blit(se2, (p6_rect.x, p6_rect.y, 10, 10))


    #섹션2 플레이어별 이름 표시
    font = pygame.font.SysFont('comicsansms', 18)
    text = font.render('Player1', True, BLACK)
    section2.blit(text, (p1_rect.x + 10, p1_rect.y + 10, 10, 10))
    text = font.render('Player2', True, BLACK)
    section2.blit(text, (p2_rect.x + 10, p2_rect.y + 10, 10, 10))
    text = font.render('Player3', True, BLACK)
    section2.blit(text, (p3_rect.x + 10, p3_rect.y + 10, 10, 10))
    text = font.render('Player4', True, BLACK)
    section2.blit(text, (p4_rect.x + 10, p4_rect.y + 10, 10, 10))
    text = font.render('Player5', True, BLACK)
    section2.blit(text, (p5_rect.x + 10, p5_rect.y + 10, 10, 10))
    text = font.render('Player6', True, BLACK)
    section2.blit(text, (p6_rect.x + 10, p6_rect.y + 10, 10, 10))

    #섹션3 크기, 배경색, 테두리 설정
    section3_width = screen_width
    section3_height = int(screen_height*0.40)
    section3 = pygame.Surface((section3_width, section3_height))
    section3.fill((255, 255, 255))
    pygame.draw.rect(section3, LIGHT_YELLOW, (0, 0, section3_width, section3_height), 3)

    #섹션3 우측 상단에 타이머 표시 칸 구현
    timer_width = int(section3_width*0.05)
    timer_height = int(section3_height*0.25)
    timer_x = section3_width - timer_width - 15
    timer_y = 10

    #섹션3 우측 상단에 타이머 표시 칸 안에 "0" 텍스트 생성
    font = pygame.font.SysFont('comicsansms', 20)
    bold_font = pygame.font.SysFont('comicsansms', 15, bold=True)
    text = font.render("0", True, RED)
    text_rect = text.get_rect(center=(timer_x + timer_width / 2, timer_y + timer_height / 2))
    section3.blit(text, text_rect)

    #섹션3 좌측 상단에 "Your turn" 텍스트 생성
    font = pygame.font.SysFont('comicsansms', 20)
    text = font.render("Your turn", True, BLACK)
    text_rect = text.get_rect(center=(int(section3_width*0.1), int(section3_height*0.1)))
    section3.blit(text, text_rect)

    #"UNO!" 텍스트 생성
    font = pygame.font.SysFont('comicsansms', 20)
    bold_font = pygame.font.SysFont('comicsansms', 15, bold=True)
    text = font.render("UNO!", True, BLACK)
    text_rect = text.get_rect(center=(int(section3_width*0.23), int(section3_height*0.1)))
    pygame.draw.rect(section3, RED, (text_rect.x - 5, text_rect.y - 5, text_rect.width + 10, text_rect.height + 10), 3)
    section3.blit(text, text_rect)

    ##섹션3 우측 중앙에 마지막 한장 남았을때 누르는 버튼 구현
    #UNO_bt = pygame.image.load('./이채은/image/UNO_bt.png')
    #UNO_bt = pygame.transform.scale(UNO_bt, (150,110))
    #section3.blit(UNO_bt, (int(section3_width*0.72), int(section3_height*0.2), 10, 10))

    # 일시정지 및 종료 버튼 구현하고 "Pause" 텍스트 생성
    pause_button_width = 30
    pause_button_height = 30
    pause_button_x = section1_width - pause_button_width - 10
    pause_button_y = 10

    #"pause_button"배경 흰색으로 설정
    WHITE = (255, 255, 255)
    pause_button_rect = pygame.draw.rect(section1, LIGHT_YELLOW, (pause_button_x, pause_button_y, pause_button_width, pause_button_height))

    font = pygame.font.SysFont('comicsansms', 15)
    bold_font = pygame.font.SysFont('comicsansms', 15, bold=True)
    text = bold_font.render("||", True, BLACK)
    text_rect = text.get_rect(center=(pause_button_x + pause_button_width / 2, pause_button_y + pause_button_height / 2))
    section1.blit(text, text_rect)

    screen.blit(section1, (0, 0))
    screen.blit(section2, (section1_width, 0))
    screen.blit(section3, (0, section1_height))

    # 게임 시작할 때
    print(players[0])
    print(discards[-1])
    user_card = []
    for item in players[0]:
        cards = Card(item, (screen_width, screen_height))
        user_card.append(cards)
    i = 0
    temp_list = []
    for item in user_card:
        #item.update((50 + (screen_width / 10) * i, (screen_height * 0.35) / 2))
        item.update((50 + 50 * i, 500))
        temp_list.append(item)
        i += 1
    user_group = pygame.sprite.RenderPlain(*temp_list)
    user_group.draw(screen)  # 그리기


    pygame.display.flip()

    # 팝업창 폰트 지정
    font = pygame.font.SysFont('comicsansms', 20)

    running = True
    # 게임 루프 실행
    while running:



        # 0번 플레이어로 하고 나머지 컴퓨터로 하기

        # 컴퓨터인 경우 먼저하기
        if playerTurn != 0:
            pygame.time.wait(700)

            print("top ", discards[-1], "player turn",playerTurn+1)

            # 이함수 hand넘겨받는기능추가필요
            unoplayer = Computerplay.UnoPlayer(players[playerTurn])
            res = unoplayer.play_card(discards[-1], curruntcolour)

            # 컴퓨터 낼수 없는경우
            if res == None:
                players[playerTurn].extend(drawCards(1))
                # 1장 추가되는거 이미지로 구현
                # 턴 이동
                playerTurn += playDirection
                if playerTurn == numPlayers:
                    playerTurn = 0
                elif playerTurn < 0:
                    playerTurn = numPlayers - 1


            else:
                # 컴퓨터 낼수 있는경우

                discards.append(res)
                # 이거 이미 컴퓨터 메소드 호출시 삭제해준다
                # players[playerTurn].remove(res)

                # 컴퓨터도 카드 내서 카드 수 감소하는거 구현필요

                # if len(players[playerTurn]) == 1:
                # 컴퓨터 우노구현
                # 컴퓨터 승리조건
                if len(players[playerTurn]) == 0:
                    playing = False
                    winner = playerTurn + 1

                else:
                    # 버린카드 특별카드 체크
                    splitCard = discards[-1].split("_", 1)
                    curruntcolour = splitCard[0]

                    # 와일드면 카드값에 any부여
                    if curruntcolour == "BLACK":
                        cardVal = "Any"
                    else:
                        cardVal = splitCard[1]
                    # 와읻드면 색 선택하게
                    if curruntcolour == "BLACK":
                        unoplayer = Computerplay.UnoPlayer(players[playerTurn])
                        newColour = unoplayer.choose_color(players[playerTurn])
                        # curruntcolour = colours[newColour - 1]
                        curruntcolour = newColour
                    # 리버스면 다음턴 회전반대로
                    if cardVal == "REVERSE":
                        playDirection = playDirection * (-1)
                        if len(players) == 2:
                            playerTurn += playDirection
                            if playerTurn == numPlayers:
                                playerTurn = 0
                            elif playerTurn < 0:
                                playerTurn = numPlayers - 1

                    # 스킵하기
                    elif cardVal == "SKIP":
                        playerTurn += playDirection
                        if playerTurn == numPlayers:
                            playerTurn = 0
                        elif playerTurn < 0:
                            playerTurn = numPlayers - 1
                    # 2장 뽑기
                    elif cardVal == "DRAW2":
                        playerDraw = playerTurn + playDirection
                        if playerDraw == numPlayers:
                            playerDraw = 0
                        elif playerDraw < 0:
                            playerDraw = numPlayers - 1
                        players[playerDraw].extend(drawCards(2))
                    # 와일드 드로우 4
                    elif cardVal == "DRAW4":
                        playerDraw = playerTurn + playDirection
                        if playerDraw == numPlayers:
                            playerDraw = 0
                        elif playerDraw < 0:
                            playerDraw = numPlayers - 1
                        players[playerDraw].extend(drawCards(4))

                    # 턴 이동
                    playerTurn += playDirection
                    if playerTurn == numPlayers:
                        playerTurn = 0
                    elif playerTurn < 0:
                        playerTurn = numPlayers - 1

                    # top카드 이미지 변화
                    back = pygame.image.load('./최회민/img/{}.png'.format(discards[-1]))
                    back = pygame.transform.scale(back, (int(section1_width * 0.20), int(section1_height * 0.45)))
                    section1.blit(back, (300, 110, 10, 10))
                    pygame.display.update()

        # 사람인경우
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # "pause"버튼을 누르면 '배경.mp3'가 멈춘다.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button_rect.collidepoint(event.pos):
                    pygame.mixer.music.pause()
                    pygame.mixer.music.rewind()
                    pygame.display.update()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # "Pause" 버튼을 누르면 게임이 일시정지
            if event.type == pygame.MOUSEBUTTONDOWN:
                '''
                if pause_button_rect.collidepoint(event.pos):
                    pygame.time.wait(1000)
                    pygame.display.update()
                    # "Pause" 버튼을 누르면 "Continue", "Restart", "EndGame" 버튼 생성
                    pygame.draw.rect(screen, WHITE, (300, 230, 180, 40))
                    pygame.draw.rect(screen, WHITE, (300, 275, 180, 40))
                    pygame.draw.rect(screen, WHITE, (300, 320, 180, 40))
                    # 각각의 버튼에 "Continue", "Restart", "EndGame" 텍스트 생성
                    co_text = font.render("Continue", True, BLACK)
                    co_text_rect = co_text.get_rect(center=(300 + 150 / 2, 230 + 40 / 2))
                    screen.blit(co_text, co_text_rect)
                    re_text = font.render("Restart", True, BLACK)
                    re_text_rect = re_text.get_rect(center=(300 + 165 / 2, 275 + 40 / 2))
                    screen.blit(re_text, re_text_rect)
                    ex_text = font.render("EndGame", True, BLACK)
                    ex_text_rect = ex_text.get_rect(center=(300 + 140 / 2, 320 + 40 / 2))
                    screen.blit(ex_text, ex_text_rect)
                    pygame.display.flip()
                # ex_text를 누르면 게임이 종료되고 'startPage.py'로 돌아감
                if ex_text_rect.collidepoint(event.pos):
                    running = False
                # re_text를 누르면 'singlegame.py'가 다시 실행
                if re_text_rect.collidepoint(event.pos):
                    import singlegame
                    singlegame.singlegame()
                # co_text를 누르면 ex_text, re_text, co_text가 닫히고 '배경.mp3'가 다시 실행되며 게임이 이어서 진행됨
                # 계속 수정..
                if co_text_rect.collidepoint(event.pos):
                    pygame.draw.rect(screen, (255, 255, 0), (300, 230, 180, 40))
                    pygame.draw.rect(screen, (255, 255, 0), (300, 275, 180, 40))
                    pygame.draw.rect(screen, (255, 255, 0), (300, 320, 180, 40))
                    pygame.mixer.music.unpause()
                    pygame.display.flip()
                pygame.display.flip()
                '''


            if event.type == pygame.MOUSEBUTTONUP:
                if playerTurn == 0:
                    print("top ", discards[-1], "player turn", playerTurn + 1)
                    mouse_pos = pygame.mouse.get_pos()
                    # 내 카드 선택
                    for sprite in user_group:
                        if sprite.get_rect().collidepoint(mouse_pos):
                            if canPlay(curruntcolour, cardVal, players[playerTurn]):

                                # 카드 낼때
                                discards.append(sprite.get_name())
                                user_group.remove(sprite)  # 핸드에서 내려는 카드를 제거하고
                                players[playerTurn].remove(sprite.get_name())



                                for temp in user_group: # 남아있는 카드들에 대해
                                    temp.move(sprite.getposition()) # 제거한 카드의 위치에 대해 빈자리를 채우게 카드 이동
                                sprite.setposition(430, 300)
                                pygame.display.update()  # 화면 업데이트

                                # top카드 이미지 변화
                                #print(sprite.get_name())
                                #print(discards)


                                #print(discards[-1],11,"그만 좀 허락해줘")
                                top = pygame.image.load('./최회민/img/{}.png'.format(discards[-1]))
                                top = pygame.transform.scale(top,
                                                              (int(section1_width * 0.20),
                                                               int(section1_height * 0.45)))
                                section1.blit(top, (300, 110, 10, 10))
                                pygame.display.update()

                                # 플레이어의 카드 변화
                                item = players[playerTurn][-1]
                                lastcard1 = len(user_group)
                                temp = Card(item, (120, 110))
                                if lastcard1 > 8:
                                    x = 50 + screen_width / 10 * (lastcard1 - 8)
                                    y = screen_height * 0.35
                                else:
                                    x = 50 + screen_width / 10 * lastcard1
                                    y = screen_height * 0.35 / 2
                                temp.setposition(x, y)
                                user_group.add(temp)
                                pygame.display.update()  # 화면 업데이트

                                # 버린카드 특별카드 체크
                                splitCard = discards[-1].split("_", 1)
                                curruntcolour = splitCard[0]

                                # 와일드면 카드값에 any부여
                                if curruntcolour == "BLACK":
                                    cardVal = "Any"
                                else:
                                    cardVal = splitCard[1]
                                # 와읻드면 색 선택하게
                                if curruntcolour == "BLACK":
                                    unoplayer = Computerplay.UnoPlayer(players[playerTurn])
                                    newColour = unoplayer.choose_color(players[playerTurn])
                                    curruntcolour = newColour

                                    '''
                                    newColour = Computerplay.UnoPlayer.choose_color(players[playerTurn])
                                    curruntcolour = colours[newColour - 1]
                                    '''
                                # 리버스면 다음턴 회전반대로
                                if cardVal == "REVERSE":
                                    playDirection = playDirection * (-1)
                                    if len(players) == 2:
                                        playerTurn += playDirection
                                        if playerTurn == numPlayers:
                                            playerTurn = 0
                                        elif playerTurn < 0:
                                            playerTurn = numPlayers - 1

                                # 스킵하기
                                elif cardVal == "SKIP":
                                    playerTurn += playDirection
                                    if playerTurn == numPlayers:
                                        playerTurn = 0
                                    elif playerTurn < 0:
                                        playerTurn = numPlayers - 1
                                # 2장 뽑기
                                elif cardVal == "DRAW2":
                                    playerDraw = playerTurn + playDirection
                                    if playerDraw == numPlayers:
                                        playerDraw = 0
                                    elif playerDraw < 0:
                                        playerDraw = numPlayers - 1
                                    players[playerDraw].extend(drawCards(2))
                                # 와일드 드로우 4
                                elif cardVal == "DRAW4":
                                    playerDraw = playerTurn + playDirection
                                    if playerDraw == numPlayers:
                                        playerDraw = 0
                                    elif playerDraw < 0:
                                        playerDraw = numPlayers - 1
                                    players[playerDraw].extend(drawCards(4))

                                # 턴 이동
                                playerTurn += playDirection
                                if playerTurn == numPlayers:
                                    playerTurn = 0
                                elif playerTurn < 0:
                                    playerTurn = numPlayers - 1
                                break
                    # 이건 덱에서 카드 뽑기

                    if sprite.get_rect().collidepoint(mouse_pos):

                        # 카드선택할 수 없으면
                        players[playerTurn].extend(drawCards(1))

                        # 플레이어의 카드 변화
                        item = players[playerTurn][-1]
                        lastcard1 = len(user_group.sprite())
                        temp = Card(item, (120, 110))

                        if lastcard1 > 8:
                            x = 50 + screen_width / 10 * (lastcard1 - 8)
                            y = screen_height * 0.35
                        else:
                            x = 50 + screen_width / 10 * lastcard1
                            y = screen_height * 0.35 / 2
                        temp.setposition(x, y)
                        user_group.add(temp)
                        pygame.display.update()  # 화면 업데이트

                        # 턴 이동
                        playerTurn += playDirection
                        if playerTurn == numPlayers:
                            playerTurn = 0
                        elif playerTurn < 0:
                            playerTurn = numPlayers - 1

                        break





    # 점수계산
    # 일반카드 숫자대로 / 와일드와 와일드 드로우4 50점/ 500점 나오면 전체 승리
    # 드로우2, 리버스, 스킵 20점
    score = 0
    for player in players:
        for j in range(len(player)):
            curruntcard = player[j].split("_", 1)
            # 처음 카드색
            if splitCard[0] == "BLACK":
                score += 50
            else:
                if splitCard[1] == "REVERSE" or splitCard[1] == "SKIP" or splitCard[1] == "DRAW2":
                    score += 20
                else:
                    score += splitCard[1]

    # 토탈 점수 계산해 500이상이면 완전끝
    playerscore[playerTurn - 1] += score
    if playerscore[playerTurn - 1] >= 500:
        running= False
