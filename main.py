import pygame
import sys
import math
import pygame.draw
from pygame.locals import *

pygame.display.set_caption("Roboter Test")
pygame.init()
screen = pygame.display.set_mode([1200, 900])
clock = pygame.time.Clock()
fps = 60

rob_dir = [0, 1]
rob_ax1 = 350
rob_ax2 = []
rob_ax3 = []
rob_ay1 = 470
rob_ay2 = []
rob_ay3 = []
arr_count = 4

img_ax1 = [pygame.image.load("graphics/ax24.png").convert_alpha(),pygame.image.load("graphics/ax23.png").convert_alpha(),pygame.image.load("graphics/ax22.png").convert_alpha(),pygame.image.load("graphics/ax21.png").convert_alpha(),pygame.image.load("graphics/ax10.png").convert_alpha(), pygame.image.load("graphics/ax11.png").convert_alpha(), pygame.image.load("graphics/ax12.png").convert_alpha(), pygame.image.load("graphics/ax13.png").convert_alpha(), pygame.image.load("graphics/ax14.png").convert_alpha()]
#img_ax2 = [pygame.image.load("graphics/testrot.png").convert_alpha(), pygame.image.load("graphics/testblu.png").convert_alpha(), pygame.image.load("graphics/testyel.png").convert_alpha(), pygame.image.load("graphics/testgrey.png").convert_alpha(), pygame.image.load("graphics/testblrot.png").convert_alpha()]
#img_ax3 = [pygame.image.load("graphics/testrot.png").convert_alpha(), pygame.image.load("graphics/testblu.png").convert_alpha(), pygame.image.load("graphics/testyel.png").convert_alpha(), pygame.image.load("graphics/testgrey.png").convert_alpha(), pygame.image.load("graphics/testblrot.png").convert_alpha()]


class robot:
    def __init__(self, rob_dir, rob_ax1,rob_ax2,rob_ax3,rob_ay1,rob_ay2,rob_ay3,arr_count):
        self.rob_dir = rob_dir
        self.rob_ax1 = rob_ax1
        self.rob_ax2 = rob_ax2
        self.rob_ax3 = rob_ax3
        self.rob_ay1 = rob_ay1
        self.rob_ay2 = rob_ay2
        self.rob_ay3 = rob_ay3
        self.arr_count = arr_count

    def move(self):
        if rob_dir[0]:
            pass
        if rob_dir[1]:
            screen.blit(img_ax1[self.arr_count], (self.rob_ax1, self.rob_ay1))


def draw_ui():
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1200, 175))

def draw_obs():
    pygame.draw.rect(screen, (255,255,0), (475, 850, 275, 50))




runtime = True
while runtime:

    if arr_count >= 9:
        arr_count = 8
    elif arr_count < 0:
        arr_count = 0
    robo = robot(rob_dir, rob_ax1, rob_ax2, rob_ax3, rob_ay1, rob_ay2, rob_ay3, arr_count)


    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if pressed[pygame.K_ESCAPE]:
            runtime = False
        if pressed[pygame.K_d]:
            arr_count += 1
        if pressed[pygame.K_a]:
            arr_count -= 1


    screen.fill((50, 50, 50))



    draw_ui()
    robo.move()
    draw_obs()
    pygame.display.update()
    clock.tick(fps)