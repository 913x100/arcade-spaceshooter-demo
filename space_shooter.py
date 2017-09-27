import arcade

from player import Player
from bullet import Bullet

SPRITE_SCALING = 0.5

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 500

BULLET_TIME = 0.25

class SpaceWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Space Shooter")
        
        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        self.wait_time = 0

    def setup(self):
        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.player = Player("images/player.png", SPRITE_SCALING)
        self.player.setup(SCREEN_WIDTH/2, 70, self.all_sprites_list, self.bullet_list)
        # self.player.center_x = SCREEN_WIDTH/2
        # self.player.center_y = 70
        self.all_sprites_list.append(self.player)


    def on_draw(self):
        arcade.start_render()

        # Draw all the sprites
        self.bullet_list.draw()
        self.player.draw()
    
    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)
    
    def update(self ,delta):
        self.all_sprites_list.update()
        self.wait_time += delta
        if self.wait_time > BULLET_TIME:
            self.player.shoot3()
            self.wait_time = 0
        
        for bullet in self.bullet_list:
            if bullet.bottom > SCREEN_HEIGHT or bullet.left < 0 or bullet.right > SCREEN_WIDTH:
                bullet.kill()

def main():
    window = SpaceWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()