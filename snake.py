import pygame
import time
import random
import math


pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
#pygame.display.flip()
pygame.display.set_caption('Snake game by Deon Choi')

clock = pygame.time.Clock()


snake_width = 10
snake_height = 10

game_over_font = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 40)

def show_score(score):
    msg = score_font.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(msg, (0, 0))

def draw_snake(snake_body):
    for snake in snake_body:
        pygame.draw.rect(screen, (255, 255, 255), (snake[0], snake[1], snake_width, snake_height))

def message(msg, color):
    msg = game_over_font.render(msg, True, color)
    screen.blit(msg, (15, 100))

def game_loop():
    game_over = False
    screen_close = False
    x = screen_width // 2
    y = screen_height // 2

    x_delta = 0
    y_delta = 0

    snake_body = []
    snake_length = 1

    speed = 10

    food_x = int(math.ceil(round(random.randrange(0, screen_width - snake_width) / 10.0))) * 10
    food_y = int(math.ceil(round(random.randrange(0, screen_height - snake_height) / 10.0))) * 10

    while not game_over:

        while screen_close:
            screen.fill((0, 0, 0))
            message('Game Over! Press P to play again or Q to quit.', (255, 0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game_loop()
                    if event.key == pygame.K_q:
                        game_over = True
                        screen_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #x -= speed
                    x_delta = -snake_width
                    y_delta = 0
                elif event.key == pygame.K_RIGHT:
                    #x += speed
                    x_delta = snake_width
                    y_delta = 0
                elif event.key == pygame.K_UP:
                    #y -= speed
                    y_delta = -snake_height
                    x_delta = 0
                elif event.key == pygame.K_DOWN:
                    #y += speed
                    y_delta = snake_height
                    x_delta = 0
        
        
        
        if x > screen_width or x <0 or y > screen_height or y < 0:
            screen_close = True
        
        x += x_delta
        y += y_delta

        screen.fill((0, 0, 0))
        #drawing food
        pygame.draw.rect(screen, (0, 0, 255), (food_x, food_y, snake_width, snake_height))
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]
        
        for snake in snake_body[:-1]:
            if snake == snake_head:
                screen_close = False
        
        draw_snake(snake_body)
        show_score(snake_length - 1)
        # drawing snake
        #pygame.draw.rect(screen, (255, 255, 255), (x, y, snake_width, snake_height))
        
        pygame.display.flip()

        if x == food_x and y == food_y:
            food_x = int(math.ceil(round(random.randrange(0, screen_width - snake_width) / 10.0))) * 10
            food_y = int(math.ceil(round(random.randrange(0, screen_height - snake_height) / 10.0))) * 10
            snake_length += 1
            speed += 5

    #message('Game Over!', (255, 0, 0))
    #pygame.display.flip()
    #time.sleep(3)
        clock.tick(speed)
    
    pygame.quit()
    quit()

game_loop()