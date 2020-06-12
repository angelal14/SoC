"""
Project 1 for Summer of Code.

Player can walk around atrium to talk to characters & make drinks at Opus

"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Project 1"
SPEED = 10


class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_SALMON)
        #DARK_SALMON or LAVENDER_BLUE

        self.eyes = None
        self.arrows = None

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("OPUS MANIA       ",SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
                         arcade.color.WHITE, font_size=60,anchor_x="center")
        arcade.draw_text("Use the four arrow keys to move around and speak\n       to friends. "
                         "Walk into Opus to start working!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40,
                         arcade.color.WHITE,font_size=20,anchor_x="center")
        arcade.draw_text("Press any key to advance",SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 210,
                         arcade.color.WHITE, font_size=17, anchor_x="center")
        self.eyes = arcade.Sprite("game1_images/eyes.png",scale=0.12,center_x=620,center_y=445)
        self.arrows = arcade.Sprite("game1_images/arrows.png",scale=0.4,center_x=SCREEN_WIDTH / 2, center_y=SCREEN_HEIGHT / 2 - 70)

        self.eyes.draw()
        self.arrows.draw()

    def on_key_press(self, symbol, modifiers):
        """ When user presses key, enter next screen. """
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)


class MyGame(arcade.View):
    """
    Main application class.

    """

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.ANTIQUE_WHITE)
        # arcade.start_render()
        # arcade.finish_render()
        #Initialize sprite lists here, set them to None
        self.tree_list = None
        self.chair_list = None
        self.col_list = None
        self.table_list = None
        self.time = 0
        self.opus = None

        #characters
        # self.char_list = None
        self.char1 = None
        self.char2 = None
        self.char3 = None
        self.char4 = None
        self.char5 = None
        self.char6 = None

        #dialogue boxes
        self.speech1 = None
        self.speech2 = None
        self.speech3 = None
        self.speech4 = None

    def setup(self):
        #Create your sprites and sprite lists here

        self.tree_list = arcade.SpriteList()
        for y in range(185,600,150):
            tree = arcade.Sprite("game1_images/tree.png", scale=0.15,
                                  center_x=150, center_y=y)
            self.tree_list.append(tree)

        self.chair_list = arcade.SpriteList()
        for y in range(185,600,83):
            chair = arcade.Sprite("game1_images/armchair.png", scale=0.125,
                                  center_x = 60, center_y=y)
            self.chair_list.append(chair)

        self.table_list = arcade.SpriteList()
        for y in range(90, 600, 150):
            for x in range(290,650,120):
                table = arcade.Sprite("game1_images/table.png", scale=0.078,
                                      center_x=x, center_y=y)
                self.table_list.append(table)

        #characters
        self.char1 = arcade.Sprite("game1_images/Char1.png", scale=0.22,
                                   center_x=290,center_y=400)
        self.char2 = arcade.Sprite("game1_images/Char2.png", scale=0.22,
                                   center_x=410,center_y=400)
        self.char3 = arcade.Sprite("game1_images/Char3.png", scale=0.22,
                                   center_x=530,center_y=90)
        self.char4 = arcade.Sprite("game1_images/Char4.png", scale=0.22,
                                   center_x=530,center_y=240)
        self.char5 = arcade.Sprite("game1_images/Char5.png", scale=0.22,
                                   center_x=200,center_y=100)

        # self.char_list = arcade.SpriteList()
        # self.char_list.append(self.char1)
        # self.char_list.append(self.char2)
        # self.char_list.append(self.char3)
        # self.char_list.append(self.char4)

    def on_draw(self):
        arcade.start_render()
        #sprite lists
        self.tree_list.draw()
        self.chair_list.draw()
        self.table_list.draw()
        arcade.draw_rectangle_filled(745, 350, 95, 400, arcade.color.BANANA_MANIA)
        self.opus = arcade.Sprite("game1_images/opus.png",center_x=745,center_y=430,scale=0.1525)
        self.opus.draw()

        #characters
        self.char1.draw()
        self.char2.draw()
        self.char3.draw()
        self.char4.draw()
        self.char5.draw()

        #check collision -- THERE HAS TO BE A CLEANER WAY TO DO THIS??
        self.collide_char1 = arcade.check_for_collision(self.char5,self.char1)
        if self.collide_char1 == True:
            self.speech1 = arcade.Sprite("game1_images/dialogue.png",scale=0.07,
                          center_x=270,center_y=475)
            self.speech1.draw()
            arcade.draw_text("Have you\ntried Opus\ntoday?",270,450,arcade.color.BLACK,10,
                             anchor_x="center",rotation=20)

        self.collide_char2 = arcade.check_for_collision(self.char5,self.char2)
        if self.collide_char2 == True:
            self.speech2 = arcade.Sprite("game1_images/dialogue270.png",scale=0.07,
                                         center_x=460,center_y=465)
            self.speech2.draw()
            arcade.draw_text("Aren't\nyou late\n    for\n   work??",465,440,arcade.color.BLACK,10,
                             anchor_x="center")

        self.collide_char3 = arcade.check_for_collision(self.char5,self.char3)
        if self.collide_char3 == True:
            self.speech3 = arcade.Sprite("game1_images/dialogue90.png",scale=0.07,
                                         center_x=470,center_y=45)
            self.speech3.draw()
            arcade.draw_text("Have\nyou\ndone the\nhome-\nwork?",470,20,arcade.color.BLACK,9,
                             anchor_x="center")

        self.collide_char4 = arcade.check_for_collision(self.char5, self.char4)
        if self.collide_char4 == True:
            self.speech4 = arcade.Sprite("game1_images/dialogue270.png", scale=0.07,
                                         center_x=580, center_y=300)
            self.speech4.draw()
            arcade.draw_text("Have\nfun at\nwork!", 580, 300, arcade.color.BLACK, 10,
                             anchor_x="center")

        self.collide_opus = arcade.check_for_collision(self.char5,self.opus)
        if self.collide_opus == True:
            game_view = Instruction2View()
            self.window.show_view(game_view)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here (???)
        Normally, you'll call update() on the sprite lists that need it.
        """
        self.char5.update()
        self.time += delta_time

    def on_key_press(self, key, mod):
        if key == arcade.key.LEFT:
            self.char5.change_x = -SPEED
        elif key == arcade.key.RIGHT:
            self.char5.change_x = +SPEED
        elif key == arcade.key.DOWN:
            self.char5.change_y = -SPEED
        elif key == arcade.key.UP:
            self.char5.change_y = +SPEED

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.char5.change_x = 0
        elif key == arcade.key.RIGHT:
            self.char5.change_x = 0
        elif key == arcade.key.DOWN:
            self.char5.change_y = 0
        elif key == arcade.key.UP:
            self.char5.change_y = 0
            

