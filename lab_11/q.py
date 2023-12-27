import pygame
import time
import random
# from r import game_vnesh
# dis_width, dis_height, snake_speed,  blue, green, red, Your_score, Your_choice, snake_head, snake_List = game_vnesh()
from r import *

def game():
    # dis_width, dis_height, snake_speed,  blue, green, red, Your_score, Your_choice,snake_head, snake_head.append, snake_List.append = game_vnesh() 
    game_over = False
    game_close = False
    font_style = pygame.font.SysFont(None, 50)
    score_font = pygame.font.SysFont(None, 35)
    x1 = dis_width / 2
    y1 = dis_height / 2
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Змейка на Python')
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            Your_score(Length_of_snake - 1)
            Your_choice()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if y1_change == 0:  
                            game()
                    elif event.key == pygame.K_DOWN:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_ESCAPE:
                    game_over = True

        #проверка границ 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        def our_snake(snake_block, snake_list):
            for x in snake_list:
                pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()
        #генрация еды
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

game()
