import pygame
import sys


pygame.display.set_caption("Roboter Test")
pygame.init()
screen = pygame.display.set_mode([1200, 900])
clock = pygame.time.Clock()
fps = 60

rob_dir = [0, 1]
rob_ax1 = 350
rob_ax2 = 253
rob_ax3 = []
rob_ay1 = 470
rob_ay2 = 270
rob_ay3 = []
arr_ax1_count = 4
arr_ax2_count = 6
arr_ax2_count_2 = 5

img_ax1 = [pygame.image.load("graphics/ax24.png").convert_alpha(),pygame.image.load("graphics/ax23.png").convert_alpha(),pygame.image.load("graphics/ax22.png").convert_alpha(),pygame.image.load("graphics/ax21.png").convert_alpha(),pygame.image.load("graphics/ax10.png").convert_alpha(), pygame.image.load("graphics/ax11.png").convert_alpha(), pygame.image.load("graphics/ax12.png").convert_alpha(), pygame.image.load("graphics/ax13.png").convert_alpha(), pygame.image.load("graphics/ax14.png").convert_alpha()]
img_ax2_pos4 = [pygame.image.load("graphics/links animiert/ax100.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax101.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax102.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax103.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax104.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax105.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax106.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax107.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax108.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax109.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax1010.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax1011.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax1012.png").convert_alpha()]
img_ax2_pos3 = [pygame.image.load("graphics/links animiert/ax110.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax111.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax112.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax113.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax114.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax115.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax116.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax117.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax118.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax119.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax1110.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax1111.png").convert_alpha(), pygame.image.load("graphics/links animiert/ax1112.png").convert_alpha()]
img_ax2_pos2 = [pygame.image.load("graphics/links animiert/120.png").convert_alpha(), pygame.image.load("graphics/links animiert/121.png").convert_alpha(), pygame.image.load("graphics/links animiert/122.png").convert_alpha(), pygame.image.load("graphics/links animiert/123.png").convert_alpha(), pygame.image.load("graphics/links animiert/124.png").convert_alpha(), pygame.image.load("graphics/links animiert/125.png").convert_alpha(), pygame.image.load("graphics/links animiert/126.png").convert_alpha(), pygame.image.load("graphics/links animiert/127.png").convert_alpha(), pygame.image.load("graphics/links animiert/128.png").convert_alpha(), pygame.image.load("graphics/links animiert/129.png").convert_alpha(), pygame.image.load("graphics/links animiert/1210.png").convert_alpha(), pygame.image.load("graphics/links animiert/1211.png").convert_alpha(), pygame.image.load("graphics/links animiert/1212.png").convert_alpha()]

class robot:
    def __init__(self, rob_dir, rob_ax1,rob_ax2,rob_ax3,rob_ay1,rob_ay2,rob_ay3):
        self.rob_dir = rob_dir
        self.rob_ax1 = rob_ax1
        self.rob_ax2 = rob_ax2
        self.rob_ax3 = rob_ax3
        self.rob_ay1 = rob_ay1
        self.rob_ay2 = rob_ay2
        self.rob_ay3 = rob_ay3
        self.arr_ax1_count = arr_ax1_count
        self.arr_ax2_count = arr_ax2_count
        self.arr_ax2_count_2 = arr_ax2_count_2

    def move(self):
        if rob_dir[0]:
            pass
        if rob_dir[1]:
            screen.blit(img_ax1[self.arr_ax1_count], (self.rob_ax1, self.rob_ay1))
            if arr_ax1_count == 2:
                screen.blit(img_ax2_pos2[self.arr_ax2_count_2], (253, 270))
            if arr_ax1_count == 3:
                screen.blit(img_ax2_pos3[self.arr_ax2_count], (253, 270))
            if arr_ax1_count == 4:
                screen.blit(img_ax2_pos4[self.arr_ax2_count], (253, 270))


def draw_ui():
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1200, 175))

def draw_obs():
    pygame.draw.rect(screen, (255,255,0), (475, 850, 275, 50))




runtime = True
while runtime:

    if arr_ax1_count >= 8:
        arr_ax1_count = 8
    elif arr_ax1_count < 0:
        arr_ax1_count = 0
    if arr_ax2_count >= 13:
        arr_ax2_count = 12
    elif arr_ax2_count < 0:
        arr_ax2_count = 0
    if arr_ax2_count_2 >= 13:
        arr_ax2_count_2 = 12
    elif arr_ax2_count_2 < 0:
        arr_ax2_count_2 = 0

    robo_ax1 = robot(rob_dir, rob_ax1, rob_ax2, rob_ax3, rob_ay1, rob_ay2, rob_ay3)
    #robo_ax2 = robot(rob_dir, rob_ax1, rob_ax2, rob_ax3, rob_ay1, rob_ay2, rob_ay3, arr_ax2_count)


    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if pressed[pygame.K_ESCAPE]:
            runtime = False
        if pressed[pygame.K_d]:
            arr_ax1_count += 1
            print(arr_ax2_count, arr_ax1_count)
        if pressed[pygame.K_a]:
            arr_ax1_count -= 1
            print(arr_ax2_count, arr_ax1_count)
        if pressed[pygame.K_s]:
            arr_ax2_count += 1
            arr_ax2_count_2 += 1
            print(arr_ax2_count, arr_ax1_count)
        if pressed[pygame.K_w]:
            arr_ax2_count -= 1
            arr_ax2_count_2 -= 1
            print(arr_ax2_count, arr_ax1_count)


    screen.fill((50, 50, 50))



    draw_ui()
    robo_ax1.move()
    draw_obs()
    pygame.display.update()
    clock.tick(fps)