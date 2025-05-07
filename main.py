import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
background = pygame.image.load("sky.jpg")
def draw():
    #Wo ist der Kommentar?
    screen.blit(background, (0, 0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()
