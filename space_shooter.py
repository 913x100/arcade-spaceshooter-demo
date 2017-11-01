import random

import arcade
import pyglet
from pyglet.window import key

import enemies
from enemies import Enemyblack, Enemygreen, Enemyred
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

class Life(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.center_x = 20
        self.center_y = 80

class Item(arcade.Sprite):
    def __init__(self, filename, scale, type):
        super().__init__(filename, scale)
        self.center_x = random.randint(50, 450)
        self.center_y = SCREEN_HEIGHT + 20
        self.change_y = -1.5
        self.type = type

    def update(self):
        self.center_y += self.change_y
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
        self.atk_sound = arcade.sound.load_sound("sounds/expl6.wav")
        self.item = ["power", "speed"]
        self.item_delay = 0


    def setup(self):
        # Set up the player
        self.player = Player("images/player.png", SPRITE_SCALING, self.bullet_list)
        bg = Background("images/6.png", SPRITE_SCALING)
        bg.setup(SCREEN_WIDTH // 2 ,SCREEN_HEIGHT)
        self.background_list.append(bg)
        bg = Background("images/6.png", SPRITE_SCALING)
        bg.setup(SCREEN_WIDTH // 2 ,2*SCREEN_HEIGHT)
        self.background_list.append(bg)
        self.life = Life("images/playerLife1_orange.png", SPRITE_SCALING*1.5)

    def on_draw(self):
        arcade.start_render()

        # Draw background
        self.background_list.draw()
        # Draw all the sprites
        self.player.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.effect_list.draw()
        self.item_list.draw()
        self.life.draw()
        # Draw text
        output = f"Score: {self.score}"
        self.score_text = arcade.create_text(output, arcade.color.WHITE, 14)
        arcade.render_text(self.score_text, 10, 50)
        output = f"x{self.player.health}"
        self.health_text = arcade.create_text(output, arcade.color.WHITE, 14)
        arcade.render_text(self.health_text, 40, 73)
    
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

    def spawn_enemy(self, type, hp):
        enemy  = None
        if type == "black":
            enemy = Enemyblack("images/enemyBlack1.png", SPRITE_SCALING, hp, self.bullet_list)
        elif type == "red":
            enemy = Enemyred("images/enemyRed5.png", SPRITE_SCALING, hp, self.bullet_list)
        elif type == "green":
            enemy = Enemygreen("images/enemyGreen2.png", SPRITE_SCALING, hp, self.bullet_list)

        self.enemy_list.append(enemy)

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
            if self.frame % 50 == 0:
                self.spawn_enemy("red", 20)
        elif self.wave == 2:
            if self.frame % 50 == 0:
                self.spawn_enemy("red", 20)
            if self.frame % 80 == 0:
                self.spawn_enemy("black", 20)
        elif self.wave == 3:
            if self.frame % 50 == 0:
                self.spawn_enemy("red", 20)
            if self.frame % 80 == 0:
                self.spawn_enemy("black", 20)
            if self.frame % 100 == 0:
                self.spawn_enemy("green", 30)
        
        # Check bullet
        for bullet in self.bullet_list:
            if not bullet.isEnemy:
                player_hits = arcade.check_for_collision_with_list(bullet, self.enemy_list)
                if len(player_hits) > 0:
                    #bullet.kill()
                    for enemy in player_hits:   
                        arcade.sound.play_sound(self.atk_sound)
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
            item = None
            choice = random.choice(self.item)
            if choice == "power":
                item = Item("images/powerupBlue_bolt.png", SPRITE_SCALING * 1.5, "power")
            elif choice == "speed":
                item = Item("images/powerupBlue_star.png", SPRITE_SCALING * 1.5, "speed")
            self.item_list.append(item)
        player_hits = arcade.check_for_collision_with_list(self.player, self.item_list)
        for item in player_hits:
            if item.type == "power":
                self.player.power += 1
                if self.player.power > 3:
                    self.player.power = 3
            if item.type == "speed":
                self.item_delay = 300
                enemies.TIME_SPEED = 0.4
            item.kill()
        
        # Enemy hits
        enemy_hits = arcade.check_for_collision_with_list(self.player, self.enemy_list)
        if len(enemy_hits) > 0:
            for enemy in enemy_hits:
                enemy.kill()
            self.player.health -= 1
        enemy_hits = arcade.check_for_collision_with_list(self.player, self.bullet_list)
        for bullet in enemy_hits:
            if bullet.isEnemy:
                bullet.kill()
                self.player.health -= 1
        #self.frame += 1
        if self.item_delay > 0:
            self.item_delay -= 1
        if self.item_delay == 0:
            enemies.TIME_SPEED = 1

        # Score
        if self.wave == 1 and self.score >= 800:
            self.wave = 2
        elif self.wave == 2 and self.score >= 3000:
            self.wave = 3
        
        if self.player.health < 0:
            exit()


keys = pyglet.window.key.KeyStateHandler()

def main():
    window = SpaceWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.push_handlers(keys)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
