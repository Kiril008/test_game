import pygame
import random


pygame.init()


WIDTH = 600
HEIGHT = 600


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


CUBE_SIZE = 50
OBSTACLE_WIDTH = 100
OBSTACLE_HEIGHT = 20


start_x = WIDTH // 2 - CUBE_SIZE // 2
start_y = HEIGHT - CUBE_SIZE - OBSTACLE_HEIGHT


obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
obstacle_y = HEIGHT - OBSTACLE_HEIGHT


cube_speed = 5
obstacle_speed = 3


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гра з кубиком")

clock = pygame.time.Clock()

def draw_cube(x, y):
    pygame.draw.rect(window, RED, (x, y, CUBE_SIZE, CUBE_SIZE))

def draw_obstacle(x, y):
    pygame.draw.rect(window, BLACK, (x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

def check_collision(cube_x, cube_y, obstacle_x, obstacle_y):
    if cube_y + CUBE_SIZE >= obstacle_y and cube_y <= obstacle_y + OBSTACLE_HEIGHT:
        if cube_x + CUBE_SIZE >= obstacle_x and cube_x <= obstacle_x + OBSTACLE_WIDTH:
            return True
    return False

def game_loop():
    cube_x = start_x
    cube_y = start_y

    obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
    obstacle_y = HEIGHT - OBSTACLE_HEIGHT

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cube_y -= CUBE_SIZE * 2

        cube_y += cube_speed
        obstacle_x -= obstacle_speed

        window.fill(WHITE)

        draw_cube(cube_x, cube_y)
        draw_obstacle(obstacle_x, obstacle_y)

        if cube_y <= 0 or cube_y + CUBE_SIZE >= HEIGHT or check_collision(cube_x, cube_y, obstacle_x, obstacle_y):
            game_over = True

        if obstacle_x + OBSTACLE_WIDTH < 0:
            obstacle_x = WIDTH
            obstacle_y = HEIGHT - OBSTACLE_HEIGHT

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

game_loop()