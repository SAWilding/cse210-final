from game import constants
from game.point import Point

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
        _width (int): The actor's width
        _height (int): The actor's height
        _image (string): The file path of the image file (if present)
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Actor): an instance of Actor.
        """
        self._name = ""
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._width = 0
        self._height = 0
        self._image = ""
        self._animation = []
        self._frame = 0

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        
    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
    
    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_image(self):
        return self._image
    
    def set_image(self, image):
        self._image = image

    def get_left_edge(self):
        return self._position.get_x()

    def get_right_edge(self):
        return self._position.get_x() + self._width

    def get_top_edge(self):
        return self._position.get_y()

    def get_bottom_edge(self):
        return self._position.get_y() + self._height

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor's textual representation.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def set_text(self, text):
        self._text = text

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given position.
        """
        self._position = position
    
    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            self (Actor): An instance of Actor.
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given velocity.
        """
        self._velocity = velocity

    def has_text(self):
        return self._text != ""

    def has_image(self):
        return self._image != ""

    def has_animation(self):
        return self._animation != []

    def set_animation(self, frames):
        for frame in frames:
            self._animation.append(frame)

    def get_animation(self):
        return self._animation

    def get_frame(self):
        return self._frame
    
    def add_frame(self):
        if int(self._frame) == len(self._animation) - 1:
            self._frame = 0
        else:
            self._frame += constants.FRAME_SPEED
