from tito_engine import *
from custom_objs import *
import pygame as pg

player1 = BallController(
    3.0, path_to_img='assets/sprites/ball_blue_large.png',
    controls=(pg.K_w, pg.K_s, pg.K_a, pg.K_d),
    transform=Transform(Vec2(30, 360)),
    tag='Player 1'
)

player2 = BallController(
    3.0, path_to_img='assets/sprites/ball_red_large.png',
    controls=(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT),
    transform=Transform(Vec2(90, 360)),
    tag='Player 2'
)

TitoEngine(colour_fill=(255, 255, 255)).run([player1, player2])
