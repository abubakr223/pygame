import pygame

pygame.init()

screen =pygame.display.set_mode((800, 600))

pygame.display.set_caption("abubakrs game")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('spaceship.png')
playerX = 370 
playerY = 480
def player():
    screen.blit(playerImg,(playerX,playerY))



running = True
while running:

    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    player()
    pygame.display.update()        


