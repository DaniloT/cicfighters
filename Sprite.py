import os,sys
import pygame
from pygame.locals import *

class Sprite(object):
    """Classe para carregar sprites estaticos e animados a partir de uma imagem grande,
    recebe o width e height do frame e o fps para criar uma lista dos frames"""
    def __init__(self,arquivo,(width,height) = (0,0),fps = False,(esticaw,esticah) = (0,0)):
        #carrega arquivo temporariamente para quebrar em superficies
        superficie = pygame.image.load(arquivo)

        if not width: width = superficie.get_width()
        if not height: height = superficie.get_height()

        #prepara o corte da imagem        
        corte = pygame.Rect(0,0,width,height)
        self.frames = []

        linha = 0
        try:
            for i in range( (superficie.get_width()/width) * (superficie.get_height()/height)):
                if esticaw and esticah:
                    self.frames.append(pygame.transform.scale(superficie.subsurface(corte), ((int)(esticaw), (int)(esticah))))
                else:
                    self.frames.append(superficie.subsurface(corte))
                corte.move_ip(width,0)
                if corte.left >= superficie.get_width():
                    linha = linha + 1
                    corte = pygame.Rect(0,linha*height,width,height)
        #caso haja recorte fora da imagem pare de recortar
        except ValueError:
            if self.frames == []:
                self.frames.append(superficie)
                print "Aviso: Houve um recorte de imagem maior que seu tamanho, arquivo", arquivo,
                print ",tamanho da imagem:",superficie.get_width(),"x",superficie.get_height(),
                print ",recorte solicitado:",width,"x",height

        self.frameatual = 0
        self.estatico = False
        if (not fps) or (len(self.frames) == 1):
            self.estatico = True
        else:
            self.tempotroca = 1./fps
        self.tempo = 0

    def update(self,dtempo):
        """Troca o frame da animacao dependendo do tempo"""
        acabou = False
        if not self.estatico:
            self.tempo = self.tempo + dtempo
            if self.tempo >= self.tempotroca:
                for i in range(int(self.tempo/self.tempotroca)):
                    self.frameatual = (self.frameatual + 1) % len(self.frames)
                    self.tempo = 0
                    #Se a animacao acabar retorna True para casos que rodem a animacao somente 1 vez
                    if self.frameatual == 0: acabou = True
        else:
            return True
        
        return acabou

    def render(self,screen,(x,y),(deslocx,deslocy) = (0,0),inverter = False):
        """Renderiza a animacao na posicao x,y da tela"""
        if inverter:
            screen.blit(pygame.transform.flip(self.frames[self.frameatual], True, False),(x+deslocx,y+deslocy)) 
        else:
            screen.blit(self.frames[self.frameatual],(x+deslocx,y+deslocy))

    def unload(self,):
        """Descarrega Animacao"""
        return True

