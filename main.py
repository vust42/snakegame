import pygame
import random
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BLOCK_SIZE = 20
SPEED = 15
WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

from config import Settings, GameRules

screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
snake_speed = Settings.GAME_SPEED

def show_score(score):
    font = pygame.font.SysFont('comicsansms', 35)
    value = font.render(f"Счет: {score}", True, WHITE)
    screen.blit(value, [10, 10])

def show_message(msg, color, y_offset=0):
    font = pygame.font.SysFont('comicsansms', 35)
    lines = msg.split('\n')
    for i, line in enumerate(lines):
        text = font.render(line, True, color)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 + y_offset + i*40))
        screen.blit(text, text_rect)

def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH // 2
    y1 = HEIGHT // 2
    
    x1_change = 0
    y1_change = 0
    
    snake_body = []
    length_of_snake = 1
    
    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    
    while not game_over:
        
        while game_close:
            screen.fill(BLACK)
            show_message("Вы проиграли!\nНажмите Q чтобы выйти\nили C чтобы сыграть снова", RED)
            show_score(length_of_snake - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = BLOCK_SIZE
                    x1_change = 0
        
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
            
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        
        pygame.draw.rect(screen, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = [x1, y1]
        snake_body.append(snake_head)
        
        if len(snake_body) > length_of_snake:
            del snake_body[0]
            
        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True
                
        for block in snake_body:
            pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])
        
        show_score(length_of_snake - 1)
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1
            
        clock.tick(SPEED)
        
    pygame.quit()
    quit()

game_loop()