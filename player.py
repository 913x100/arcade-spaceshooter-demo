import arcade

SPRITE_SCALING = 0.5

class Player():
    def __init__(self, ORIGIN_X, ORIGIN_Y):
        self.player_sprite = arcade.Sprite("images/player.png", SPRITE_SCALING)
        self.player_sprite.center_x = ORIGIN_X
        self.player_sprite.center_y = ORIGIN_Y
    
    def draw(self):
        self.player_sprite.draw()