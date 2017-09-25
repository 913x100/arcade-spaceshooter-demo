import arcade

from game import World

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 500

class SpaceWindow(arcade.Window):
    def __init__(self):
        super().__init__(
            width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="Space Shooter")
        global world
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)
        self.world.draw()
    
    def on_key_press(self, key, modifiers):
        self.world.player.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.world.player.on_key_release(key, modifiers)


    def update(self, delta):
        self.world.player.update()

def main():
    SpaceWindow()
    arcade.run()

if __name__ == "__main__":
    main()