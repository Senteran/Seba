import pygame
import random

from lib import constants

def main():
    pygame.init()

    image = pygame.image.load('seba.png')
    images = [pygame.image.load('cl.png'), pygame.image.load('erty.png'), pygame.image.load('exeos.png'), pygame.image.load('hot.png'), pygame.image.load('kfra.png'), pygame.image.load('krup.png'), pygame.image.load('seba.png'), pygame.image.load('sent.png')]
    pygame.display.set_icon(image)
    pygame.display.set_caption('Seba!')

    screen = pygame.display.set_mode((1280,720))

    running = True

    coords = [[10, 10], [300, 10], [10, 300], [150, 150], [250, 100], [1000, 10], [10, 500], [400, 400]]
    directions = [[True, True], [True, True], [True, True], [True, True], [True, True], [True, True], [True, True], [True, True]]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    screen = pygame.display.set_mode((1920,1080))
                if event.key == pygame.K_2:
                    screen = pygame.display.set_mode((1280,720))
                if event.key == pygame.K_3:
                    screen = pygame.display.set_mode((1000, 1000))
        
        screen.fill((50,50,50))

        display_info = pygame.display.Info()
        width = display_info.current_w
        height = display_info.current_h

        for i in range(8):
            screen.blit(images[i], (coords[i][0], coords[i][1]))
            ran = random.randint(1, 10)
            dir_change = random.randint(1, 1000)
            if dir_change == 50:
                directions[i][0] = not directions[i][0]
            if dir_change == 51:
                directions[i][1] = not directions[i][1]
            if directions[i][0]:
                dir_modifier_x = constants.move_value
            else:
                dir_modifier_x = -1 * constants.move_value
            if directions[i][1]:
                dir_modifier_y = constants.move_value
            else:
                dir_modifier_y = -1 * constants.move_value

            if True:
                coords[i][1] = coords[i][1] + dir_modifier_y
            if True:
                coords[i][0] = coords[i][0] + dir_modifier_x
            
            if(coords[i][0] > width - 50):
                coords[i][0] = 10
            if(coords[i][1] > height - 50):
                coords[i][1] = 10
            if(coords[i][0] < 0):
                coords[i][0] = width - 50
            if(coords[i][1] < 0):
                coords[i][1] = height - 50

        pygame.display.flip()

if __name__ == '__main__':
    main()