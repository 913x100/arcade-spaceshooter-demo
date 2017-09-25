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
    
def main():
    SpaceWindow()
    arcade.run()

if __name__ == "__main__":
    main()