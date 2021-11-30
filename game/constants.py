import os
from game.point import Point
from random import randint

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 60

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

SCORE_WIDTH = 75
SCORE_HEIGHT = 25

IMAGE_PLAYER = os.path.join(os.getcwd(), "./cse210-final/assets/player.png")

SOUND_PLAYER_DEATH = os.path.join(os.getcwd(), "./cse210-final/assets/hitHurt.wav")
SOUND_SCORE = os.path.join(os.getcwd(), "./cse210-final/assets/pickupCoin.wav")
SOUND_JUMP = os.path.join(os.getcwd(), "./cse210-final/assets/jump.wav")




GRAVITY = .5
MAX_GRAVITY_SPEED = 8
PLAYER_JUMP = 15
PLAYER_HEIGHT = 16
PLAYER_WIDTH = 16

IMAGE_OBSTACLE = os.path.join(os.getcwd(), "./cse210-final/assets/obstacle.png")

OBSTACLE_HEIGHT = 300
OBSTACLE_WIDTH = 8
OBSTACLE_SPEED = -4
