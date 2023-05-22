import pygame
import json

class SoundSettingsWindow:
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 600

        self.WHITE = (255, 255, 255)

        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Sound Settings")

        self.button_width = 40
        self.button_height = 40
        self.button_x = 450
        self.button_y = 150

        self.volume_all = 50
        self.volume_1 = 50
        self.volume_2 = 50

        self.load_sound_settings()

        pygame.mixer.music.load('./이채은/sound/배경.mp3')
        self.sound_effect = pygame.mixer.Sound('./이채은/sound/뿅.mp3')

        pygame.mixer.music.set_volume(self.volume_1 / 100)
        self.sound_effect.set_volume(self.volume_2 / 100)

        self.font = pygame.font.Font(None, 30)
        text1 = self.font.render("Text1", True, pygame.Color('black'))
        text2 = self.font.render("Text2", True, pygame.Color('black'))
        text3 = self.font.render("Text3", True, pygame.Color('black'))
        self.texts = [text1, text2, text3]

    def load_sound_settings(self):
        with open('sound_settings.json', 'r') as file:
            sound_settings = json.load(file)

        self.volume_all = sound_settings['volume_all']
        self.volume_1 = sound_settings['volume_1']
        self.volume_2 = sound_settings['volume_2']

    def save_sound_settings(self):
        sound_settings = {
            'volume_all': self.volume_all,
            'volume_1': self.volume_1,
            'volume_2': self.volume_2
        }

        with open('sound_settings.json', 'w') as file:
            json.dump(sound_settings, file)

    def draw_window(self):
        self.window.fill(self.WHITE)

        for i in range(3):
            self.window.blit(self.texts[i], (self.button_x - self.button_width - 30, self.button_y + i * 50 + 10))

        pygame.draw.rect(self.window, pygame.Color('red'), pygame.Rect(self.button_x - self.button_width, self.button_y, self.button_width, self.button_height))
        pygame.draw.rect(self.window, pygame.Color('red'), pygame.Rect(self.button_x + self.button_width, self.button_y, self.button_width, self.button_height))
        text_minus = self.font.render("-", True, pygame.Color('white'))
        text_plus = self.font.render("+", True, pygame.Color('white'))
        self.window.blit(text_minus, (self.button_x - self.button_width + 16, self.button_y + 8))
        self.window.blit(text_plus, (self.button_x + self.button_width + 17, self.button_y + 8))

        pygame.draw.rect(self.window, pygame.Color('red'), pygame.Rect(self.button_x - self.button_width, self.button_y + 50, self.button_width, self.button_height))
        pygame.draw.rect(self.window, pygame.Color('red'), pygame.Rect(self.button_x + self.button_width, self.button_y + 50, self.button_width, self.button_height))
        self.window.blit(text_minus, (self.button_x - self.button_width + 16, self.button_y + 58))
        self.window.blit(text_plus, (self.button_x + self.button_width + 17, self.button_y + 58))

        pygame.draw.rect(self.window, pygame.Color('red'), pygame.Rect(self.button_x - self.button_width, self.button_y + 100, self.button_width, self.button_height))
        pygame.draw.rect(self.window, pygame.Color('red'), pygame.Rect(self.button_x + self.button_width, self.button_y + 100, self.button_width, self.button_height))
        self.window.blit(text_minus, (self.button_x - self.button_width + 16, self.button_y + 108))
        self.window.blit(text_plus, (self.button_x + self.button_width + 17, self.button_y + 108))

        text_volume_all = self.font.render(str(self.volume_all), True, pygame.Color('black'))
        text_volume_1 = self.font.render(str(self.volume_1), True, pygame.Color('black'))
        text_volume_2 = self.font.render(str(self.volume_2), True, pygame.Color('black'))
        self.window.blit(text_volume_all, (self.button_x - self.button_width + 52, self.button_y + 10))
        self.window.blit(text_volume_1, (self.button_x - self.button_width + 52, self.button_y + 60))
        self.window.blit(text_volume_2, (self.button_x - self.button_width + 52, self.button_y + 110))

        pygame.draw.rect(self.window, pygame.Color('gray'), pygame.Rect(290, 350, 100, 50))
        pygame.draw.rect(self.window, pygame.Color('gray'), pygame.Rect(440, 350, 100, 50))
        text_save = self.font.render("Save", True, pygame.Color('black'))
        text_back = self.font.render("Back", True, pygame.Color('black'))
        self.window.blit(text_save, (315, 365))
        self.window.blit(text_back, (465, 365))

        pygame.display.update()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(290, 350, 100, 50).collidepoint(event.pos):
                        self.save_sound_settings()
                    elif pygame.Rect(440, 350, 100, 50).collidepoint(event.pos):
                        running = False
                    elif pygame.Rect(self.button_x - self.button_width, self.button_y, self.button_width, self.button_height).collidepoint(event.pos):
                        self.volume_all -= 10
                        self.volume_all = max(0, self.volume_all)
                        self.volume_1 = self.volume_all
                        self.volume_2 = self.volume_all
                    elif pygame.Rect(self.button_x + self.button_width, self.button_y, self.button_width, self.button_height).collidepoint(event.pos):
                        self.volume_all += 10
                        self.volume_all = min(100, self.volume_all)
                        self.volume_1 = self.volume_all
                        self.volume_2 = self.volume_all
                    elif pygame.Rect(self.button_x - self.button_width, self.button_y + 50, self.button_width, self.button_height).collidepoint(event.pos):
                        self.volume_1 -= 10
                        self.volume_1 = max(0, self.volume_1)
                    elif pygame.Rect(self.button_x + self.button_width, self.button_y + 50, self.button_width, self.button_height).collidepoint(event.pos):
                        self.volume_1 += 10
                        self.volume_1 = min(100, self.volume_1)
                    elif pygame.Rect(self.button_x - self.button_width, self.button_y + 100, self.button_width, self.button_height).collidepoint(event.pos):
                        self.volume_2 -= 10
                        self.volume_2 = max(0, self.volume_2)
                    elif pygame.Rect(self.button_x + self.button_width, self.button_y + 100, self.button_width, self.button_height).collidepoint(event.pos):
                        self.volume_2 += 10
                        self.volume_2 = min(100, self.volume_2)

            self.draw_window()

    pygame.quit()
