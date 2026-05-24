import pygame
import sys

from game import *
from const import *

class Main:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Chess.fun")
        self.game=Game()
    def mainloop(self):
        # Game loop
        running = True
        while running:
            self.game.show_bg(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
            pygame.display.update()         
                
main=Main()
main.mainloop()

    