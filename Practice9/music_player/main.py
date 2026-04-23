import pygame
from player import MusicPlayer

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 48)

player = MusicPlayer()
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)

    screen.fill((0, 0, 0))  # чёрный фон

    # 🎵 текст Now Playing
    text = font.render(
        f"Now Playing: Track {player.current + 1}",
        True,
        (255, 255, 255)
    )
    screen.blit(text, (120, 180))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next()

            elif event.key == pygame.K_b:
                player.prev()

            elif event.key == pygame.K_SPACE:
                player.pause()

    pygame.display.flip()

pygame.quit()