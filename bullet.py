import arcade 

BULLET_SPEED = 6.5


class Bullet(arcade.Sprite):
    def update(self):
        if self.bullet_type == 1:
            self.center_y += BULLET_SPEED
        elif self.bullet_type == 2:
            self.center_x += BULLET_SPEED-4
            self.center_y += BULLET_SPEED
        elif self.bullet_type == 3:
            self.center_x -= BULLET_SPEED-4
            self.center_y += BULLET_SPEED

        
    