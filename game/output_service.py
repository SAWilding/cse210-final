from game import constants
import pygame

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        None
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
        """
        self._textures = {}

        self._window = pygame.display.set_mode((constants.MAX_X, constants.MAX_Y))
        self._clock = pygame.time.Clock()

    def open_window(self, title):
        """
        Opens a new window with the provided title.
        """
        pygame.display.set_caption("Space Evader")
        self._clock.tick(constants.FRAME_RATE)
        
    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._window.fill((0, 0, 0))


    def draw_box(self, x, y, width, height, color=(0, 0, 255)):
        """
        Draws at rectangular box with the provided specifications.
        """
        rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self._window, color, rect)

    def draw_text(self, x, y, text, is_dark_text):
        """
        Outputs the provided text at the desired location.
        """
        white = (255, 255, 255)

        if pygame.font.get_init() == False:
            pygame.font.init()

        my_font = pygame.font.SysFont("Rockwell", 25)
        

        self._window.blit(my_font.render(text, True, white), (x + 5, y + 5))

    def draw_image(self, x, y, image):
        """
        Outputs the provided image on the screen.
        """
        if image not in self._textures.keys():

            loaded = pygame.image.load(image)
            self._textures[image] = loaded

        texture = self._textures[image]
        
        self._window.blit(texture, (x, y))

    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actor (Actor): The actor to render.
        """ 
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        width = actor.get_width()
        height = actor.get_height()
        frame = actor.get_frame()
        animation_length = len(actor.get_animation())
        if actor.has_image():
            image = actor.get_image()
            self.draw_image(x, y, image)
        elif actor.has_animation():
            animation = actor.get_animation()
            self.draw_image(x, y, animation[int(frame)])
            actor.add_frame()
        elif actor.has_text():
            text = actor.get_text()
            self.draw_text(x, y, text, True)
        elif (width > 0 and height > 0) and (actor.has_animation == False):
            self.draw_box(x, y, width, height)

    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        pygame.display.update()