import pygame
from clock import time_angle

pygame.init()
WIDTH, HEIGHT = 800,600
center = (WIDTH//2, HEIGHT//2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
main = pygame.image.load("images/clock.png")
left = pygame.image.load("images/sec_hand.png")
right = pygame.image.load("images/min_hand.png")
running = True
x = time_angle()
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x.update()
    screen.blit(main, (0,0))
    pygame.draw.circle(screen, (200,100,200), center, 10)
    rotated_left_hand = pygame.transform.rotate(left, -x.s_angle)
    rotated_rigth_hand = pygame.transform.rotate(right, -x.m_angle)
    rect_l = rotated_left_hand.get_rect(center = center)
    rect_r = rotated_rigth_hand.get_rect(center = center)
    screen.blit(rotated_left_hand, rect_l)
    screen.blit(rotated_rigth_hand, rect_r)
    pygame.display.flip()
    clock.tick(60)