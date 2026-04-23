import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Размер блока
block_size = 20

# Змейка
snake = [(100, 100)]
direction = (block_size, 0)

# Еда
def spawn_food():
    while True:
        x = random.randrange(0, WIDTH, block_size)
        y = random.randrange(0, HEIGHT, block_size)
        if (x, y) not in snake:
            return (x, y)

food = spawn_food()

# Счёт и уровень
score = 0
level = 1
speed = 10

font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Управление
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -block_size)
            if event.key == pygame.K_DOWN:
                direction = (0, block_size)
            if event.key == pygame.K_LEFT:
                direction = (-block_size, 0)
            if event.key == pygame.K_RIGHT:
                direction = (block_size, 0)

    # Новая голова
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    new_head = (head_x, head_y)

    # Проверка выхода за границы
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over (wall)")
        running = False

    # Проверка на саму себя
    if new_head in snake:
        print("Game Over (self)")
        running = False

    snake.insert(0, new_head)

    # Проверка еды
    if new_head == food:
        score += 1
        food = spawn_food()

        # Повышение уровня каждые 3 очка
        if score % 3 == 0:
            level += 1
            speed += 2  # увеличение скорости

    else:
        snake.pop()

    # Рисуем змейку
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, block_size, block_size))

    # Рисуем еду
    pygame.draw.rect(screen, RED, (*food, block_size, block_size))

    # Текст (счёт и уровень)
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()