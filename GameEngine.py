import os,sys
import pygame
from pygame.locals import *
import time

from ContrEstados import *


class GameEngine(object):
    """Engine de jogo principal"""
    def __init__(self, windowed):
        self.windowed = windowed
        self.inicializa()
        
    def inicializa(self,):
        """Inicia engine de jogo"""
        #Inicializa pygame
        pygame.init()

        #Inicializa tempo
        self.tempoantigo = time.time()

        if self.windowed:
            #self.window = pygame.display.set_mode((800,600))
            self.window = pygame.display.set_mode((800,600),pygame.FULLSCREEN)#|pygame.HWSURFACE|pygame.DOUBLEBUF)
        else:
            self.window = pygame.display.set_mode((800,600))
            #self.window = pygame.display.set_mode((800,600),pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF)

        pygame.mouse.set_visible(False)            
        self.screen = pygame.display.get_surface()

        for i in range(pygame.joystick.get_count()):
            pygame.joystick.Joystick(i).init()


    
    def run(self,):
        """Loop principal do jogo, calcula tempo e executa controlador de estados"""
        Estado = ContrEstados()

        sair = False        
        #Captura tempo
        while not sair:
            #seta dtempo
            tempo = time.time()
            dtempo = tempo - self.tempoantigo
            self.tempoantigo = tempo

            sair = Estado.update(dtempo,pygame.event.get())
            Estado.render(self.screen)

        Estado.unload()        
        pygame.quit()
        return True
