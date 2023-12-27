import time
import random


def game_vnesh():
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    dis_width = 800
    dis_height = 600
    snake_List = []
    Length_of_snake = 1
    snake_block = 10
    snake_speed = 15
    x1 = dis_width / 2
    y1 = dis_height / 2
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_List.append(snake_head)

    
    def Your_score(score):
        value = score_font.render("Счет: " + str(score), True, white)
        dis.blit(value, [0, 0])

    def Your_choice():
        smallfont = pygame.font.SysFont(None, 35)
        text = smallfont.render("Нажмите стрелку вверх для перезапуска или стрелку вниз для выхода", True, white)
        dis.blit(text, [dis_width / 5, dis_height / 1.5])
    
    return dis_width, dis_height, snake_speed, blue, green, red,  Your_score, Your_choice, snake_head, snake_head.append, snake_List.append