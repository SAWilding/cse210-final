from game.action import Action
from game import constants
from game.point import Point


class HandleCollisionsAction(Action):
    def __init__(self, physics_service, audio_service) -> None:
        self._physics_service = physics_service
        self._audio_service = audio_service
    def execute(self, cast):
        obstacles = []
        player_exists = False
        for group in cast.values():
            for actor in group:
                if actor.get_name() == "Player":
                    player = actor
                    player_group = group
                    player_exists = True
                if actor.get_name() == "Obstacle":
                    obstacle = actor
                    obstacles.append(obstacle)
        if player_exists:
            for obstacle in obstacles:
                if self._physics_service.is_collision(player, obstacle):
                    player_group.remove(player)
                    self._audio_service.play_sound(constants.SOUND_PLAYER_DEATH)