import pygame
from pygame.draw import *

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (100, 0, 100), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 110)
circle(screen, (0, 0, 0), (200, 200), 110, 2)
rect(screen, (0, 0, 0), (150, 260, 100, 22))
circle(screen, (255, 0, 0), (150, 180), 20)
circle(screen, (0, 0, 0), (150, 180), 8)
circle(screen, (255, 0, 0), (250, 180), 16)
circle(screen, (0, 0, 0), (250, 180), 8)
polygon(screen, (0, 0, 0), [(100, 100), (108,92),
                               (176,160), (168, 170)])
polygon(screen, (0, 0, 0), [(233, 173), (225, 163), (323, 103), (330,113)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()




