import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 30
PACMAN_SIZE = 30
GHOST_SIZE = 30
COIN_SIZE = 15
FPS = 30

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Initialize game variables
pacman_pos = [WIDTH // 2, HEIGHT // 2]
ghost_pos = [random.randrange(0, WIDTH - GHOST_SIZE), random.randrange(0, HEIGHT - GHOST_SIZE)]
coin_pos = [random.randrange(0, WIDTH - COIN_SIZE), random.randrange(0, HEIGHT - COIN_SIZE)]

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Game")
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pacman_pos[0] > 0:
        pacman_pos[0] -= 5
    if keys[pygame.K_RIGHT] and pacman_pos[0] < WIDTH - PACMAN_SIZE:
        pacman_pos[0] += 5
    if keys[pygame.K_UP] and pacman_pos[1] > 0:
        pacman_pos[1] -= 5
    if keys[pygame.K_DOWN] and pacman_pos[1] < HEIGHT - PACMAN_SIZE:
        pacman_pos[1] += 5

    # Check for collisions
    if pygame.Rect(pacman_pos, (PACMAN_SIZE, PACMAN_SIZE)).colliderect(
        pygame.Rect(ghost_pos, (GHOST_SIZE, GHOST_SIZE))
    ):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    if pygame.Rect(pacman_pos, (PACMAN_SIZE, PACMAN_SIZE)).colliderect(
        pygame.Rect(coin_pos, (COIN_SIZE, COIN_SIZE))
    ):
        print("Congratulations! You collected the coin!")
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, YELLOW, pacman_pos, PACMAN_SIZE // 2)
    pygame.draw.rect(screen, RED, pygame.Rect(ghost_pos, (GHOST_SIZE, GHOST_SIZE)))
    pygame.draw.circle(screen, WHITE, coin_pos, COIN_SIZE // 2)

    pygame.display.flip()
    clock.tick(FPS)
