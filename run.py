import pygame, sys
pygame.init()
scr = pygame.display.set_mode((700,700))
cl = pygame.time.Clock()
font = pygame.font.Font('font/Blocktopia.ttf', 50)
pygame.display.set_caption("Poolsweeper")
bg = pygame.image.load("img/bg.png").convert()

soap = pygame.image.load("img/soap.png").convert_alpha()
soap = pygame.transform.scale(soap, (35, 35))

paused = True

title = font.render("Poolsweeper", False, "Black")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    scr.blit(bg,(0,0))
    scr.blit(title,(220,100))
    scr.blit(soap,(50,50))
    pygame.display.update()
    cl.tick(30)