class Instruction2View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_SALMON)
        # arcade.start_render()
        # arcade.finish_render()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("You are entering Opus\n            to work!",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30,
                         arcade.color.WHITE, font_size=40, anchor_x="center")
        arcade.draw_text("Click on the right ingredients to make the\n"
                         "                      desired drink!",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50,
                         arcade.color.WHITE, font_size=20,anchor_x="center")
        arcade.draw_text("Press any key to play", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 175,
                         arcade.color.WHITE, font_size=17, anchor_x="center")

    def on_key_press(self, symbol, modifiers):
        game_view = OpusView()
        # game_view.setup()
        self.window.show_view(game_view)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If user presses mouse button, start OPUS game. """
        game_view = OpusView()
        # game_view.setup()
        self.window.show_view(game_view)



class OpusView(arcade.View):

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BISQUE)
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, 520, 600, 100, arcade.color.LIGHT_STEEL_BLUE)

        #Initialize sprite lists here, set them to None
        self.instructions = None
        self.instructions_pos = (140,500)
        self.boss = None
        self.you = None
        self.wannabeyours = None

        #music lol
        # self.wannabeyours = .load_sound("game1_images/wannabeyours.mp3")
        # arcade.play_sound(self.wannabeyours)


    def setup(self):
        self.you = arcade.Sprite("game1_images/you.png", scale=0.45, center_x=720, center_y=100)
        self.boss = arcade.Sprite("game1_images/boss.png", scale=0.19, center_x=100, center_y=460)
        self.instructions = arcade.draw_text("Hey! Glad you could make it to work. We have\n"
                         "a busy day ahead of us!", self.instructions_pos[0], self.instructions_pos[1], arcade.color.BLACK, 18)

    def on_draw(self):
        arcade.start_render()
        self.you.draw()
        self.boss.draw()
        self.instructions.draw()
        arcade.draw_text("(Press Space to continue)", 320, 480, arcade.color.BLACK, 10)

    def on_update(self, delta_time):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.instructions = arcade.draw_text("TEST TRIGGERED", 400, 300, arcade.color.BLACK, 20)
            self.instructions.draw()


def main():
        """ Main method """

        window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        start_view = InstructionView()
        window.show_view(start_view)
        arcade.run()

        # game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # # arcade.set_background_color(arcade.color.ANTIQUE_WHITE)
        # # arcade.start_render()
        # # arcade.finish_render()
        # game.setup()
        # arcade.run()

if __name__ == "__main__":
        main()
