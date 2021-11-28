import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.player import Player
from game.obstacle import Obstacle
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.scoreboard import Scoreboard


def main():

    # create the cast {key: tag, value: list}
    cast = {}
    scoreboard = Scoreboard()
    cast["player"] = [Player()]
    # TODO: Create bricks here and add them to the list

    cast["obstacle"] = [Obstacle()]
    # TODO: Create a ball here and add it to the list

    # TODO: Create a paddle here and add it to the list
    cast["scoreboard"] = [scoreboard]

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction(cast)
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service, audio_service, scoreboard)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    
    director = Director(cast, script)
    director.start_game()
    audio_service.stop_audio()

if __name__ == "__main__":
    main()