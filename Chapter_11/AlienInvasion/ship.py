import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen 

        #load ship image
        self.image = pygame.image.load('Chapter_11/AlienInvasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start a new ship at the bottom of the screen 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''Draw ship at its current location'''
        self.screen.blit(self.image, self.rect)