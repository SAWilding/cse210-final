from random import vonmisesvariate
from game.action import Action
from game import constants
from game.point import Point

class ControlActorsAction(Action):
    def __init__(self, input_service, audio_service) -> None:
        self._input_service = input_service
        self._audio_service = audio_service
    def execute(self, cast):
            for actor in cast["player"]:
                player = actor
                if self._input_service.is_space_pressed():
                    self._audio_service.play_sound(constants.SOUND_JUMP)
                    velocity = player.get_velocity()
                    velocity_y = velocity.get_y()
                    
        
                    velocity_y -= constants.PLAYER_JUMP
                    player.set_velocity(Point(0, velocity_y))

