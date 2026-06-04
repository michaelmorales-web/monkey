import random
import pygame

pygame.init()

class puntaje:
    def __init__(self):
        self.score = 0

class vidas:
    def __init__(self):
        self.lives = 3
        self.rect = pygame.Rect(0, 0, 50, 50)

puntaje = puntaje()
vidas = vidas()


class banana(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sp_banana = pygame.image.load('assets/images/banana.png')
        self.image = self.sp_banana
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = 0
        self.x = self.rect.x
        self.y = self.rect.y
    
    def move(self):
        self.rect.y += 15
        self.y = self.rect.y
    
    def delete(self):
        global vidas
        vidas.lives -= 1
        self.kill()


class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 550
        self.sp_player = pygame.image.load('assets/images/mono.png')
        self.image = self.sp_player
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, 600)
    
    def move(self, direction):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > 0:
            self.x -= 17
        elif keys[pygame.K_d] and self.x < 750:
            self.x += 17
    
    def comer(self, banana):
        if self.sprite.collide_rect(self, banana):
            global puntaje
            puntaje += 1
            banana.kill()
            pygame.mixer.Sound('assets/sounds/coin.mp3').play()