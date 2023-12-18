from tito_engine import Sprite, Transform, InputManager, Vec2
import pygame as pg


class BallController(Sprite):
    def __init__(self, move_speed: float, path_to_img: str, controls, transform: Transform = Transform(), enabled=True, tag: str = ''):
        self._move_speed = move_speed
        self.controls = controls
        super().__init__(path_to_img, transform, enabled, tag)

    def update(self, world):
        self.move()
        super().update(world)

    def move(self):
        # Get the input from WSAD Keys, make a vector from them and update the objects's position
        x_input, y_input = InputManager.get_axis(
            self.controls[2], self.controls[3]), InputManager.get_axis(self.controls[0], self.controls[1])

        self.transform.position += Vec2(x_input,
                                        y_input).normalize() * self._move_speed

