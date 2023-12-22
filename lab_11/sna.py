import pygame
import time
import random

def game_logic():
    snake_block = 10
    snake_speed = 15

    x1 = 300
    y1 = 300
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    dis_width = 800
    dis_height = 600
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Змейка на Python')

    white = (255, 255, 255)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    game_close = False

    while not game_close:
        for event in pygame.event.get():
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
                    pygame.quit()
                    quit()

        x1 += x1_change
        y1 += y1_change

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_List.append(snake_head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        for segment in snake_List:
            pygame.draw.rect(dis, green, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        pygame.time.Clock().tick(snake_speed)
        pygame.time.delay(50)  # Задержка в 50 миллисекунд


    pygame.quit()
    quit()

def game_vnesh():
    pygame.init()

    white = (255, 255, 255)
    green = (0, 255, 0)


    dis = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Змейка на Python')

    score_font = pygame.font.SysFont(None, 35)

    game_logic()

game_vnesh()
