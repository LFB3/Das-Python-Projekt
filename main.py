import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
background = pygame.image.load("sky.jpg")
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.velocity = [0, 0]

    def gravity(self):
        self.velocity[1] += .1



        self.y = self.y - self.velocity[1]
def draw():
    screen.blit(background, (0, 0))
Player = Player()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_UP:
                Player.velocity[1] += 10
            if event.key == pygame.K_DOWN:
                Player.velocity[1] -= 10
    draw()
    pygame.display.update()
pygame.display.quit()