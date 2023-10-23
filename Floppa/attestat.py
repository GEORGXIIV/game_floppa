import time

import pygame
import pygame as pg
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

size = 800, 600
width, height = size
GREEN = (150, 255, 150)
RED = (255, 0, 0)
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(size)
background = pygame.image.load('8194_oasis-landscape-green_800x600.jpg')
pygame.display.set_caption("Big Russian Floppa")
s = pg.mixer.Sound('hihihiha.mp3')
s2 = pg.mixer.Sound('I Sawed the Demons.mp3')
s3 = pg.mixer.Sound('povezlo.mp3')
flag = True
running = True
player_sprite = pygame.image.load('5843-floppa-awake.png')
player_sprite = pygame.transform.rotozoom(player_sprite, 0, 0.5)
player_rect = player_sprite.get_rect()
player_rect.center = 0 + player_rect.size[0] / 2, size[1] // 2
speed = [0, 9]


cactus = pygame.image.load('3953-floppa-holding-gun2.png')
cactus = pygame.transform.rotozoom(cactus, 0, 0.5)
cactus_rect = cactus.get_rect()
cactus_rect.left = size[0]
cactus_rect.bottom = size[1] - 100
cactus_speed = [-10, 0]


floppa = pygame.image.load('8173-floppawithglasses.png')
floppa = pygame.transform.rotozoom(floppa, 0, 0.5)
floppa_rect = floppa.get_rect()
floppa_rect.left = size[0]
floppa_rect.bottom = size[1] - 100
floppa_speed = [-3, -0]

timer = pygame.time.Clock()
is_jump = False
score = 0
score_font = pygame.font.SysFont('arial', 36)
score_text = score_font.render(f'Ну типа счёт = {score}', True, (180, 0, 0))
lose_text = score_font.render('', True, (180, 0, 0))

BG = 52,78,91
font = pygame.font.SysFont('arialblack',30)
TEXT_COLOR = 255,255,255

class Button:
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.clicked = False

    def draw(self,screen):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0]==False:
                self.clicked = False

        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action


def draw_text(text,font,text_color,x,y):
    surface = font.render(text,True,text_color)
    screen.blit(surface,(x,y))

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

resume_img = pygame.image.load('buttons/button_resume.png')
options_img = pygame.image.load('buttons/button_options.png')
quit_img = pygame.image.load('buttons/button_quit.png')
video_img = pygame.image.load('buttons/button_video.png')
audio_img = pygame.image.load('buttons/button_audio.png')
keys_img = pygame.image.load('buttons/button_keys.png')
back_img = pygame.image.load('buttons/button_back.png')

resume_button = Button(304,125,resume_img)
options_button = Button(297,250,options_img)
quit_button = Button(336,375,quit_img)

video_button = Button(226,75,video_img)
audio_button = Button(225,200,audio_img)
keys_button = Button(246,325,keys_img)
back_button = Button(332,450,back_img)


game_pause = False
menu_state = 'main'
running = True
game_running = True
while running:
    while game_running:
        timer.tick(60)
        pygame.display.set_caption("Big Russian Floppa")
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                is_jump = True
        keys = pygame.key.get_pressed()
        if keys[K_SPACE] and is_jump == False:
            player_rect.y -= 20
        screen.blit(background, (0, 0))
        screen.blit(player_sprite, player_rect)
        screen.blit(cactus, cactus_rect)
        screen.blit(floppa, floppa_rect)
        floppa_rect = floppa_rect.move(floppa_speed)
        cactus_rect = cactus_rect.move(cactus_speed)
        player_rect = player_rect.move(speed)
        if player_rect.bottom > size[1] - 100:
            player_rect.bottom = size[1] - 100
            is_jump = False
        if cactus_rect.left < 0:
            cactus_rect.right = size[0]
            score_text = score_font.render(f'Ну типа счёт = {score}', True, (180, 0, 0))
        if floppa_rect.left < 0:
            floppa_rect.right = size[0]
            score_text = score_font.render(f'Ну типа счёт = {score}', True, (180, 0, 0))
        if player_rect.colliderect(cactus_rect):
            score -= 1
            s.play()
        if player_rect.colliderect(floppa_rect):
            floppa_rect.right = size[0]
            score += 2
            score_text = score_font.render(f'Ну типа счёт = {score}', True, (180, 0, 0))
            s3.play()
        screen.blit(lose_text, (size[0] / 2, size[1] / 2))
        screen.blit(score_text, (10, 20))
        pygame.display.update()

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False

    pygame.display.set_caption('Менюха(вежливо и абсолютно культурно позаимствованная каперским путём)')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_pause = True

    screen.fill(BG)
    if game_pause==True:
        if menu_state == 'main':
            if resume_button.draw(screen) == True:
                game_pause = False
                game_running = True

            elif options_button.draw(screen) == True:
                menu_state = 'options'

            elif quit_button.draw(screen) == True:
                running = False

        elif menu_state == 'options':
            if audio_button.draw(screen):
                if flag is True:
                    s2.play()
                    flag = False
                elif flag is False:
                    s2.stop()
                    flag = True
            if back_button.draw(screen):
                menu_state = 'main'
    else:
        draw_text('Повторно нажмите esc', font, TEXT_COLOR, 160, 250)
    pygame.display.update()
pygame.quit()