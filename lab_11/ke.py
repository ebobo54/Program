import pygame
import time
import random
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