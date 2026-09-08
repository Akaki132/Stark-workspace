import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Mens et Manus")
icon = pygame.image.load("Images/images.png")
pygame.display.set_icon(icon)

object1 = pygame.Surface((30, 90))
object1.fill("Grey")

if_true = True

while if_true:
    screen.blit(object1,(0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if_true = False
            pygame.quit()