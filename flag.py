import pygame

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
screen.fill((150, 150, 150))

def draw():
    width = 0
    color = (0, 0, 0)
    point = [(40,40), (5,420)]
    pygame.draw.rect(screen, color, point, width)

    color = (255, 255, 255)
    point = [(45,40), (415,100)]
    pygame.draw.rect(screen, color, point, width)

    color = (0, 0, 255)
    point = [(45,140), (415,100)]
    pygame.draw.rect(screen, color, point, width)

    color = (255, 0, 0)
    point = [(45,240), (415,100)]
    pygame.draw.rect(screen, color, point, width)

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()