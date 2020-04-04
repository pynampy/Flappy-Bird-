import pygame
import random
from random import randint
import math
import sys

(HEIGHT,WIDTH) = (600,1200)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
bg = pygame.image.load("bg.png").convert()
base = pygame.image.load("base.png").convert()
lower_pipe = pygame.image.load("pipe.png").convert_alpha()
upper_pipe = pygame.transform.rotate(pygame.image.load("pipe.png").convert(),180)
flappy1 = pygame.transform.scale2x(pygame.image.load("bird1.png").convert_alpha())
starting_screen = pygame.image.load("ss.png").convert()
flappy2 = pygame.transform.scale2x(pygame.image.load("bird2.png").convert())
flappy3 = pygame.transform.scale2x(pygame.image.load("bird3.png").convert())
flappy = [flappy1,flappy2,flappy3]

bird_mask = [pygame.mask.from_surface(flappy1),pygame.mask.from_surface(flappy2),pygame.mask.from_surface(flappy3)]
lowerpipe_mask = pygame.mask.from_surface(lower_pipe)
upperpipe_mask = pygame.mask.from_surface(upper_pipe)


def bird():

    global BIRD_Y, VEL_Y,ACC_Y
   
    if ACC_Y < 10:
        ACC_Y = ACC_Y + 50
    elif ACC_Y > 10:
        ACC_Y = ACC_Y - 30
    
    VEL_Y = VEL_Y + ACC_Y
    VEL_Y = min(VEL_Y,600)
    BIRD_Y = BIRD_Y + VEL_Y/60
    
    if BIRD_Y >= 510:
        BIRD_Y = 510

    if VEL_Y > 0:
        x = 0
    elif VEL_Y < 0:
        x = 2
    else: x = 1 
    screen.blit(flappy[x],(100,BIRD_Y))    


def pipes():

    global score
    for x in range(5):

        screen.blit(upper_pipe,(x_pipe[x],y_pipe[x]))
        screen.blit(lower_pipe,(x_pipe[x],y_pipe[x]+550))

        x_pipe[x] = x_pipe[x] -3

        if x_pipe[x] < -100:
            x_pipe[x] = 1240
            y_pipe[x] = randint(-200,0)
            
        if x_pipe[x] < 100:
            score = score + 1

        x_offset = int(-100 + x_pipe[x]) #
        y_offset = int(-BIRD_Y + y_pipe[x]+550) #

        for x in range(3):
            if bird_mask[x].overlap(lowerpipe_mask,(x_offset,y_offset)):
                return 0
            if bird_mask[x].overlap(upperpipe_mask,(x_offset,y_offset-550)):
                return 0

running = True 
pygame.init()

while running:
    
    screen.blit(starting_screen,(0,0))
    pygame.display.flip()
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False
            if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

running = True
variable = True

if __name__ == "__main__":
    while variable:
        y_pipe = [-300,-300,-300,-300,-300]
        x_pipe = [400,650,900,1200,1450]
        BIRD_Y= 100
        VEL_Y = 30
        ACC_Y = 10
        score = 0
        while running:
            clock.tick(60)
            screen.blit(bg,(0,0))            
            bird()
            y = pipes()
            if y == 0:
                print("Your Score is : ",score)
                pygame.time.wait(2000)
                break
            screen.blit(base,(0,555))
            pygame.display.flip()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    VEL_Y = -300
                    BIRD_Y = BIRD_Y - 30   # MORE PUNCH
                    #ACC_Y = - 300   # PHYSICS ACCCURATE

