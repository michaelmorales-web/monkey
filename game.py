import pygame
import random
import time
from assets.src.classes import banana, player, puntaje, vidas

pygame.init()

lost = pygame.mixer.Sound("assets/sounds/PERDER.wav")
coin = pygame.mixer.Sound("assets/sounds/COMIDA.wav")
bg = pygame.image.load("assets/images/FONDO.jpg")
screen = pygame.display.set_mode((1024, 800))
blanco = (255, 255, 255)
clock = pygame.time.Clock()

# Crear instancias de las clases
banana_obj = banana()
player_obj = player()
puntaje_obj = puntaje
vidas_obj = vidas


while True:
    clock.tick(30)  # 30 FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg, (0, 0))
    
    # Llamar a los movimientos
    banana_obj.move()
    player_obj.move(None)
    
    # Actualizar rect del jugador con su nueva posición x
    player_obj.rect.x = player_obj.x
    
    screen.blit(banana_obj.sp_banana, (banana_obj.x, banana_obj.y))
    screen.blit(player_obj.sp_player, (player_obj.x, player_obj.rect.y))
    fuente = pygame.font.SysFont("comic sans ms", 35, 1, 1)
    texto1 = fuente.render("puntos: " + str(puntaje_obj.score), 1, blanco)
    texto2 = fuente.render("vidas: " + str(vidas_obj.lives), 1, blanco)
    screen.blit(texto1, (50, 50))
    screen.blit(texto2, (50, 100))

    if player_obj.rect.colliderect(banana_obj.rect):
        coin.play()
        puntaje_obj.score += 1
        banana_obj.rect.x = random.randint(0, 750)
        banana_obj.rect.y = random.randint(0, 0)
        banana_obj.x = banana_obj.rect.x
        banana_obj.y = banana_obj.rect.y

    if player_obj.rect.colliderect(vidas_obj.rect):
        lost.play()
        vidas_obj.lives -= 1
        vidas_obj.rect.x = random.randint(0, 750)
        vidas_obj.rect.y = random.randint(0, 550)

    if vidas_obj.lives <= 0:
        lost.play()
        time.sleep(7)
        print("Game Over")
        pygame.quit()
        exit()
    
    if banana_obj.rect.y > 800:
        banana_obj.delete()
        banana_obj.rect.x = random.randint(0, 750)
        banana_obj.rect.y = random.randint(0, 0)
        banana_obj.x = banana_obj.rect.x
        banana_obj.y = banana_obj.rect.y

    pygame.display.flip()