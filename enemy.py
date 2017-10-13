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

class Bulletblack(arcade.Sprite):
    def setup(self, x, bottom, BULLET_SPEED):
        self.center_x = x
        self.top = bottom
        self.angle = 180
        self.speed = BULLET_SPEED
        self.isEnemy = True
        
    def update(self):
        self.center_y += self.change_y
        
        if self.bottom < 0 or self.left < 0 or self.right > SCREEN_WIDTH:
                self.kill()

class Enemyblack(arcade.Sprite):
    def setup(self, x, y, bullet_list):
        self.bullet_list = bullet_list
        self.center_x = x
        self.center_y = y
        self.wait_time = 0
        self.target_y = randint(SCREEN_HEIGHT-200, SCREEN_HEIGHT-100)
        self.isShoot = False

    def shoot(self):
        bullet = Bulletblack("images/laserRed01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.center_y, -3)
        #bullet.change_x = math.sin(angle) * -3
        #bullet.change_y = math.cos(angle) * -3
        bullet.change_y = -3
        self.bullet_list.append(bullet)

    def update(self, delta):
        self.wait_time += 1
        #angle = math.atan2(self.center_x - self.player.center_x, self.center_y - self.player.center_y)
        #self.angle = math.degrees(-angle)
        if self.center_y > self.target_y:
            self.center_y -= 3
        if self.center_y <= self.target_y:
            self.isShoot = True

        if self.isShoot and self.wait_time % 40 == 0:
            self.shoot()
            #self.wait_time = 0
        
class Bulletgreen(arcade.Sprite):
    def setup(self, x, bottom, BULLET_SPEED):
        self.center_x = x
        self.top = bottom
        self.angle = 180
        self.speed = randint(2, 10) / 10
        self.isEnemy = True
        
    def update(self):
        self.center_y += self.change_y       
        if self.bottom < 0 or self.left < 0 or self.right > SCREEN_WIDTH:
                self.kill()

class Enemygreen(arcade.Sprite):
    def setup(self, x, y, bullet_list):
        self.bullet_list = bullet_list
        self.center_x = x
        self.center_y = y
        self.wait_time = 0
        self.target_y = randint(SCREEN_HEIGHT-200, SCREEN_HEIGHT-100)
        self.isShoot = False
        self.change_x = randint(-2, 2)
        '''
        if self.change_x == 0:
            self.change_x = -1
        else:
            self.change_x = 1
        '''


    def shoot(self):
        bullet = Bulletblack("images/circleYellow01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.center_y, -3)
        bullet.change_y = -3
        self.bullet_list.append(bullet)

    def update(self, delta):
        self.wait_time += delta
        self.center_x += self.change_x
        self.center_y -= 1

        if self.center_y < 0:
            self.kill()

        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = -self.change_x
        

        if self.wait_time > 0.8:
            self.shoot()
            self.wait_time = 0