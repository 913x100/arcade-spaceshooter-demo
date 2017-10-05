import arcade

from random import randint

from player import Player
from enemy import Enemy

SPRITE_SCALING = 0.5

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 500

BULLET_TIME = 0.25

class Explosion(arcade.Sprite):
    def setup(self, x, y):
        self.center_x = x
        self.center_y = y


class SpaceWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Space Shooter")
        
        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        self.background = arcade.load_texture("images/background.png")
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.effect_list = arcade.SpriteList()
        self.gameOver = False
        self.wave = 1
        self.isStart = False
        self.frame = 0
        self.spawn = 0
        self.wait_time = 0
        self.expl_time = 0

    def setup(self):
        # Set up the player
        self.player = Player("images/player.png", SPRITE_SCALING)
        self.player.setup(self.bullet_list)


    def on_draw(self):
        arcade.start_render()

        # Draw back ground
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        # Draw all the sprites
        self.player.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.effect_list.draw()
    
    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)
    
    def update(self ,delta):
        # All object update
        self.player.update(delta)
        self.bullet_list.update()
        for enemy in self.enemy_list:
                enemy.update(delta)

        if self.wave == 1:
            time_spawn = randint(40, 80)
            random_list = [60, 100, 140, 180, 220, 260, 300, 340, 380, 420, 460]
            if self.frame % 100 == 0 and len(self.enemy_list) < 5:
                enemy = Enemy("images/enemyBlack1.png", SPRITE_SCALING)
                spawn_x = randint(0, len(random_list)-1)
                enemy.setup(random_list[spawn_x], SCREEN_HEIGHT + 20, self.bullet_list)
                random_list.remove(random_list[spawn_x])
                self.enemy_list.append(enemy)
                self.spawn += 1

        # Check bullet
        for bullet in self.bullet_list:
            if not bullet.isEnemy:
                player_hits = arcade.check_for_collision_with_list(bullet, self.enemy_list)
                if len(player_hits) > 0:
                    bullet.kill()
                    for enemy in player_hits:
                        enemy.kill()
                        for i in range(0, 8):
                            expl = Explosion("images/regularExplosion0"+str(i)+".png", SPRITE_SCALING)
                            expl.setup(enemy.center_x, enemy.center_y)
                            self.effect_list.append(expl)

        self.expl_time += delta
        if self.expl_time > 0.03 :
            self.expl_time = 0
            if len(self.effect_list) > 0:
                self.effect_list[0].kill()
        
        self.frame += 1

def main():
    window = SpaceWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()