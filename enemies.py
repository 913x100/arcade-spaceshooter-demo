import arcade 
import math
from random import randint

SPRITE_SCALING = 0.5

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 500

MOVEMENT_SPEED = 2
TIME_SPEED = 1
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
        self.center_y += self.change_y * TIME_SPEED
        
        if self.bottom < 0 or self.left < 0 or self.right > SCREEN_WIDTH:
                self.kill()

class Enemyblack(arcade.Sprite):
    def __init__(self, filename, scale, hp, bullet_list):
        super().__init__(filename, scale)
        self.bullet_list = bullet_list
        self.center_x = randint(40, 460)
        self.center_y = SCREEN_HEIGHT + 20
        self.wait_time = 0
        self.target_y = randint(SCREEN_HEIGHT-200, SCREEN_HEIGHT-100)
        self.isShoot = False
        self.health = hp
        self.score = 100

    def shoot(self):
        bullet = Bulletblack("images/circleRed01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.center_y, -3)
        bullet.change_y = -4
        self.bullet_list.append(bullet)

    def die(self):
        pass

    def update(self, delta):
        self.wait_time += 1
        if self.center_y > self.target_y:
            self.center_y -= 3 * TIME_SPEED
        if self.center_y <= self.target_y:
            self.isShoot = True

        if self.isShoot and self.wait_time % 40 == 0:
            self.shoot()
            #self.wait_time = 0
        
class Bulletgreen(arcade.Sprite):
    def setup(self, x, y):
        self.center_x = x
        self.center_y = y
        self.angle = 180
        self.speed = randint(2, 10) / 10
        self.isEnemy = True
        
    def update(self):
        self.center_x += self.change_x * TIME_SPEED
        self.center_y += self.change_y * TIME_SPEED  
         
        if self.bottom < 0 or self.left < 0 or self.right > SCREEN_WIDTH:
                self.kill()

class Enemygreen(arcade.Sprite):
    def __init__(self, filename, scale, hp, time_speed, bullet_list):
        super().__init__(filename, scale)
        self.bullet_list = bullet_list
        self.center_x = randint(40, 460)
        self.center_y = SCREEN_HEIGHT + 20
        self.change_y = 1
        self.wait_time = 0
        self.target_y = randint(SCREEN_HEIGHT-200, SCREEN_HEIGHT-100)
        self.isShoot = False
        self.health = hp
        self.score = 150
        if randint(0, 1) == 0:
            self.change_x = randint(1, 2)
        else:
            self.change_x = -randint(1, 2)

    def shoot(self):
        bullet = Bulletgreen("images/laserRed15.png", SPRITE_SCALING * 1.2)
        bullet.setup(self.center_x, self.bottom-10)
        bullet.change_y = -3
        bullet.change_x = 0
        self.bullet_list.append(bullet)

    def die(self):
        #Bullet1
        bullet = Bulletgreen("images/circleYellow01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.center_y)
        bullet.change_y = 5
        bullet.change_x = 0
        self.bullet_list.append(bullet)
        #Bullet2
        bullet = Bulletgreen("images/circleYellow01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.center_y)
        bullet.change_y = 3.5
        bullet.change_x = 3.5
        self.bullet_list.append(bullet)
        #Bullet3
        bullet = Bulletgreen("images/circleYellow01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.center_y)
        bullet.change_y = 0
        bullet.change_x = 5
        self.bullet_list.append(bullet)
        #Bullet4
        bullet = Bulletgreen("images/circleYellow01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.center_y)
        bullet.change_y = -3.5
        bullet.change_x = 3.5
        self.bullet_list.append(bullet)
        #Bullet5
        bullet = Bulletgreen("images/circleYellow01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.center_y)
        bullet.change_y = -5
        bullet.change_x = 0
        self.bullet_list.append(bullet)
        #Bullet6
        bullet = Bulletgreen("images/circleYellow01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.center_y)
        bullet.change_y = -3.5
        bullet.change_x = -3.5
        self.bullet_list.append(bullet)
        #Bullet7
        bullet = Bulletgreen("images/circleYellow01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.center_y)
        bullet.change_y = 0
        bullet.change_x = -5
        self.bullet_list.append(bullet)
        #Bullet8
        bullet = Bulletgreen("images/circleYellow01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.center_y)
        bullet.change_y = 3.5
        bullet.change_x = -3.5
        self.bullet_list.append(bullet)

    def update(self, delta):
        self.wait_time += 1
        self.center_x += self.change_x * TIME_SPEED
        self.center_y -= self.change_y * TIME_SPEED

        if self.center_y < 0:
            self.kill()

        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = -self.change_x
        

        if self.wait_time % 50 == 0:
            self.shoot()

class Enemyred(arcade.Sprite):
    def __init__(self, filename, scale, hp, bullet_list):
        super().__init__(filename, scale)
        self.bullet_list = bullet_list
        self.center_x = randint(30, 470)
        self.center_y = SCREEN_HEIGHT + 20
        self.change_y = 5
        self.health = hp
        self.score = 50
        
    def die(self):
        pass

    def update(self, delta):
        self.center_y -= self.change_y * TIME_SPEED

        if self.center_y < 0:
            self.kill()

        