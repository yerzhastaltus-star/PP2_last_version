import pygame
from ball import x_move, y_move
pygame.init()
WIDTH, HEIGHT = 800,600
radius = 25
speed = 20
x, y = 800//2, 600//2
red = (255, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= speed
                y = y_move(y, HEIGHT, radius, speed, "up")
            if event.key == pygame.K_DOWN:
                y += speed
                y = y_move(y, HEIGHT, radius, speed, "down")
            if event.key == pygame.K_LEFT:
                x -= speed
                x = x_move(x, WIDTH, radius, speed, "left")
            if event.key == pygame.K_RIGHT:
                x += speed
                x = x_move(x, WIDTH, radius, speed, "right")
    
    screen.fill((255,255,255))
    pygame.draw.circle(screen, red, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
        