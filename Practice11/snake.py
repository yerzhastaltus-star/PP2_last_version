import pygame
import random
import sys

pygame.init()

# Set up screen size and colors for the game

WIDTH = 600
HEIGHT = 600

colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 36)
image_game_over = font.render("Game Over", True, colorRED)
image_game_over_rect = image_game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))
sc_rect = image_game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 30))
CELL = 30


def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
                if j!=0:
                        pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)


def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // CELL):
        if i != 0:
            for j in range(WIDTH // CELL):
                pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.score = 0
        self.level = 1 
        self.alive = True

    # Move snake body and check border collisions
    def move(self):
        # Shift body segments to follow the head
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
            

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # checks the right border
        if self.body[0].x > WIDTH // CELL - 1:
            print("Snake is out of the border! r")
            self.alive = False
        # checks the left border
        if self.body[0].x < 0:
            print("Snake is out of the border! l")
            self.alive = False
        # checks the bottom border
        if self.body[0].y > HEIGHT // CELL - 1:
            print("Snake is out of the border! b")
            self.alive = False
        # checks the top border
        if self.body[0].y == 0:
            print("Snake is out of the border! t")
            self.alive = False


    # Draw snake head and body on the screen
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorBLACK, (head.x * CELL, head.y * CELL, CELL, CELL))
    
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    # Check if snake eats food and update score/level
    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.score += food.value
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self.body)
            self.level = 1 + self.score//3

class Food:
    # Initialize food with random value and timer
    def __init__(self):
        self.pos = Point(9, 9) 
        r=random.random()
        if r<0.7:
            self.value=1
        elif r<0.9:
            self.value=3
        else:
            self.value=5
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 5000  # 5 seconds     

    # Draw food with different colors depending on value
    def draw(self):
        if self.value == 1:
            color = colorGREEN
        elif self.value == 3:
            color = (255, 140, 0)
        else:
            color = colorYELLOW

        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    # Generate new position for food (not on snake)
    def generate_random_pos(self, snake_body):
        while True:
            # regenerate food value each time it appears
            r = random.random()
            if r < 0.7:
                self.value = 1
            elif r < 0.9:
                self.value = 3
            else:
                self.value = 5
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            self.spawn_time = pygame.time.get_ticks()
            if not any(self.pos.x == s.x and self.pos.y == s.y for s in snake_body) and self.pos.y > 0:
                break



FPS = 5
clock = pygame.time.Clock()
food = Food()
snake = Snake()
food.generate_random_pos(snake.body)

# Main game loop starts here
running = True
game_over = False
while running:
   
    score = snake.score
    level = snake.level
    points_to_next = 3 - (score % 3)

    sc = font.render(f'Score: {score}', True, colorBLUE)
    lv = font.render(f'Level: {level}', True, colorBLUE)  
    if points_to_next == 1:
        txt = f'Next level in {points_to_next} point'
    else:
        txt = f'Next level in {points_to_next} points'
    
    nx = font.render(txt, True, colorRED) 

    # Handle user input (keyboard and window events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # quit anytime
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

            # restart only when game over
            if game_over and event.key == pygame.K_r:
                food = Food()
                snake = Snake()
                food.generate_random_pos(snake.body)
                game_over = False
                continue

            # movement only if alive
            if not game_over:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                elif event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                elif event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1
                elif event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1

    # If snake dies, show Game Over screen
    if not snake.alive:
        game_over = True
        stra = f"""Score: {score} 
Level: {level}"""
        sc_r = font.render(stra, True, colorRED)
        screen.fill(colorBLACK)
        screen.blit(image_game_over, image_game_over_rect)
        screen.blit(sc_r, sc_rect)
        pygame.display.flip()
        clock.tick(5)
        continue

    # Check if food lifetime expired and respawn
    current_time = pygame.time.get_ticks()
    if current_time - food.spawn_time > food.lifetime:
        food.generate_random_pos(snake.body)

    # Draw game elements (grid, snake, food, UI)
    if not game_over:
        screen.fill(colorWHITE)
        draw_grid()
        snake.move()
        snake.check_collision(food)
        snake.draw()

    if not game_over:
        food.draw()
        screen.blit(sc, (2, 0))
        screen.blit(lv, (120, 0))
        screen.blit(nx, (250, 0))
    pygame.display.flip()
    clock.tick(FPS + level)

pygame.quit()

'''
#
# # #

-----

#
#
# #

-----

#
#
#
#

'''