import arcade

SPRITE_SCALING = 0.5

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 500

MOVEMENT_SPEED = 5

BULLET_TIME = 0.25
class Bullet(arcade.Sprite):
    def setup(self, x, bottom, BULLET_TYPE, BULLET_SPEED):
        self.center_x = x
        self.bottom = bottom
        self.bullet_type = BULLET_TYPE
        self.speed = BULLET_SPEED
        self.isEnemy = False
        self.damage = 10
        
    def update(self):
        if self.bullet_type == 1:
            self.center_y += self.speed
        elif self.bullet_type == 2:
            self.center_x += self.speed-5
            self.center_y += self.speed
        elif self.bullet_type == 3:
            self.center_x -= self.speed-5
            self.center_y += self.speed

        if self.bottom > SCREEN_HEIGHT or self.left < 0 or self.right > SCREEN_WIDTH:
                self.kill()


class Player(arcade.Sprite):

    def __init__(self, filename, scale, bullet_list):
        super().__init__(filename, scale)
        self.bullet_list = bullet_list
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 70
        self.wait_time = 0
        self.power = 1
        self.health = 5
        self.isshot = False
        self.shoot_sound = arcade.sound.load_sound("sounds/pew.wav")        

    def shoot1(self):
        bullet = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.top, 1, 6.5)
        self.bullet_list.append(bullet)
    
    def shoot2(self):
        bullet = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x-10, self.top, 1, 6.5)
        self.bullet_list.append(bullet)
        bullet = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x+10, self.top, 1, 6.5)
        self.bullet_list.append(bullet)
    
    def shoot3(self):
        bullet = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x+5, self.top, 2, 6.5)
        bullet.angle = -15
        self.bullet_list.append(bullet)
        bullet = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x, self.top, 1, 6.5)
        self.bullet_list.append(bullet)
        bullet = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        bullet.setup(self.center_x-5, self.top, 3, 6.5)
        bullet.angle = 15
        self.bullet_list.append(bullet)
        

    def movement(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.isshot = True
        
    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.isshot = False
        
    def update(self, delta):
        self.movement()

        self.wait_time += delta
        if self.wait_time > BULLET_TIME:
            if self.isshot: 
                arcade.sound.play_sound(self.shoot_sound)
                if self.power == 1:
                    self.shoot1()
                elif self.power == 2:
                    self.shoot2()
                elif self.power == 3:
                    self.shoot3()
                    pass
            self.wait_time = 0
