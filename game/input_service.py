import sys
from game.point import Point
import pygame
from pygame.constants import *

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        pass
        
    def is_space_pressed(self):
        for event in pygame.event.get(KEYDOWN):
            if event.key == K_SPACE:
                return True

