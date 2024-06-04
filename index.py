import pygame 
import random 

pygame.init() 
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock() 
running = True 
 
bg= pygame.image.load("bg.jpg")
fruit = pygame.image.load("fruit2.webp")
fruit = pygame.transform.scale(fruit, (100,100))

fruit_pos = [[640, 0], [100, 0], [1200, 0], [1000,0]]

def fall(fruit_pos ): 
    
    fruit_pos[random.randint(0,3)] += 5 
    if fruit_pos[random.randint(0,3)] > 720:
        fruit_pos[random.randint(0,3)] = 0
    screen.blit(fruit, fruit_pos)

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False 

    screen.fill((255,0,0))
    screen.blit(bg, (0,0))
    fall(fruit_pos)
    pygame.display.flip() 
    clock.tick(60) 
pygame.quit()