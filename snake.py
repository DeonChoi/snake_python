import pygame
import time
import random
import math



screen_width = 500
screen_height = 500

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.flip()
pygame.display.set_caption('Snake game by Deon Choi')


speed = 10
snake_width = 10
snake_height = 10

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    msg = font_style.render(msg, True, color)
    screen.blit(msg, (screen_width//2, screen_height//2))

def game_loop():
    game_over = False
    x = screen_width // 2
    y = screen_height // 2

    food_x = int(math.ceil(round(random.randrange(0, screen_width - snake_width) / 10.0))) * 10
    print(food_x)
    food_y = int(math.ceil(round(random.randrange(0, screen_height - snake_height) / 10.0))) * 10
    print(food_y)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= speed
                elif event.key == pygame.K_RIGHT:
                    x += speed
                elif event.key == pygame.K_UP:
                    y -= speed
                elif event.key == pygame.K_DOWN:
                    y += speed
        
        if x > screen_width or x <0 or y > screen_height or y < 0:
            game_over = True

        screen.fill((0, 0, 0))
        # drawing snake
        pygame.draw.rect(screen, (255, 255, 255), (x, y, snake_width, snake_height))
        # drawing food
        pygame.draw.rect(screen, (0, 0, 255), (food_x, food_y, snake_width, snake_height))
        pygame.display.flip()

        if x == food_x and y == food_y:
            print("Tastes Great!")

    message('Game Over!', (255, 0, 0))
    pygame.display.flip()
    time.sleep(2)

    pygame.quit()
    quit()

game_loop()