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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((50,50,50))

        for i in range(8):
            screen.blit(images[i], (coords[i][0], coords[i][1]))
            ran = random.randint(1, 10)

            if(ran < 4):
                coords[i][1] = coords[i][1] + 1
            else:
                coords[i][0] = coords[i][0] + 1
            
            if(coords[i][0] > 1150):
                coords[i][0] = 10
            if(coords[i][1] > 600):
                coords[i][1] = 10

        pygame.display.flip()

if __name__ == '__main__':
    main()