import arcade

from bullet import Bullet


SPRITE_SCALING = 0.5

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 500

MOVEMENT_SPEED = 5

class Player(arcade.Sprite):
    def setup(self, x, y, all_sprites_list, bullet_list):
        self.all_sprites_list = all_sprites_list
        self.bullet_list = bullet_list
        self.center_x = x
        self.center_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.change_x = 0

    def shoot1(self):
        bullet = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        # Position the bullet
        bullet.center_x = self.center_x
        bullet.bottom = self.top
        bullet.bullet_type = 1
        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)
        self.all_sprites_list.append(bullet)
    
    def shoot2(self):
        bullet1 = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        bullet2 = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        # Position the bullet
        bullet1.center_x = self.center_x+10
        bullet1.bottom = self.top
        bullet2.center_x = self.center_x-10
        bullet2.bottom = self.top
        bullet1.bullet_type = 1
        bullet2.bullet_type = 1

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet1)
        self.bullet_list.append(bullet2)
        self.all_sprites_list.append(bullet1)
        self.all_sprites_list.append(bullet2)

    def shoot3(self):
        bullet1 = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        bullet2 = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        bullet3 = Bullet("images/laserBlue01.png", SPRITE_SCALING * 1.5)
        # Position the bullet
        bullet1.center_x = self.center_x+15
        bullet1.bottom = self.top-10
        bullet2.center_x = self.center_x
        bullet2.bottom = self.top
        bullet3.center_x = self.center_x-15
        bullet3.bottom = self.top-10

        bullet1.angle = -20
        bullet3.angle = 20

        bullet1.bullet_type = 2
        bullet2.bullet_type = 1
        bullet3.bullet_type = 3

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet1)
        self.bullet_list.append(bullet2)
        self.bullet_list.append(bullet3)
        self.all_sprites_list.append(bullet1)
        self.all_sprites_list.append(bullet2)
        self.all_sprites_list.append(bullet3)
   
    def update(self):
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