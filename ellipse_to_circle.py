import pygame
from pygame import gfxdraw
import math
import sys

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
size = [1400, 1200]
screen = pygame.display.set_mode(size) 
screen.fill(white)


pygame.draw.ellipse(screen, black, (250,250,700,100),1)
pygame.display.update()
pygame.time.wait(300)
screen.fill(white)

pygame.draw.ellipse(screen, black, (250,250,650,150),1)
pygame.display.update()
pygame.time.wait(300)
screen.fill(white)

pygame.draw.ellipse(screen, black, (250,250,600,200),1)
pygame.display.update()
pygame.time.wait(300)
screen.fill(white)

pygame.draw.ellipse(screen, black, (250,250,550,250),1)
pygame.display.update()
pygame.time.wait(300)
screen.fill(white)

pygame.draw.ellipse(screen, black, (250,250,500,300),1)
pygame.display.update()
pygame.time.wait(300)
screen.fill(white)

pygame.draw.ellipse(screen, black, (250,250,450,350),1)
pygame.display.update()
pygame.time.wait(300)
screen.fill(white)

pygame.draw.ellipse(screen, black, (250,250,400,400),1)
pygame.display.update()
pygame.time.wait(300)
screen.fill(white)


while True:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			pygame.quit()
			sys.exit()