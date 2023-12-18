from tito_engine import *
from custom_objs import *

player = TopDownCharacterController(
    3.0, path_to_img='assets/sprites/ball_blue_large.png',
    transform=Transform(Vec2(30, 360)),
    tag='Player'
)

zombie1 = Zombie(2.0, 20.0, 200.0, 'assets/sprites/ball_red_large.png',
                 Transform(Vec2(540, 360)))

TitoEngine(colour_fill=(200, 200, 200)).run([player, zombie1])
