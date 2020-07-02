"""
16. Imagine you are creating a Super Mario game. You need to define
a class to represent Mario. What would it look like? If you aren't
familiar with SuperMario, use your own favorite video or board game
to model a player.
"""


class Mario:
    state = ["FALLING", "JUMPING", "STANDING", "RUNNING", "GROWING", "DEAD"]
    world = None
    b2body = None

    mario_stand = None
    big_mario_stand = None
    big_mario_jump = None
    mario_dead = None
    big_mario_run = None
    grow_mario = None

    mario_run = None
    mario_jump = None

    running_right = None
    state_timer = None
    mario_is_big = None
    mario_is_dead = None

    def refresh_frames(self):
        pass

    def start_animation(self):
        pass

    def move_mario(self):
        pass

    def jump_mario(self):
        pass

    def spawn_mario(self):
        pass

    def grow_mario(self):
        pass

    def end_animation(self):
        pass
