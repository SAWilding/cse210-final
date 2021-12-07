from game.action import Action
from game.point import Point
from game import constants

class HandleOffScreenAction(Action):
    def __init__(self, cast, audio_service) -> None:
        self._cast = cast
        self._audio_service = audio_service

    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                if actor.get_name() == "Player":
                    player = actor
                    velocity_y = player.get_velocity().get_y()
                    if player.get_position().is_off_screen_bottom():
                        group.remove(player)
                        self._audio_service.play_sound(constants.SOUND_PLAYER_DEATH)
                    elif player.get_position().is_off_screen_top() and velocity_y < 0:
                        
                        player.set_velocity(Point(0, velocity_y * -1))
                if actor.get_name() == "Obstacle":
                    obstacle = actor
                    if obstacle.get_position().is_off_screen_x():
                        group.remove(obstacle)
                if actor.get_name() == "Coin":
                    coin = actor
                    if coin.get_position().is_off_screen_x():
                        group.remove(coin)