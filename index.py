import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

bg = pygame.image.load("bg.jpg")
fruit = pygame.image.load("fruit2.webp")
fruit2 = pygame.image.load("loot.jpg")
basket = pygame.image.load("basket.webp")
basket = pygame.transform.scale(basket, (100,100))
fruit = pygame.transform.scale(fruit, (100, 100))
fruit2 = pygame.transform.scale(fruit2, (100, 100))

# Initialize fruit positions with random x values
fruit_positions = [[fruit, random.randint(0, 1180), 0], [fruit2, random.randint(0, 1180), 0],
                   [fruit, random.randint(0, 1180), 0], [fruit2, random.randint(0, 1180), 0]]

basket_position = [0,720]


def fall(fruit_positions):
    for i, (fruit, x, y) in enumerate(fruit_positions):
        y += 5  # Increase the y position to make the fruit fall
        if y > 720:
            y = 0  # Reset to top once it goes off the screen
            x = random.randint(0, 1180)  # Randomize the x position
        screen.blit(fruit, (x, y))
        # Update the position in the list
        fruit_positions[i] = [fruit, x, y]

def basket(basket_position):
    

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.K_LEFT:
            basket_position[0] += 5
        if e.type == pygame.K_RIGHT:
            basket_position[0] += 5

    screen.fill((255, 0, 0))  # Fill screen with red using RGB values
    screen.blit(bg, (0, 0))
    basket(basket_position)
    fall(fruit_positions)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
