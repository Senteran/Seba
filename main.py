import pygame
import random

def main():
    pygame.init()

    image = pygame.image.load('seba.png')
    pygame.display.set_icon(image)
    pygame.display.set_caption('Seba!')

    screen = pygame.display.set_mode((1280,720))

    running = True

    coords = [10, 10]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((50,50,50))
        screen.blit(image, (coords[0], coords[1]))

        ran = random.randint(1, 10)

        if(ran < 4):
            coords[1] = coords[1] + 1
        else:
            coords[0] = coords[0] + 1
        
        if(coords[0] > 1150):
            coords[0] = 0
        else: 
            if(coords[1] > 600):
                coords[1] = 10

        pygame.display.flip()

if __name__ == '__main__':
    main()