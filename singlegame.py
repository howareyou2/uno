import pygame
import sys

import loadcard
import shuffle
from loadcard import Card
import Computerplay
from config import Configset
import pause
import achievement
import datetime
import json

pygame.init()


def timer(total_time, font, RED, timer_x, timer_width, timer_y, timer_height, section3, WHITE):
    start_ticks = pygame.time.get_ticks()
    while True:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if total_time <= elapsed_time:
            break
        text = font.render(str(int(total_time - elapsed_time)), True, RED)
        text_rect = text.get_rect(center=(timer_x + timer_width / 2, timer_y + timer_height / 2))

        # Draw a rectangle with white color as background
        background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20,
                                      text_rect.height + 20)
        pygame.draw.rect(section3, WHITE, background_rect)

        # Now draw the text
        section3.blit(text, text_rect)

        pygame.display.update()

def show_color_popup(screen, width, height, font, colors, color_values):
    rects = []

    popup_x = (screen.get_width() - width) // 2
    popup_y = (screen.get_height() - height) // 2

    for i in range(4):
        rect_x = popup_x + 20 + i * 120
        rect_y = popup_y + 25
        rect = pygame.Rect(rect_x, rect_y, 50, 50)
        rects.append(rect)
        pygame.draw.rect(screen, color_values[i], rect)
        color_text = font.render(colors[i], True, (0, 0, 0))
        color_text_rect = color_text.get_rect(center=rect.center)
        screen.blit(color_text, color_text_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(rects):
                    if rect.collidepoint(mouse_pos):
                        return colors[i]

def change_turn(playDirection, numPlayers, playerTurn):
    # 턴 이동
    playerTurn += playDirection
    if playerTurn == numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers - 1
    return playerTurn

# 텍스트 생성 함수
def render_timer():
    current_time = datetime.datetime.now()
    time_left = end_time - current_time
    if time_left.total_seconds() <= 0:
        text = bold_font.render("Time's up!", True, (255, 0, 0))
    else:
        seconds_left = int(time_left.total_seconds())
        text = font.render(str(seconds_left), True, (0, 0, 0))
    text_rect = text.get_rect(center=(timer_x + timer_width / 2, timer_y + timer_height / 2))
    section3.blit(text, text_rect)


def next_draw(numPlayers, playDirection, playerTurn):
    playerDraw = playerTurn + playDirection
    if playerDraw == numPlayers:
        playerDraw = 0
    elif playerDraw < 0:
        playerDraw = numPlayers - 1
    return playerDraw


def start_game():

    # 업적 개체 선언
    achieve = achievement.Achievement()
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

    # 플레이어 낸카드 가능한건지 체크하기
    def check_card(colour, value, sprite):
        name = sprite.get_name()
        name = name.split('_')
        if name[0] == 'BLACK':
            return True
        elif name[0] == colour:
            return True
        elif name[1] == value:
            return True
        else:
            return False

    # 버리는카드
    discards = []
    colours = ["RED", "GREEN", "YELLOW", "BLUE"]
    # 플레이어
    players = []

    # 플레이어 인원 입력받기

    numPlayers = json.load(open('players.json'))['players']


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


    # 이전 저장파일 불러오기
    cf = Configset()
    default = cf.getChange()
    screen_width = int(default[0])
    screen_height = int(default[1])
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("UNO Game")

    # 다음 턴
    playerTurn = 0
    turn = 0

    # 시계방향1 반시계방향 -1
    playDirection = 1

    # Set up 유저 카드
    selected_item = 0

    # 처음 카드 1장 버리기
    discards.append(card.pop(0))

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

    # '배경1.mp3' 파일 재생
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
    GREEN = (0, 255, 0)  # 녹색 추가
    LIGHT_YELLOW = (255, 255, 153)

    # 섹션1 크기, 테두리 설정, 배경사진'background.png'
    section1_width = int(screen_width * 0.80)
    section1_height = int(screen_height * 0.60)
    section1 = pygame.Surface((section1_width, section1_height))

    background = pygame.image.load('./이채은/image/singleBG_c.png')
    background = pygame.transform.scale(background, (section1_width, section1_height))
    section1.blit(background, (0, 0, 10, 10))
    pygame.draw.rect(section1, LIGHT_YELLOW, (0, 0, section1_width, section1_height), 3)
    '''
    # 현재 색 표시 칸 구현

    pygame.draw.circle(section1, WHITE, (int(section1_width * 0.8), int(section1_height * 0.45)),
                       int(section1_width * 0.05), 0)
    pygame.draw.circle(section1, LIGHT_YELLOW, (int(section1_width * 0.8), int(section1_height * 0.45)),
                       int(section1_width * 0.05), 3)
    pygame.draw.circle(section1, GREEN, (int(section1_width * 0.8), int(section1_height * 0.45)),
                       int(section1_width * 0.05), 0)
    '''
    # 현재 색 표시 칸 구현
    if curruntcolour == 'BLUE':
        pygame.draw.circle(section1, BLUE,
                           (int(section1_width * 0.8), int(section1_height * 0.45)),
                           int(section1_width * 0.05), 0)
    elif curruntcolour == 'RED':
        pygame.draw.circle(section1, RED,
                           (int(section1_width * 0.8), int(section1_height * 0.45)),
                           int(section1_width * 0.05), 0)
    elif curruntcolour == 'YELLOW':
        pygame.draw.circle(section1, LIGHT_YELLOW,
                           (int(section1_width * 0.8), int(section1_height * 0.45)),
                           int(section1_width * 0.05), 0)
    elif curruntcolour == 'GREEN':
        pygame.draw.circle(section1, GREEN,
                           (int(section1_width * 0.8), int(section1_height * 0.45)),
                           int(section1_width * 0.05), 0)

    # Inside your game loop where you want to draw the text
    len(card)
    font = pygame.font.Font(None, 24)
    card_count_text = str(len(card))  # convert the card count to string
    text_surface = font.render(card_count_text, True, BLACK)  # render the text
    text_rect = text_surface.get_rect(
        center=(int(section1_width * 0.8), int(section1_height * 0.45)))  # get the rect for positioning
    section1.blit(text_surface, text_rect)  # draw the text to the section1 surface
    pygame.display.update()






    # 색 표시 기능 구현

    # 섹션2 크기, 배경색, 테두리 설정
    section2_width = int(screen_width * 0.25)
    section2_height = screen_height
    section2 = pygame.Surface((section2_width, section2_height))
    section2.fill((LIGHT_YELLOW))
    pygame.draw.rect(section2, LIGHT_YELLOW, (0, 0, section2_width, section2_height), 3)

    # 플레이어별 위치 구현
    p_width = int(section2_width / 1.0)  # Width of each rectangle, slightly smaller than section2
    p_height = int((section2_height - 10) / 6)  # Height of each rectangle, spaced apart by 2
    p_spacing = 3  # Spacing between rectangles

    p1_rect = pygame.Rect((section2_width - p_width) / 2, p_spacing, p_width * 0.789, p_height)
    p2_rect = pygame.Rect((section2_width - p_width) / 2, p_height + p_spacing * 2, p_width * 0.789, p_height)
    p3_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 2 + p_spacing * 3, p_width * 0.789, p_height)
    p4_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 3 + p_spacing * 4, p_width * 0.789, p_height)
    p5_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 4 + p_spacing * 5, p_width * 0.789, p_height)
    p6_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 5 + p_spacing * 6, p_width * 0.789, p_height)

    # p에 모두 'se2.png' 이미지 띄우기
    se2 = pygame.image.load('./이채은/image/se2.png')
    se2 = pygame.transform.scale(se2, (int(p_width * 0.789), int(p_height)))
    section2.blit(se2, (p1_rect.x, p1_rect.y, 10, 10))
    section2.blit(se2, (p2_rect.x, p2_rect.y, 10, 10))
    section2.blit(se2, (p3_rect.x, p3_rect.y, 10, 10))
    section2.blit(se2, (p4_rect.x, p4_rect.y, 10, 10))
    section2.blit(se2, (p5_rect.x, p5_rect.y, 10, 10))
    section2.blit(se2, (p6_rect.x, p6_rect.y, 10, 10))

    # 섹션2 플레이어별 이름 표시
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



    # 섹션3 크기, 배경색, 테두리 설정
    section3_width = section1_width
    section3_height = int(screen_height * 0.40)
    section3 = pygame.Surface((section3_width, section3_height))
    section3.fill((255, 255, 255))
    pygame.draw.rect(section3, LIGHT_YELLOW, (0, 0, section3_width, section3_height), 3)

    # 섹션3 우측 상단에 타이머 표시 칸 구현
    timer_width = int(section3_width * 0.05)
    timer_height = int(section3_height * 0.25)
    timer_x = section3_width - timer_width - 15
    timer_y = 10

    # Draw a rectangle with white color as background
    timer_rect = pygame.Rect(timer_x, timer_y, timer_width, timer_height)
    pygame.draw.rect(section3, WHITE, timer_rect)


    # 섹션3 우측 상단에 타이머 표시 칸 안에 "0" 텍스트 생성
    font = pygame.font.SysFont('comicsansms', 20)
    bold_font = pygame.font.SysFont('comicsansms', 15, bold=True)
    text = font.render("0", True, RED)
    text_rect = text.get_rect(center=(timer_x + timer_width / 2, timer_y + timer_height / 2))
    section3.blit(text, text_rect)

    # Draw a rectangle with white color as background
    background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20)
    pygame.draw.rect(section3, WHITE, background_rect)

    # Now draw the text
    section3.blit(text, text_rect)

    '''
    # 섹션3 좌측 상단에 "Your turn" 텍스트 생성
    font = pygame.font.SysFont('comicsansms', 20)
    if playerTurn == 0:
        text = font.render("Your turn", True, BLACK)
    else:
        text = font.render("{}'s turn".format(playerTurn), True, BLACK)
    text_rect = text.get_rect(center=(int(section3_width * 0.1), int(section3_height * 0.1)))
    section3.blit(text, text_rect)
    '''
    with open('nickname.json', 'r') as f:
        data = json.load(f)
        nickname = data['nickname']


    # 섹션3 좌측 상단에 "Your turn" 텍스트 생성
    font = pygame.font.SysFont('comicsansms', 20)
    if playerTurn == 0:
        text = font.render("{}' turn".format(nickname), True, BLACK)
    else:
        text = font.render("{}'s turn".format(playerTurn), True, BLACK)

    text_rect = text.get_rect(center=(int(section3_width * 0.1), int(section3_height * 0.1)))

    # Draw a rectangle with white color as background
    background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20,
                                  text_rect.height + 20)  # create a larger rect for the background
    pygame.draw.rect(section3, WHITE, background_rect)  # draw the rect to the section3 surface

    # Now draw the text
    section3.blit(text, text_rect)

    pygame.display.update()

    # "UNO!" 텍스트 생성
    font = pygame.font.SysFont('comicsansms', 20)
    bold_font = pygame.font.SysFont('comicsansms', 15, bold=True)
    text = font.render("UNO!", True, BLACK)
    text_rect = text.get_rect(center=(int(section3_width * 0.23), int(section3_height * 0.1)))
    pygame.draw.rect(section3, RED, (text_rect.x - 5, text_rect.y - 5, text_rect.width + 10, text_rect.height + 10), 3)
    section3.blit(text, text_rect)

    # 색상 변경 사각형 및 텍스트 생성
    colors = ["RED", "YELLOW", "BLUE", "GREEN"]
    color_values = [(255, 0, 0), (255, 255, 0), (0, 0, 255), (0, 255, 0)]
    rects = []
    '''

    for i in range(4):
        rect_x = text_rect.right + 50 + i * 90
        rect_y = text_rect.centery - 25
        rect = pygame.Rect(rect_x, rect_y, 50, 50)
        rects.append(rect)
        pygame.draw.rect(section3, color_values[i], rect)
        color_text = font.render(colors[i], True, BLACK)
        color_text_rect = color_text.get_rect(center=rect.center)
        section3.blit(color_text, color_text_rect)

    pygame.display.update()
    '''

    ##섹션3 우측 중앙에 마지막 한장 남았을때 누르는 버튼 구현
    # UNO_bt = pygame.image.load('./이채은/image/UNO_bt.png')
    # UNO_bt = pygame.transform.scale(UNO_bt, (150,110))
    # section3.blit(UNO_bt, (int(section3_width*0.72), int(section3_height*0.2), 10, 10))

    ##섹션3 우측 중앙에 마지막 한장 남았을때 누르는 버튼 구현
    # UNO_bt = pygame.image.load('./이채은/image/UNO_bt.png')
    # UNO_bt = pygame.transform.scale(UNO_bt, (150,110))
    # section3.blit(UNO_bt, (int(section3_width*0.72), int(section3_height*0.2), 10, 10))


    screen.blit(section1, (0, 0))
    screen.blit(section2, (section1_width, 0))
    screen.blit(section3, (0, section1_height))

    pygame.display.update()

    # 게임 시작할 때
    # 유저 카드 그리기

    selected_card = 0  # 선택된 카드의 인덱스

    user_card = []
    for item in players[0]:
        cards = Card(item, (screen_width, screen_height))
        user_card.append(cards)
    i = 0
    temp_list = []
    for item in user_card:
        # item.update((50 + (screen_width / 10) * i, (screen_height * 0.35) / 2))
        item.update((50 + 50 * i, 500))
        if i == selected_card:  # 선택된 카드에 대한 시각적 표시 (예: 선택된 카드를 약간 위로 올림)
            item.update((50 + 50 * i, 470))
        temp_list.append(item)
        i += 1

    user_group = pygame.sprite.RenderPlain(*temp_list)
    user_group.draw(screen)  # 그리기



    # 백 카드 스프라이트로 시도하기

    backcard = Card('BACK', (screen_width, screen_height))
    backcard.transform(160, 150)
    backcard.update((int(section1_width * 0.20), int(section1_height * 0.45)))
    backcard = pygame.sprite.RenderPlain(backcard)
    backcard.draw(screen)

    # 컴퓨터 카드 그리기
    for j in range(1, numPlayers):
        temp_list = []
        i = 0
        for item in players[j]:  # player_deck 해당 컴퓨터의 카드 리스트
            cards = Card('BACK', (1200, 500))
            cards.transform(30, 40)
            cards.update((810 + 100 / len(players[1]) * i, 105 * j - 50))
            temp_list.append(cards)
            i += 1

        player_group = pygame.sprite.RenderPlain(*temp_list)
        player_group.draw(screen)


    pygame.display.update()


    # top카드 이미지 변화
    back = pygame.image.load('./최회민/img/{}.png'.format(discards[-1]))
    back = pygame.transform.scale(back, (128, 162))
    x = int(screen_width * 0.4)
    y = int(screen_height * 0.4)
    screen.blit(back, (300, 110, 10, 10))
    # section1.blit(back, (300, 110, 10, 10))


    pygame.display.update()

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

            print("top ", discards[-1], "player turn", playerTurn + 1)

            # 이함수 hand넘겨받는기능추가필요
            unoplayer = Computerplay.UnoPlayer(players[playerTurn])
            res = unoplayer.play_card(discards[-1], curruntcolour)

            # 컴퓨터 낼수 없는경우
            if res == None:
                players[playerTurn].extend(drawCards(1))
                # 1장 추가되는거 이미지로 구현
                # 턴 변화
                playerTurn = change_turn(playDirection, numPlayers, playerTurn)
                turn += 1

                # 화면다시 그리기
                screen.blit(section3, (0, section1_height))

                # 플레이어 카드 변화
                for i, item in enumerate(user_group):
                    if i == selected_card:  # 선택된 카드에 대한 시각적 표시 (예: 선택된 카드를 약간 위로 올림)
                        item.update((50 + 50 * i, 470))
                    else:
                        item.update((50 + 50 * i, 500))

                user_group.draw(screen)
                pygame.display.update()

                # 섹션3 좌측 상단에 "Your turn" 텍스트 생성
                font = pygame.font.SysFont('comicsansms', 20)
                if playerTurn == 0:
                    text = font.render("Your turn", True, BLACK)
                else:
                    text = font.render("{}'s turn".format(playerTurn), True, BLACK)

                text_rect = text.get_rect(center=(int(section3_width * 0.1), int(section3_height * 0.1)))

                # Draw a rectangle with white color as background
                background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20,
                                              text_rect.height + 20)  # create a larger rect for the background
                pygame.draw.rect(section3, WHITE, background_rect)  # draw the rect to the section3 surface

                # Now draw the text
                section3.blit(text, text_rect)

                pygame.display.update()

                screen.blit(section1, (0, 0))
                # 백 카드 스프라이트로 시도하기

                backcard = Card('BACK', (screen_width, screen_height))
                backcard.transform(160, 150)
                backcard.update((int(section1_width * 0.20), int(section1_height * 0.45)))
                backcard = pygame.sprite.RenderPlain(backcard)
                backcard.draw(screen)

                # top카드 이미지 변화
                back = pygame.image.load('./최회민/img/{}.png'.format(discards[-1]))
                back = pygame.transform.scale(back, (128, 162))
                x = int(screen_width * 0.4)
                y = int(screen_height * 0.4)
                screen.blit(back, (300, 110, 10, 10))
                # section1.blit(back, (300, 110, 10, 10))
                pygame.display.update()

                # 현재 색 표시 칸 구현
                if curruntcolour == 'BLUE':
                    pygame.draw.circle(section1, BLUE,
                                       (int(section1_width * 0.8), int(section1_height * 0.45)),
                                       int(section1_width * 0.05), 0)
                elif curruntcolour == 'RED':
                    pygame.draw.circle(section1, RED,
                                       (int(section1_width * 0.8), int(section1_height * 0.45)),
                                       int(section1_width * 0.05), 0)
                elif curruntcolour == 'YELLOW':
                    pygame.draw.circle(section1, LIGHT_YELLOW,
                                       (int(section1_width * 0.8), int(section1_height * 0.45)),
                                       int(section1_width * 0.05), 0)
                elif curruntcolour == 'GREEN':
                    pygame.draw.circle(section1, GREEN,
                                       (int(section1_width * 0.8), int(section1_height * 0.45)),
                                       int(section1_width * 0.05), 0)
                # Inside your game loop where you want to draw the text
                len(card)
                font = pygame.font.Font(None, 24)
                card_count_text = str(len(card))  # convert the card count to string
                text_surface = font.render(card_count_text, True, BLACK)  # render the text
                text_rect = text_surface.get_rect(
                    center=(
                        int(section1_width * 0.8), int(section1_height * 0.45)))  # get the rect for positioning
                section1.blit(text_surface, text_rect)  # draw the text to the section1 surface
                pygame.display.update()





                pygame.display.update()




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
                    running = False
                    print("finish")
                    text = font.render("{}'s win! continue : enter".format(playerTurn), True, BLACK)
                    text_rect = text.get_rect(center=(int(screen_width * 0.3), int(screen_height * 0.5)))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    # enter key 누르면 게임 종료
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    return

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
                        curruntcolour = newColour
                    # 리버스면 다음턴 회전반대로
                    if cardVal == "REVERSE":
                        playDirection = playDirection * (-1)
                        if len(players) == 2:
                            playerTurn = change_turn(playDirection, numPlayers, playerTurn)

                    # 스킵하기
                    elif cardVal == "SKIP":
                        playerTurn = change_turn(playDirection, numPlayers, playerTurn)
                    # 2장 뽑기
                    elif splitCard[1] == "DRAW2":
                        playerDraw = next_draw(numPlayers, playDirection, playerTurn)
                        players[playerDraw].extend(drawCards(2))

                        # 플레이어면 유저그룹 변하게
                        if playerDraw == 0:
                            # 화면다시 그리기
                            screen.blit(section3, (0, section1_height))
                            for i in range(2):
                                tmp = Card(players[playerDraw][len(players[playerDraw]) - 2 + i], (800, 600))
                                user_group.add(tmp)
                            # 플레이어 카드 변화
                            for i, item in enumerate(user_group):
                                if i == selected_card:  # 선택된 카드에 대한 시각적 표시 (예: 선택된 카드를 약간 위로 올림)
                                    item.update((50 + 50 * i, 470))
                                else:
                                    item.update((50 + 50 * i, 500))

                            user_group.draw(screen)
                            pygame.display.update()

                    # 어게인
                    elif splitCard[1] == "AGAIN":
                        playDirection = playDirection * (-1)
                        playerTurn = change_turn(playDirection, numPlayers, playerTurn)
                        playDirection = playDirection * (-1)

                        # 색 체인지
                    elif splitCard[1] == "CHANGE":
                        unoplayer = Computerplay.UnoPlayer(players[playerTurn])
                        newColour = unoplayer.choose_color(players[playerTurn])
                        curruntcolour = newColour


                    # 와일드 드로우 4
                    elif splitCard[1] == "DRAW4":

                        playerDraw = next_draw(numPlayers, playDirection, playerTurn)
                        players[playerDraw].extend(drawCards(4))

                        # 플레이어면 유저그룹 변하게
                        if playerDraw == 0:
                            # 화면다시 그리기
                            screen.blit(section3, (0, section1_height))

                            for i in range(4):
                                tmp = Card(players[playerDraw][len(players[playerDraw]) - 4 + i], (800, 600))
                                user_group.add(tmp)
                                # 플레이어 카드 변화
                            # 플레이어 카드 변화
                            for i, item in enumerate(user_group):
                                if i == selected_card:  # 선택된 카드에 대한 시각적 표시 (예: 선택된 카드를 약간 위로 올림)
                                    item.update((50 + 50 * i, 470))
                                else:
                                    item.update((50 + 50 * i, 500))

                            user_group.draw(screen)
                            pygame.display.update()


                    # 컴퓨터 카드변화
                    screen.blit(section2, (section1_width, 0))
                    # 컴퓨터 카드 그리기
                    for j in range(1, numPlayers):
                        temp_list = []
                        i = 0
                        for item in players[j]:  # player_deck 해당 컴퓨터의 카드 리스트
                            cards = Card('BACK', (1200, 500))
                            cards.transform(30, 40)
                            cards.update((810 + 100 / len(players[1]) * i, 105 * j - 50))
                            temp_list.append(cards)
                            i += 1

                        player_group = pygame.sprite.RenderPlain(*temp_list)
                        player_group.draw(screen)
                    pygame.display.update()

                    # 턴 변화
                    playerTurn = change_turn(playDirection, numPlayers, playerTurn)
                    turn += 1



                    # 화면다시 그리기
                    screen.blit(section3, (0, section1_height))

                    # 플레이어 카드 변화
                    for i, item in enumerate(user_group):
                        if i == selected_card:  # 선택된 카드에 대한 시각적 표시 (예: 선택된 카드를 약간 위로 올림)
                            item.update((50 + 50 * i, 470))
                        else:
                            item.update((50 + 50 * i, 500))

                    user_group.draw(screen)
                    pygame.display.update()
                    '''
                    # playerTurn 화면표시

                    font = pygame.font.SysFont('comicsansms', 20)
                    if playerTurn == 0:
                        text = font.render("Your turn", True, BLACK)
                    else:
                        text = font.render("{}'s turn".format(playerTurn), True, BLACK)
                    text_rect = text.get_rect(
                        center=(int(section3_width * 0.1), int(section3_height * 0.1)))
                    section3.blit(text, text_rect)
                    '''
                    # 섹션3 좌측 상단에 "Your turn" 텍스트 생성
                    font = pygame.font.SysFont('comicsansms', 20)
                    if playerTurn == 0:
                        text = font.render("Your turn", True, BLACK)
                    else:
                        text = font.render("{}'s turn".format(playerTurn), True, BLACK)

                    text_rect = text.get_rect(center=(int(section3_width * 0.1), int(section3_height * 0.1)))

                    # Draw a rectangle with white color as background
                    background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20,
                                                  text_rect.height + 20)  # create a larger rect for the background
                    pygame.draw.rect(section3, WHITE, background_rect)  # draw the rect to the section3 surface

                    # Now draw the text
                    section3.blit(text, text_rect)

                    pygame.display.update()




                    pygame.display.update()

                    screen.blit(section1, (0, 0))
                    # 백 카드 스프라이트로 시도하기

                    backcard = Card('BACK', (screen_width, screen_height))
                    backcard.transform(160, 150)
                    backcard.update((int(section1_width * 0.20), int(section1_height * 0.45)))
                    backcard = pygame.sprite.RenderPlain(backcard)
                    backcard.draw(screen)



                    # top카드 이미지 변화
                    back = pygame.image.load('./최회민/img/{}.png'.format(discards[-1]))
                    back = pygame.transform.scale(back, (128, 162))
                    x = int(screen_width * 0.4)
                    y = int(screen_height * 0.4)
                    screen.blit(back, (300, 110, 10, 10))
                    # section1.blit(back, (300, 110, 10, 10))
                    pygame.display.update()

                    # 현재 색 표시 칸 구현
                    if curruntcolour == 'BLUE':
                        pygame.draw.circle(section1, BLUE,
                                           (int(section1_width * 0.8), int(section1_height * 0.45)),
                                           int(section1_width * 0.05), 0)
                    elif curruntcolour == 'RED':
                        pygame.draw.circle(section1, RED,
                                           (int(section1_width * 0.8), int(section1_height * 0.45)),
                                           int(section1_width * 0.05), 0)
                    elif curruntcolour == 'YELLOW':
                        pygame.draw.circle(section1, LIGHT_YELLOW,
                                           (int(section1_width * 0.8), int(section1_height * 0.45)),
                                           int(section1_width * 0.05), 0)
                    elif curruntcolour == 'GREEN':
                        pygame.draw.circle(section1, GREEN,
                                           (int(section1_width * 0.8), int(section1_height * 0.45)),
                                           int(section1_width * 0.05), 0)
                    # Inside your game loop where you want to draw the text
                    print(len(card))
                    font = pygame.font.Font(None, 24)
                    card_count_text = str(len(card))  # convert the card count to string
                    text_surface = font.render(card_count_text, True, BLACK)  # render the text
                    text_rect = text_surface.get_rect(
                        center=(
                        int(section1_width * 0.8), int(section1_height * 0.45)))  # get the rect for positioning
                    section1.blit(text_surface, text_rect)  # draw the text to the section1 surface
                    pygame.display.update()


                    pygame.display.update()

        # 타이머 설정
        time_limit = datetime.timedelta(minutes=2)
        start_time = datetime.datetime.now()
        end_time = start_time + time_limit

        # 타이머 업데이트

        current_time = datetime.datetime.now()
        time_left = end_time - current_time
        if time_left.total_seconds() <= 0:
            text = bold_font.render("Time's up!", True, (255, 0, 0))
        else:
            seconds_left = int(time_left.total_seconds())
            text = font.render(str(seconds_left), True, (0, 0, 0))
        text_rect = text.get_rect(center=(timer_x + timer_width / 2, timer_y + timer_height / 2))
        section3.blit(text, text_rect)

        pygame.display.update()
        '''
        if playerTurn == 0:
            timer(10, font, RED, timer_x, timer_width, timer_y, timer_height, section3, WHITE)
        '''

        # 사람인경우
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:  # 왼쪽 화살표 키가 눌렸을 때
                    selected_card = (selected_card - 1) % len(user_group)
                    # 화면다시 그리기
                    screen.blit(section3, (0, section1_height))
                    # 플레이어 카드 변화
                    for i, item in enumerate(user_group):
                        if i == selected_card:  # 선택된 카드에 대한 시각적 표시 (예: 선택된 카드를 약간 위로 올림)
                            item.update((50 + 50 * i, 470))
                        else:
                            item.update((50 + 50 * i, 500))

                    user_group.draw(screen)
                    pygame.display.update()


                elif event.key == pygame.K_RIGHT:  # 오른쪽 화살표 키가 눌렸을 때
                    selected_card = (selected_card + 1) % len(user_group)
                    # 화면다시 그리기
                    screen.blit(section3, (0, section1_height))


                    # 플레이어 카드 변화
                    for i, item in enumerate(user_group):
                        if i == selected_card:  # 선택된 카드에 대한 시각적 표시 (예: 선택된 카드를 약간 위로 올림)
                            item.update((50 + 50 * i, 470))
                        else:
                            item.update((50 + 50 * i, 500))

                    user_group.draw(screen)
                    pygame.display.update()


                elif event.key == pygame.K_RETURN:  # enter 키가 눌렸을 때
                    if playerTurn == 0:

                        for i, sprite in enumerate(user_group):
                            if i == selected_card:
                                if check_card(curruntcolour, cardVal, sprite):
                                    # 카드 낼때
                                    discards.append(sprite.get_name())
                                    user_group.remove(sprite)  # 핸드에서 내려는 카드를 제거하고
                                    players[playerTurn].remove(sprite.get_name())

                                    if len(players[playerTurn]) == 0:
                                        print("finish")
                                        running = False
                                        winner = playerTurn + 1

                                        achieve.setSingleWin()

                                        if turn <= 10:
                                            achieve.setIn10Turn()
                                        text = font.render("YOU win! continue : enter", True, BLACK)
                                        text_rect = text.get_rect(
                                            center=(int(screen_width * 0.3), int(screen_height * 0.5)))
                                        screen.blit(text, text_rect)
                                        pygame.display.update()
                                        # enter key 누르면 게임 종료
                                        while True:
                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN:
                                                    if event.key == pygame.K_RETURN:
                                                        return
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
                                        curruntcolour = show_color_popup(screen, 500, 100, font, colors, color_values)

                                    # 리버스면 다음턴 회전반대로
                                    if cardVal == "REVERSE":
                                        playDirection = playDirection * (-1)
                                        if len(players) == 2:
                                            playerTurn = change_turn(playDirection, numPlayers, playerTurn)

                                    # 스킵하기
                                    elif cardVal == "SKIP":
                                        playerTurn = change_turn(playDirection, numPlayers, playerTurn)
                                    # 2장 뽑기
                                    elif splitCard[1] == "DRAW2":
                                        playerDraw = next_draw(numPlayers, playDirection, playerTurn)
                                        players[playerDraw].extend(drawCards(2))
                                        # 컴퓨터 카드 변화구현
                                    # 와일드 드로우 4
                                    elif splitCard[1] == "DRAW4":
                                        playerDraw = next_draw(numPlayers, playDirection, playerTurn)
                                        players[playerDraw].extend(drawCards(4))
                                        # 컴퓨터 카드 변화구현

                                    # 색 체인지
                                    elif splitCard[1] == "CHANGE":
                                        curruntcolour = show_color_popup(screen, 500, 100, font, colors, color_values)

                                    # 어게인
                                    elif splitCard[1] == "AGAIN":
                                        playDirection = playDirection * (-1)
                                        playerTurn = change_turn(playDirection, numPlayers, playerTurn)
                                        playDirection = playDirection * (-1)




                                    # 턴 변화
                                    playerTurn = change_turn(playDirection, numPlayers, playerTurn)
                                    turn += 1



                                    screen.blit(section1, (0, 0))
                                    # 백 카드 스프라이트로 시도하기

                                    backcard = Card('BACK', (screen_width, screen_height))
                                    backcard.transform(160, 150)
                                    backcard.update((int(section1_width * 0.20), int(section1_height * 0.45)))
                                    backcard = pygame.sprite.RenderPlain(backcard)
                                    backcard.draw(screen)

                                    # top카드 이미지 변화
                                    back = pygame.image.load('./최회민/img/{}.png'.format(discards[-1]))
                                    back = pygame.transform.scale(back, (128, 162))
                                    x = int(screen_width * 0.4)
                                    y = int(screen_height * 0.4)
                                    screen.blit(back, (300, 110, 10, 10))
                                    # section1.blit(back, (300, 110, 10, 10))
                                    pygame.display.update()

                                    # 현재 색 표시 칸 구현
                                    if curruntcolour == 'BLUE':
                                        pygame.draw.circle(section1, BLUE,
                                                           (int(section1_width * 0.8), int(section1_height * 0.45)),
                                                           int(section1_width * 0.05), 0)
                                    elif curruntcolour == 'RED':
                                        pygame.draw.circle(section1, RED,
                                                           (int(section1_width * 0.8), int(section1_height * 0.45)),
                                                           int(section1_width * 0.05), 0)
                                    elif curruntcolour == 'YELLOW':
                                        pygame.draw.circle(section1, LIGHT_YELLOW,
                                                           (int(section1_width * 0.8), int(section1_height * 0.45)),
                                                           int(section1_width * 0.05), 0)
                                    elif curruntcolour == 'GREEN':
                                        pygame.draw.circle(section1, GREEN,
                                                           (int(section1_width * 0.8), int(section1_height * 0.45)),
                                                           int(section1_width * 0.05), 0)

                                    # Inside your game loop where you want to draw the text
                                    len(card)
                                    font = pygame.font.Font(None, 24)
                                    card_count_text = str(len(card))  # convert the card count to string
                                    text_surface = font.render(card_count_text, True, BLACK)  # render the text
                                    text_rect = text_surface.get_rect(
                                        center=(int(section1_width * 0.8),
                                                int(section1_height * 0.45)))  # get the rect for positioning
                                    section1.blit(text_surface, text_rect)  # draw the text to the section1 surface
                                    pygame.display.update()


                                    pygame.display.update()



                                    # 화면다시 그리기
                                    screen.blit(section3, (0, section1_height))

                                    # 플레이어 카드 변화
                                    for i, item in enumerate(user_group):
                                        if i == selected_card:  # 선택된 카드에 대한 시각적 표시 (예: 선택된 카드를 약간 위로 올림)
                                            item.update((50 + 50 * i, 470))
                                        else:
                                            item.update((50 + 50 * i, 500))

                                    user_group.draw(screen)
                                    pygame.display.update()

                                    break

                                    # 섹션3 좌측 상단에 "Your turn" 텍스트 생성
                                    font = pygame.font.SysFont('comicsansms', 20)
                                    if playerTurn == 0:
                                        text = font.render("Your turn", True, BLACK)
                                    else:
                                        text = font.render("{}'s turn".format(playerTurn), True, BLACK)

                                    text_rect = text.get_rect(
                                        center=(int(section3_width * 0.1), int(section3_height * 0.1)))

                                    # Draw a rectangle with white color as background
                                    background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10,
                                                                  text_rect.width + 20,
                                                                  text_rect.height + 20)  # create a larger rect for the background
                                    pygame.draw.rect(section3, WHITE,
                                                     background_rect)  # draw the rect to the section3 surface

                                    # Now draw the text
                                    section3.blit(text, text_rect)

                                    pygame.display.update()


                                    pygame.display.update()



                                    # 컴퓨터 카드변화
                                    screen.blit(section2, (section1_width, 0))
                                    # 컴퓨터 카드 그리기
                                    for j in range(1, numPlayers):
                                        temp_list = []
                                        i = 0
                                        for item in players[j]:  # player_deck 해당 컴퓨터의 카드 리스트
                                            cards = Card('BACK', (1200, 500))
                                            cards.transform(30, 40)
                                            cards.update((810 + 100 / len(players[1]) * i, 105 * j - 50))
                                            temp_list.append(cards)
                                            i += 1

                                        player_group = pygame.sprite.RenderPlain(*temp_list)
                                        player_group.draw(screen)
                                    pygame.display.update()



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
                    deck = loadcard.Card('BACK', (350, 300))
                    deck_group = pygame.sprite.RenderPlain(deck)
                    # 이건 덱에서 카드 뽑기
                    for sprite in backcard:
                        if sprite.get_rect().collidepoint(mouse_pos):
                            # 카드선택할 수 없으면
                            players[playerTurn].extend(drawCards(1))

                            # 플레이어의 카드 변화
                            item = players[playerTurn][-1]
                            lastcard1 = len(user_group.sprites())
                            temp = Card(item, (800, 600))
                            user_group.add(temp)
                            # 턴 변화
                            playerTurn = change_turn(playDirection, numPlayers, playerTurn)
                            turn += 1


                            # 화면다시 그리기
                            screen.blit(section3, (0, section1_height))
                            # 플레이어 카드 변화
                            for i, item in enumerate(user_group):
                                if i == selected_card:  # 선택된 카드에 대한 시각적 표시 (예: 선택된 카드를 약간 위로 올림)
                                    item.update((50 + 50 * i, 470))
                                else:
                                    item.update((50 + 50 * i, 500))
                            user_group.draw(screen)
                            pygame.display.update()


                            # 섹션3 좌측 상단에 "Your turn" 텍스트 생성
                            font = pygame.font.SysFont('comicsansms', 20)
                            if playerTurn == 0:
                                text = font.render("Your turn", True, BLACK)
                            else:
                                text = font.render("{}'s turn".format(playerTurn), True, BLACK)

                            text_rect = text.get_rect(center=(int(section3_width * 0.1), int(section3_height * 0.1)))

                            # Draw a rectangle with white color as background
                            background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20,
                                                          text_rect.height + 20)  # create a larger rect for the background
                            pygame.draw.rect(section3, WHITE, background_rect)  # draw the rect to the section3 surface

                            # Now draw the text
                            section3.blit(text, text_rect)

                            pygame.display.update()


                            break

                    # 내 카드 선택
                    for sprite in user_group:
                        if sprite.get_rect().collidepoint(mouse_pos):
                            if check_card(curruntcolour, cardVal, sprite):
                                # 카드 낼때
                                discards.append(sprite.get_name())
                                user_group.remove(sprite)  # 핸드에서 내려는 카드를 제거하고
                                players[playerTurn].remove(sprite.get_name())
                                if len(players[playerTurn]) == 0:
                                    print("finish")
                                    running = False
                                    winner = playerTurn + 1
                                    achieve.setSingleWin()
                                    if turn <= 10:
                                        achieve.setIn10Turn()

                                    text = font.render("YOU win! continue : enter", True, BLACK)
                                    text_rect = text.get_rect(
                                        center=(int(screen_width * 0.3), int(screen_height * 0.5)))
                                    screen.blit(text, text_rect)
                                    pygame.display.update()
                                    # enter key 누르면 게임 종료
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_RETURN:
                                                    return

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
                                    curruntcolour = show_color_popup(screen, 500, 100, font, colors, color_values)

                                # 리버스면 다음턴 회전반대로
                                if cardVal == "REVERSE":
                                    playDirection = playDirection * (-1)
                                    if len(players) == 2:
                                        playerTurn = change_turn(playDirection, numPlayers, playerTurn)

                                # 스킵하기
                                elif cardVal == "SKIP":
                                    playerTurn = change_turn(playDirection, numPlayers, playerTurn)
                                # 2장 뽑기
                                elif splitCard[1] == "DRAW2":
                                    playerDraw = next_draw(numPlayers, playDirection, playerTurn)
                                    players[playerDraw].extend(drawCards(2))
                                    # 컴퓨터 카드 변화구현
                                # 와일드 드로우 4
                                elif splitCard[1] == "DRAW4":
                                    playerDraw = next_draw(numPlayers, playDirection, playerTurn)
                                    players[playerDraw].extend(drawCards(4))
                                    # 컴퓨터 카드 변화구현

                                # 색 체인지
                                elif splitCard[1] == "CHANGE":
                                    curruntcolour = show_color_popup(screen, 500, 100, font, colors, color_values)

                                # 어게인
                                elif splitCard[1] == "AGAIN":
                                    playDirection = playDirection * (-1)
                                    playerTurn = change_turn(playDirection, numPlayers, playerTurn)
                                    playDirection = playDirection * (-1)

                                # 턴 변화
                                playerTurn = change_turn(playDirection, numPlayers, playerTurn)
                                turn += 1





                                screen.blit(section1, (0, 0))
                                # 백 카드 스프라이트로 시도하기

                                backcard = Card('BACK', (screen_width, screen_height))
                                backcard.transform(160, 150)
                                backcard.update((int(section1_width * 0.20), int(section1_height * 0.45)))
                                backcard = pygame.sprite.RenderPlain(backcard)
                                backcard.draw(screen)

                                # top카드 이미지 변화
                                back = pygame.image.load('./최회민/img/{}.png'.format(discards[-1]))
                                back = pygame.transform.scale(back, (128, 162))
                                x = int(screen_width * 0.4)
                                y = int(screen_height * 0.4)
                                screen.blit(back, (300, 110, 10, 10))
                                # section1.blit(back, (300, 110, 10, 10))
                                pygame.display.update()

                                # 현재 색 표시 칸 구현
                                if curruntcolour == 'BLUE':
                                    pygame.draw.circle(section1, BLUE,
                                                       (int(section1_width * 0.8), int(section1_height * 0.45)),
                                                       int(section1_width * 0.05), 0)
                                elif curruntcolour == 'RED':
                                    pygame.draw.circle(section1, RED,
                                                       (int(section1_width * 0.8), int(section1_height * 0.45)),
                                                       int(section1_width * 0.05), 0)
                                elif curruntcolour == 'YELLOW':
                                    pygame.draw.circle(section1, LIGHT_YELLOW,
                                                       (int(section1_width * 0.8), int(section1_height * 0.45)),
                                                       int(section1_width * 0.05), 0)
                                elif curruntcolour == 'GREEN':
                                    pygame.draw.circle(section1, GREEN,
                                                       (int(section1_width * 0.8), int(section1_height * 0.45)),
                                                       int(section1_width * 0.05), 0)
                                # Inside your game loop where you want to draw the text
                                len(card)
                                font = pygame.font.Font(None, 24)
                                card_count_text = str(len(card))  # convert the card count to string
                                text_surface = font.render(card_count_text, True, BLACK)  # render the text
                                text_rect = text_surface.get_rect(
                                    center=(int(section1_width * 0.8),
                                            int(section1_height * 0.45)))  # get the rect for positioning
                                section1.blit(text_surface, text_rect)  # draw the text to the section1 surface
                                pygame.display.update()

                                pygame.display.update()

                                # 화면다시 그리기
                                screen.blit(section3, (0, section1_height))

                                # 플레이어 카드 변화
                                for i, item in enumerate(user_group):
                                    if i == selected_card:  # 선택된 카드에 대한 시각적 표시 (예: 선택된 카드를 약간 위로 올림)
                                        item.update((50 + 50 * i, 470))
                                    else:
                                        item.update((50 + 50 * i, 500))

                                user_group.draw(screen)
                                pygame.display.update()

                                # 섹션3 좌측 상단에 "Your turn" 텍스트 생성
                                font = pygame.font.SysFont('comicsansms', 20)
                                if playerTurn == 0:
                                    text = font.render("Your turn", True, BLACK)
                                else:
                                    text = font.render("{}'s turn".format(playerTurn), True, BLACK)

                                text_rect = text.get_rect(
                                    center=(int(section3_width * 0.1), int(section3_height * 0.1)))

                                # Draw a rectangle with white color as background
                                background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10,
                                                              text_rect.width + 20,
                                                              text_rect.height + 20)  # create a larger rect for the background
                                pygame.draw.rect(section3, WHITE,
                                                 background_rect)  # draw the rect to the section3 surface

                                # Now draw the text
                                section3.blit(text, text_rect)

                                pygame.display.update()



                                pygame.display.update()
                                break

                                # 컴퓨터 카드변화
                                screen.blit(section2, (section1_width, 0))
                                # 컴퓨터 카드 그리기
                                for j in range(1, numPlayers):
                                    temp_list = []
                                    i = 0
                                    for item in players[j]:  # player_deck 해당 컴퓨터의 카드 리스트
                                        cards = Card('BACK', (1200, 500))
                                        cards.transform(30, 40)
                                        cards.update((810 + 100 / len(players[1]) * i, 105 * j - 50))
                                        temp_list.append(cards)
                                        i += 1

                                    player_group = pygame.sprite.RenderPlain(*temp_list)
                                    player_group.draw(screen)
                                pygame.display.update()

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
                if splitCard[1] == "REVERSE" or splitCard[1] == "SKIP" or splitCard[1] == "DRAW2" or splitCard[1] == "AGAIN" or splitCard[1] == "CHANGE":
                    score += 20
                else:
                    score += int(splitCard[1])

    # 토탈 점수 계산해 500이상이면 완전끝
    playerscore[playerTurn - 1] += score
    if playerscore[playerTurn - 1] >= 500:
        running = False




