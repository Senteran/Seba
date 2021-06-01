import pygame
import random

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
        
        screen.fill((50,50,50))

        for i in range(8):
            screen.blit(images[i], (coords[i][0], coords[i][1]))
            ran = random.randint(1, 10)
            dir_change = random.randint(1, 1000)
            if dir_change == 50:
                directions[i][0] = not directions[i][0]
            if dir_change == 51:
                directions[i][1] = not directions[i][1]
            if directions[i][0]:
                dir_modifier_x = 1
            else:
                dir_modifier_x = -1
            if directions[i][1]:
                dir_modifier_y = 1
            else:
                dir_modifier_y = -1

            if(ran < 4):
                coords[i][1] = coords[i][1] + dir_modifier_y
            else:
                coords[i][0] = coords[i][0] + dir_modifier_x
            
            if(coords[i][0] > 1100):
                coords[i][0] = 10
            if(coords[i][1] > 600):
                coords[i][1] = 10
            if(coords[i][0] < 0):
                coords[i][0] = 1100
            if(coords[i][1] < 0):
                coords[i][1] = 600

        pygame.display.flip()

if __name__ == '__main__':
    main()