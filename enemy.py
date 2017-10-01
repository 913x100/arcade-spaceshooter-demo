import arcade 

from bullet import Bullet

SPRITE_SCALING = 0.5

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 500

MOVEMENT_SPEED = 5

BULLET_TIME = 0.25

class Enemy(arcade.Sprite):
    def setup(self, x, y, all_sprites_list):
        self.all_sprites_list = all_sprites_list
        self.bullet_list = arcade.SpriteList()
        self.center_x = x
        self.center_y = y
        self.change_x = 3
        self.change_y = 0
        self.wait_time = 0
        self.frame_count = 0

    def shoot(self):
        bullet = Bullet("images/circleRed01.png", SPRITE_SCALING * 1.5)
        bullet.setup(180, -3.5)
        # Position the bullet
        bullet.center_x = self.center_x
        bullet.top = self.bottom
        bullet.bullet_type = 1
        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def movement(self):
        if self.center_x > SCREEN_WIDTH - self.width - 50:
            self.change_x = -3
        elif self.center_x < self.width + 50:
            self.change_x = 3
            
        self.center_x += self.change_x

    def update(self, delta):
        self.center_x += self.change_x
        self.center_y += self.change_y

        self.bullet_list.update()

        self.wait_time += delta
        if self.wait_time > BULLET_TIME:
            self.shoot()
            self.wait_time = 0

        for bullet in self.bullet_list:         
            if bullet.bottom < 0 or bullet.left < 0 or bullet.right > SCREEN_WIDTH:
                bullet.kill()
            
        if self.center_x > SCREEN_WIDTH - self.width - 50:
            self.change_x = -3
        elif self.center_x < self.width + 50:
            self.change_x = 3