import pygame
import time
import random

def game_logic():

    snake_block = 10
    snake_speed = 15

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    dis_width = 800 
    dis_height = 600
    dis = pygame.display.set_mode((dis_width, dis_height))
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while True:
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


            game_close = True
        x1 += x1_change
        y1 += y1_change

        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        pygame.time.Clock().tick(snake_speed)


game_logic()
def game_vnesh():
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

    def Your_score(score):
        value = score_font.render("Счет: " + str(score), True, white)
        dis.blit(value, [0, 0])

    def Your_choice():
        smallfont = pygame.font.SysFont(None, 35)
        text = smallfont.render("Нажмите стрелку вверх для перезапуска или стрелку вниз для выхода", True, white)
        dis.blit(text, [dis_width / 5, dis_height / 1.5])

    pygame.init()

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    dis =pygame.display.set_mode((800,600))
    pygame.display.set_caption('Змейка на Python')
    gameloop()
game_vnesh()