import raylibpy
from PIL import Image
from game import constants
from game.director import Director
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
from game.handle_gravity_action import HandleGravityAction
from game.handle_score_action import HandleScoreAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.handle_obstacles_action import HandleObstaclesAction
from game.reset_game_action import ResetGameAction
from game.scoreboard import Scoreboard

 

def main():

    # create the cast {key: tag, value: list}
    cast = {}
    scoreboard = Scoreboard()
    cast["player"] = [Player()]

    cast["obstacles"] = [Obstacle()] 

    cast["scoreboard"] = [scoreboard]

    cast["coin"] = [] 
    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService() 


    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction(cast, input_service)
    control_actors_action = ControlActorsAction(input_service, audio_service)
    handle_collisions_action = HandleCollisionsAction(physics_service, audio_service)
    handle_gravity_action = HandleGravityAction(cast)
    handle_score_action = HandleScoreAction(cast, audio_service)
    handle_off_screen_action = HandleOffScreenAction(cast, audio_service)
    handle_obstacles_action = HandleObstaclesAction(cast)
    reset_game_action = ResetGameAction(cast, input_service)
    

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action, reset_game_action]
    script["update"] = [move_actors_action, 
                        handle_collisions_action, 
                        handle_gravity_action,
                        handle_off_screen_action, 
                        handle_obstacles_action]
    script["output"] = [draw_actors_action, handle_score_action]  



    # Start the game  
    output_service.open_window("Space Evader")
    audio_service.start_audio()
    
    director = Director(cast, script)
    director.start_game()
    audio_service.stop_audio()

if __name__ == "__main__":
    main()
