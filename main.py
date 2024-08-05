import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong Game"


class Bar(arcade.Sprite):
    def __int__(self):
        super().__init__('bar png2.webp', 1.0)


class Game(arcade.Window):
    def __int__(self, width, height, title):
        super().__int__(width, height, title)
        self.bar = Bar()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()


if __name__ == '__main__':
    Window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
