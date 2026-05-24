import pygame
from const import *

class Game:
    def __init__(self):
        pass
    #show methods
    def show_bg(self,surface):
        for rows in range (ROWS):
            for cols in range (CLS):
                if (rows+cols)%2==0:
                    color=(234,235,200)
                else:
                    color=(119,154,88)
                rect=(cols * SQSIZE,rows * SQSIZE,SQSIZE,SQSIZE)
                
                pygame.draw.rect(surface,color,rect)
                
       
        
            
        
    