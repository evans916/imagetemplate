import pygame
pygame.init()

screen = pygame.display.set_mode((600,600),pygame.RESIZABLE)
pygame.display.set_caption('porn')
icon = pygame.image.load("22761865_058_94a7.jpg")
pygame.display.set_icon(icon)
image1 = pygame.image.load("22761865_058_94a7.jpg")
image2 = pygame.image.load("38053209_313_b3e6.jpg")
image3 = pygame.image.load("58308853_083_cb11.jpg")
image4 = pygame.image.load("62624016_074_a5d6.jpg")
image5 = pygame.image.load("45786121_040_6d42.jpg")
image6 = pygame.image.load("93750900_012_2290.jpg")

size1=(300,200)
size2=(250,350)
size3=(200,150)

image11 = pygame.transform.scale(image1,size1)
image21 = pygame.transform.scale(image2,size2)
image31 = pygame.transform.scale(image3,size2)
image41 = pygame.transform.scale(image4,size2)
image51 = pygame.transform.scale(image5,size2)
image61 = pygame.transform.scale(image6,size2)

color = 'red'
running = True
screen.fill(color)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(color)
    screen.blit(image1,(25,25))
    screen.blit(image21,(10,25))
    screen.blit(image31,(10,400))
    screen.blit(image41,(800,25))
    screen.blit(image51,(500,25))
    screen.blit(image61,(1050,25))
    pygame.display.flip()
