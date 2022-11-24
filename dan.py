import pygame
import pysound


pygame.init()
dis=pygame.display.set_mode((1000,500))
pygame.display.update()
pygame.display.set_caption('Đàn chơi')
game_end=False
while not game_end:
    #Lấy ra các sự kiện xảy ra
    for event in pygame.event.get():
    	if event.type==pygame.QUIT:
            game_end=True
            


#Thoát trò chơi
pygame.quit()
quit()