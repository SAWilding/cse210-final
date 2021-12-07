import os
from game.point import Point
from random import randint

MAX_X = 800
MAX_Y = 504
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
SOUND_COW = os.path.join(os.getcwd(), "./cse210-final/assets/CowMoo.wav")



GRAVITY = .5
MAX_GRAVITY_SPEED = 8
PLAYER_JUMP = 15
PLAYER_HEIGHT = 25
PLAYER_WIDTH = 42

IMAGE_OBSTACLE = os.path.join(os.getcwd(), "./cse210-final/assets/obstacle.png")

OBSTACLE_HEIGHT = 286
OBSTACLE_WIDTH = 32
OBSTACLE_SPEED = -4

IMAGE_COIN_ANIMATION = [os.path.join(os.getcwd(), "./cse210-final/assets/cow.png"),
os.path.join(os.getcwd(), "./cse210-final/assets/cow30.png"),
os.path.join(os.getcwd(), "./cse210-final/assets/cow60.png"),
os.path.join(os.getcwd(), "./cse210-final/assets/cow90.png"),
os.path.join(os.getcwd(), "./cse210-final/assets/cow120.png"),
os.path.join(os.getcwd(), "./cse210-final/assets/cow150.png"),
os.path.join(os.getcwd(), "./cse210-final/assets/cow180.png"),
os.path.join(os.getcwd(), "./cse210-final/assets/cow210.png"),
os.path.join(os.getcwd(), "./cse210-final/assets/cow240.png"),
os.path.join(os.getcwd(), "./cse210-final/assets/cow270.png"),
os.path.join(os.getcwd(), "./cse210-final/assets/cow300.png"),
os.path.join(os.getcwd(), "./cse210-final/assets/cow330.png")]

FRAME_SPEED = 0.15
COIN_HEIGHT = 41
COIN_WIDTH = 45

IMAGE_BACKGROUND = os.path.join(os.getcwd(), "./cse210-final/assets/background.png")