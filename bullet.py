import arcade 

class Bullet(arcade.Sprite):
    def setup(self, angle, BULLET_SPEED):
        self.angle = angle
        self.speed = BULLET_SPEED
        
    def update(self):
        if self.bullet_type == 1:
            self.center_y += self.speed
        elif self.bullet_type == 2:
            self.center_x += self.speed-5
            self.center_y += self.speed
        elif self.bullet_type == 3:
            self.center_x -= self.speed-5
            self.center_y += self.speed

        
    