import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# загружаем изображения
car_img = pygame.image.load("resources/carrr.png")
road_img = pygame.image.load("resources/road.png")
coin_img = pygame.image.load("resources/coin1.png")

# изменяем размер изображений
car_img = pygame.transform.scale(car_img, (50, 80))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))
coin_img = pygame.transform.scale(coin_img, (20, 20))

# начальная позиция машины
car_x = WIDTH // 2 - 25
car_y = HEIGHT - 100
car_speed = 5

# список монет
coins = []
coin_spawn_timer = 0

# счёт
score = 0
font = pygame.font.SysFont(None, 30)

running = True
while running:

    # рисуем фон
    screen.blit(road_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # управление машиной
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # ограничение движения по экрану
    if car_x < 0:
        car_x = 0
    if car_x > WIDTH - 50:
        car_x = WIDTH - 50

    # создаём монеты через время
    coin_spawn_timer += 1
    if coin_spawn_timer > 60:
        coin_x = random.randint(20, WIDTH - 20)
        coins.append([coin_x, 0])
        coin_spawn_timer = 0

    # двигаем монеты вниз
    for coin in coins:
        coin[1] += 5

    # проверяем сбор монет
    for coin in coins[:]:
        if (car_x < coin[0] < car_x + 50) and (car_y < coin[1] < car_y + 80):
            coins.remove(coin)
            score += 1

    # удаляем монеты за экраном
    coins = [coin for coin in coins if coin[1] < HEIGHT]

    # рисуем машину
    screen.blit(car_img, (car_x, car_y))

    # рисуем монеты
    for coin in coins:
        screen.blit(coin_img, (coin[0], coin[1]))

    # выводим счёт
    score_text = font.render(f"Coins: {score}", True, (0, 0, 0))
    screen.blit(score_text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()