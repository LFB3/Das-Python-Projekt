import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
background = pygame.image.load("sky.jpg")
def draw():
    # Irgendwas ist noch nicht ganz richtig
    screen.blit(background, (0, 0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()