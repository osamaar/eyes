import pygame
from vect2d import Vect2d

RESOLUTION = (800, 600)
CAPTION = 'eyes'
BGCOLOR = (80, 80, 80)

class Eye:
    def __init__(self, cx, cy):
        self.c0 = Vect2d(cx, cy)
        self.c1 = Vect2d(cx, cy)
        self.r0 = 100
        self.r1 = 50
        self.target = Vect2d(cx+self.r0, cy)
        self.br = 0
        self.lw = 1
        self.c0color = (254, 254, 254)
        self.c1color = (50, 100, 127)
        self.lcolor = (150, 20, 20)

    def look(self, x, y):
        self.target.x = x
        self.target.y = y
        c0_t = self.target - self.c0
        u = c0_t.unit()
        c1 = self.c0 + u*(self.r0 - self.r1)
        self.c1.x = int(c1.x)
        self.c1.y = int(c1.y)

    def draw(self, screen):
        pygame.draw.circle(screen, self.c0color, self.c0, self.r0, self.br)
        pygame.draw.circle(screen, self.c1color, self.c1, self.r1, self.br)
        #pygame.draw.line(screen, self.lcolor, self.c0, self.target, self.lw)

def mainloop():
    # init pygame
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption(CAPTION)
    screen.fill(BGCOLOR)

    x, y = 0, 0

    spacing = 50
    eyel = Eye((RESOLUTION[0]-spacing)/2 - 100, 250)
    eyer = Eye((RESOLUTION[0]+spacing)/2 + 100, 250)

    frames = 0
    done = False
    while not done:
        # events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done = True
            elif (event.type==pygame.KEYUP and
                  event.key==pygame.K_ESCAPE):
                done = True
            elif (event.type==pygame.KEYUP and
                  event.key==pygame.K_SPACE):
                pass
            elif event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                
        # update
        eyel.look(x, y)
        eyer.look(x, y)

        # draw
        screen.fill(BGCOLOR)
        eyel.draw(screen)
        eyer.draw(screen)
        
        pygame.display.flip()
        clock.tick(fps)
        frames += 1
        
    pygame.quit()

def main():
    mainloop()
    
if __name__ == '__main__': main()
