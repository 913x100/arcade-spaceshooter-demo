import arcade

from player import Player
from bullet import Bullet
from enemy import Enemy

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
        self.frame_count = 0

    def setup(self):
        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        # Set up the player
        self.player = Player("images/player.png", SPRITE_SCALING)
        self.player.setup(SCREEN_WIDTH/2, 70, self.all_sprites_list, self.enemy_list)
        self.all_sprites_list.append(self.player)

        # Set up the enemy 
        self.enemy = Enemy("images/enemyBlack1.png", SPRITE_SCALING)
        self.enemy.setup(120, SCREEN_HEIGHT - self.enemy.height, self.all_sprites_list)
        self.all_sprites_list.append(self.enemy)
        self.enemy_list.append(self.enemy)

        self.enemy = Enemy("images/enemyBlack1.png", SPRITE_SCALING)
        self.enemy.setup(SCREEN_WIDTH-120, SCREEN_HEIGHT - self.enemy.height, self.all_sprites_list)
        self.all_sprites_list.append(self.enemy)
        self.enemy_list.append(self.enemy)


    def on_draw(self):
        arcade.start_render()

        # Draw all the sprites
        self.player.bullet_list.draw()
        self.player.draw()
        for enemy in self.enemy_list:
            enemy.bullet_list.draw()
        self.enemy_list.draw()
    
    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)
    
    def update(self ,delta):
        self.player.update(delta)
        self.frame_count += 1

        for enemy in self.enemy_list:
                enemy.update(delta)

def main():
    window = SpaceWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()