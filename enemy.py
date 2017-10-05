import arcade 
import math
from random import randint

SPRITE_SCALING = 0.5

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 500

MOVEMENT_SPEED = 2

BULLET_TIME = 0.8

class Explosion(arcade.Sprite):
    def setup(self, x, y):
        self.center_x = x
        self.center_y = y

class Bullet(arcade.Sprite):
    def setup(self, x, y, BULLET_SPEED):
        self.center_x = x
        self.center_y = y
        self.angle = 180
        self.speed = BULLET_SPEED
        self.isEnemy = True
        
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        if self.bottom < 0 or self.left < 0 or self.right > SCREEN_WIDTH:
                self.kill()

class Enemy(arcade.Sprite):
    def setup(self, x, y, bullet_list):
        self.bullet_list = bullet_list
        self.center_x = x
        self.center_y = y
        self.wait_time = 0
        self.target_y = randint(SCREEN_HEIGHT-200, SCREEN_HEIGHT-100)
        self.isShoot = False

    def shoot(self):
        bullet = Bullet("images/circleRed01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.center_y, -3)
        #bullet.change_x = math.sin(angle) * -3
        #bullet.change_y = math.cos(angle) * -3
        bullet.change_y = -3
        self.bullet_list.append(bullet)

    def movement(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

    def update(self, delta):
        # self.movement()
        self.wait_time += delta
        #angle = math.atan2(self.center_x - self.player.center_x, self.center_y - self.player.center_y)
        #self.angle = math.degrees(-angle)
        if self.center_y > self.target_y:
            self.center_y -= 3
        if self.center_y <= self.target_y:
            self.isShoot = True

        if self.isShoot and self.wait_time > BULLET_TIME:
            self.shoot()
            self.wait_time = 0
        
        