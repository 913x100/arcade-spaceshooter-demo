from random import randint

import arcade
import pyglet
from pyglet.window import key

from enemy import Enemyblack, Enemygreen, Enemyred
from player import Player

SPRITE_SCALING = 0.5

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 500

BULLET_TIME = 0.25

MOVEMENT_SPEED = 5

class Explosion(arcade.Sprite):
    def setup(self, x, y):
        self.center_x = x
        self.center_y = y

class Power(arcade.Sprite):
    def setup(self, x):
        self.center_x = x
        self.center_y = SCREEN_HEIGHT + 20
        self.type = "power"
    def update(self):
        self.center_y -= 1.5

        if self.center_y < 0:
            self.kill()


class Background(arcade.Sprite):
    def setup(self, x, top):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.center_x = x
        self.top = top
    
    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT

class SpaceWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Space Shooter")
        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        self.background = arcade.load_texture("images/6.png")
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.effect_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.item_list = arcade.SpriteList()
        self.gameOver = False
        self.wave = 1
        self.score = 0     
        self.isStart = False
        self.frame = 0
        self.spawn = 0
        self.wait_time = 0
        self.expl_time = 0
        self.level_text = None
        self.expl_sound = arcade.sound.load_sound("sounds/expl3.wav")

    def setup(self):
        # Set up the player
        self.player = Player("images/player.png", SPRITE_SCALING)
        self.player.setup(self.bullet_list)
        bg = Background("images/6.png", SPRITE_SCALING)
        bg.setup(SCREEN_WIDTH // 2 ,SCREEN_HEIGHT)
        self.background_list.append(bg)
        bg = Background("images/6.png", SPRITE_SCALING)
        bg.setup(SCREEN_WIDTH // 2 ,2*SCREEN_HEIGHT)
        self.background_list.append(bg)

    def on_draw(self):
        arcade.start_render()

        # Draw background
        #arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
        #                              SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.background_list.draw()
        # Draw all the sprites
        self.player.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.effect_list.draw()
        self.item_list.draw()
        # Draw text
        output = f"Level: {self.wave}"
        self.level_text = arcade.create_text(output, arcade.color.WHITE, 14)
        arcade.render_text(self.level_text, 10, 70)
        output = f"Score: {self.score}"
        self.score_text = arcade.create_text(output, arcade.color.WHITE, 14)
        arcade.render_text(self.score_text, 10, 50)
    
    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)
    
    def player_controller(self):
        if keys[key.LEFT]:
            self.player.center_x -= MOVEMENT_SPEED
        if keys[key.RIGHT]:
            self.player.center_x += MOVEMENT_SPEED
        if keys[key.UP]:
            self.player.center_y += MOVEMENT_SPEED
        if keys[key.DOWN]:
            self.player.center_y -= MOVEMENT_SPEED

    def update(self ,delta):
        # All object update 
        self.background_list.update()
        self.item_list.update()
        self.player_controller()

        self.player.update(delta)
        self.bullet_list.update()
        for enemy in self.enemy_list:
                enemy.update(delta)
        
        self.frame += 1

        if self.wave == 1:
            time_spawn = randint(40, 80)
            random_list = [60, 100, 140, 180, 220, 260, 300, 340, 380, 420, 460]
            if self.frame % 60 == 0 and len(self.enemy_list) < 15:
                #enemy = Enemyblack("images/enemyBlack1.png", SPRITE_SCALING)
                enemy = Enemyred("images/enemyRed5.png", SPRITE_SCALING)
                spawn_x = randint(0, len(random_list)-1)
                enemy.setup(random_list[spawn_x], SCREEN_HEIGHT + 20, 20, self.bullet_list)
                self.enemy_list.append(enemy)
                if self.score >= 800:
                    self.wave += 1
        elif self.wave == 2:
            if self.frame % 80 == 0 and len(self.enemy_list) < 15:
                enemy = Enemyblack("images/enemyBlack1.png", SPRITE_SCALING)
                spawn_x = randint(50, 460)
                enemy.setup(spawn_x, SCREEN_HEIGHT + 20, 30, self.bullet_list)
                self.enemy_list.append(enemy)
                if self.score >= 2000:
                    self.wave += 1
        elif self.wave == 3:
            if self.frame % 100 == 0 and len(self.enemy_list) < 15:
                enemy = Enemygreen("images/enemyGreen2.png", SPRITE_SCALING)
                spawn_x = randint(50, 460)
                enemy.setup(spawn_x, SCREEN_HEIGHT + 20, 30, self.bullet_list)
                self.enemy_list.append(enemy)
                if self.score >= 3500:
                    self.wave += 1
        elif  self.wave == 4:
            random_list = [60, 100, 140, 180, 220, 260, 300, 340, 380, 420, 460]
            if self.frame % 60 == 0 and len(self.enemy_list) < 25:
                #enemy = Enemyblack("images/enemyBlack1.png", SPRITE_SCALING)
                enemy = Enemyred("images/enemyRed5.png", SPRITE_SCALING)
                spawn_x = randint(0, len(random_list)-1)
                enemy.setup(random_list[spawn_x], SCREEN_HEIGHT + 20, 20, self.bullet_list)
                self.enemy_list.append(enemy)
            if self.frame % 80 == 0 and len(self.enemy_list) < 25:
                enemy = Enemyblack("images/enemyBlack1.png", SPRITE_SCALING)
                spawn_x = randint(50, 460)
                enemy.setup(spawn_x, SCREEN_HEIGHT + 20, 30, self.bullet_list)
                self.enemy_list.append(enemy)
            if self.frame % 100 == 0 and len(self.enemy_list) < 25:
                enemy = Enemygreen("images/enemyGreen2.png", SPRITE_SCALING)
                spawn_x = randint(50, 460)
                enemy.setup(spawn_x, SCREEN_HEIGHT + 20, 30, self.bullet_list)
                self.enemy_list.append(enemy)

        
        # Check bullet
        for bullet in self.bullet_list:
            if not bullet.isEnemy:
                player_hits = arcade.check_for_collision_with_list(bullet, self.enemy_list)
                if len(player_hits) > 0:
                    #bullet.kill()
                    for enemy in player_hits:   
                        enemy.health -= bullet.damage
                        if enemy.health <= 0:    
                            self.score += enemy.score   
                            arcade.sound.play_sound(self.expl_sound)           
                            enemy.die()
                            enemy.kill()
                            for i in range(0, 8):
                                expl = Explosion("images/regularExplosion0"+str(i)+".png", SPRITE_SCALING)
                                expl.setup(enemy.center_x, enemy.center_y)
                                self.effect_list.append(expl)
                    bullet.kill()

        self.expl_time += delta
        if self.expl_time > 0.03 :
            self.expl_time = 0
            if len(self.effect_list) > 0:
                self.effect_list[0].kill()
        
        # Check power
        if self.frame % 1000 == 0:
            power = Power("images/powerupBlue_bolt.png", SPRITE_SCALING * 1.5)
            power.setup(randint(50, 460))
            self.item_list.append(power)
        player_hits = arcade.check_for_collision_with_list(self.player, self.item_list)
        for item in player_hits:
            if item.type == "power":
                self.player.power += 1
                if self.player.power > 3:
                    self.player.power = 3
            item.kill()
        
        #self.frame += 1
        

keys = pyglet.window.key.KeyStateHandler()

def main():
    window = SpaceWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.push_handlers(keys)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
