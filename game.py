import arcade

from player import Player

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player = Player(50, 70)

    def update(self, delta):
        self.player.update()

    def draw(self):
        self.player.draw()