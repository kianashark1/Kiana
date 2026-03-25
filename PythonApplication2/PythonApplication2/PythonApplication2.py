import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (200, 50, 100)
BLUE = (0, 100, 170)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
         player_pos[0] -= 12  # Increased speed from 5 to 7
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 12  # Increased speed from 5 to 7

    player_pos[0] = max(0, min(WIDTH - player_size, player_pos[0]))

    enemy_pos[1] += enemy_speed

    if enemy_pos[1] > HEIGHT:
        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
        score += 1
        print(f"Score: {score}")

        player_size += 4 
        enemy_speed += 1 
    if (enemy_pos[0] < player_pos[0] < enemy_pos[0] + enemy_size or enemy_pos[0] < player_pos[0] + player_size < enemy_pos[0] + enemy_size) and \
       (enemy_pos[1] < player_pos[1] < enemy_pos[1] + enemy_size or enemy_pos[1] < player_pos[1] + player_size < enemy_pos[1] + enemy_size):
        print("Game Over!")
        game_over = True

    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()



