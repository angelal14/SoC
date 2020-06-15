"""
Project 1 for Summer of Code.

Player can walk around atrium to talk to characters & make drinks at Opus

"""
import arcade
import random

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
        arcade.draw_text("Use the four arrow keys to move around and speak\n to friends. "
                         "Walk into Opus to start working!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40,
                         arcade.color.WHITE,font_size=20,align="center",anchor_x="center")
        arcade.draw_text("Press any key to advance",SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 210,
                         arcade.color.WHITE, font_size=17, align="center",anchor_x="center")
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
        if arcade.check_for_collision(self.char5,self.char1):
            self.speech1 = arcade.Sprite("game1_images/dialogue.png",scale=0.07,
                          center_x=270,center_y=475)
            self.speech1.draw()
            arcade.draw_text("Have you\ntried Opus\ntoday?",270,450,arcade.color.BLACK,10,
                             anchor_x="center",rotation=20)

        if arcade.check_for_collision(self.char5,self.char2):
            self.speech2 = arcade.Sprite("game1_images/dialogue270.png",scale=0.07,
                                         center_x=460,center_y=465)
            self.speech2.draw()
            arcade.draw_text("Aren't\nyou late\n    for\n   work??",465,440,arcade.color.BLACK,10,
                             anchor_x="center")

        if arcade.check_for_collision(self.char5,self.char3):
            self.speech3 = arcade.Sprite("game1_images/dialogue90.png",scale=0.07,
                                         center_x=470,center_y=45)
            self.speech3.draw()
            arcade.draw_text("Have\nyou\ndone the\nhome-\nwork?",470,20,arcade.color.BLACK,9,
                             anchor_x="center")

        if arcade.check_for_collision(self.char5, self.char4):
            self.speech4 = arcade.Sprite("game1_images/dialogue270.png", scale=0.07,
                                         center_x=580, center_y=300)
            self.speech4.draw()
            arcade.draw_text("Have\nfun at\nwork!", 580, 280, arcade.color.BLACK, 10,
                             anchor_x="center")

        if arcade.check_for_collision(self.char5,self.opus):
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

    #DELETE THIS LATER... JUST FOR TESTING USE
    def on_key_press(self, symbol, modifiers):
            game_view = Instruction2View()
            self.window.show_view(game_view)


class Instruction2View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_SALMON)
        # arcade.start_render()
        # arcade.finish_render()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("You are entering Opus\nto work!",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30,
                         arcade.color.WHITE, font_size=40, align="center",anchor_x="center")
        arcade.draw_text("Click on the right ingredients to make the\n desired drink!",
                         SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50,
                         arcade.color.WHITE, font_size=20,align="center",anchor_x="center")
        arcade.draw_text("Press any key to play", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 175,
                         arcade.color.WHITE, font_size=17, anchor_x="center")

    def on_key_press(self, symbol, modifiers):
        game_view = OpusView()
        game_view.setup()
        self.window.show_view(game_view)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If user presses mouse button, start OPUS game. """
        game_view = OpusView()
        game_view.setup()
        self.window.show_view(game_view)



class OpusView(arcade.View):

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BISQUE)

        self.instructions = "Hey! Glad you could make it to work. We have\na busy day ahead of us!"
        self.press_space = "(Press SPACE to continue)"
        self.pos_x = SCREEN_WIDTH / 2
        self.pos_y = 525
        self.you = None
        self.boss = None
        self.wannabeyours = None

        self.space_count = 0
        self.cup = None
        self.time = 35

        #stations
        self.iced_tea = None
        self.coffee_station = None
        self.milk_station = None
        self.syrup_station = None
        self.ice_station = None
        self.whipped_cream = None
        self.trash = None

        self.game_start = False
        self.drink = None

        #logic check
        self.syrup_done = False
        self.ice_done = False
        self.coffee_done = False
        self.complete = False
        self.order_num = 1
        self.cup_empty = True
        self.failed = False
        self.levels_completed = 0
        self.level = 1

    def setup(self):
        self.you = arcade.Sprite("game1_images/you.png", scale=0.45, center_x=500, center_y=305)
        self.boss = arcade.Sprite("game1_images/boss.png", scale=0.19, center_x=100, center_y=460)
        self.cup = arcade.Sprite("game1_images/cup.png",scale=0.18,center_x=400,center_y=305)

        #stations
        self.trash = arcade.Sprite("game1_images/trash.png",scale=0.15,center_x=730,center_y=400)
        self.coffee_station = arcade.Sprite("game1_images/coffee_station.jpg",scale=0.15,center_x=80,center_y=250)
        self.milk_station = arcade.Sprite("game1_images/milk.png",scale=0.08,center_x=80,center_y=80)
        self.syrup_station = arcade.Sprite("game1_images/syrup_station.png",scale=0.15,center_x=370,center_y=70)
        self.ice_station = arcade.Sprite("game1_images/ice.jpg",scale=0.15,center_x=490,center_y=70)
        self.whipped_cream = arcade.Sprite("game1_images/whipped_cream.png",scale=0.15,center_x=580,center_y=70)
        self.iced_tea = arcade.Sprite("game1_images/iced_tea.png",scale=0.15,center_x=730,center_y=70)


    def on_draw(self):
        arcade.start_render()
        self.boss.draw()

        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, 520, 600, 100, arcade.color.LIGHT_STEEL_BLUE)
        arcade.draw_text(self.instructions, self.pos_x, self.pos_y, arcade.color.BLACK, 16,font_name="Comic Sans MS",
                         anchor_x="center",anchor_y="center",align="center")
        arcade.draw_text(self.press_space, 320, 480, arcade.color.BLACK, 10)

        if self.space_count > 0:
            self.cup.draw()
        if self.game_start == True:
            arcade.draw_text(f"Time remaining: {self.time:.0f}", 400,456,arcade.color.BLACK,anchor_x="center",
                             anchor_y="center",align="center",font_name="Comic Sans MS",font_size=15)

        self.iced_tea.draw()
        self.coffee_station.draw()
        self.milk_station.draw()
        self.syrup_station.draw()
        self.ice_station.draw()
        self.whipped_cream.draw()
        self.trash.draw()
        if self.space_count > 3:
          self.you.draw()

        #MAKING DRINKS!!!
        if self.drink == "Iced Coffee":
            if arcade.check_for_collision(self.you,self.ice_station) and self.cup_empty == True:
                self.cup = arcade.Sprite("game1_images/ice_cup.png",scale=0.18,center_x=400,center_y=305)
                self.ice_done = True
                self.cup_empty = False
            if arcade.check_for_collision(self.you, self.coffee_station) and self.ice_done == True:
                self.cup = arcade.Sprite("game1_images/ice_coffee1.png",scale=0.18,center_x=400,center_y=305)
                self.coffee_done = True
                self.ice_done = False
            if arcade.check_for_collision(self.you, self.milk_station) and self.coffee_done == True:
                self.cup = arcade.Sprite("game1_images/ice_coffee2.png",scale=0.18,center_x=400,center_y=305)
                self.coffee_done = False
                self.complete = True
            self.check_complete()

        elif self.drink == "Iced Tea":
            if arcade.check_for_collision(self.you,self.ice_station) and self.cup_empty == True:
                self.cup = arcade.Sprite("game1_images/ice_cup.png",scale=0.18,center_x=400,center_y=305)
                self.ice_done = True
                self.cup_empty = False
            if arcade.check_for_collision(self.you,self.iced_tea) and self.ice_done == True:
                #make a popup asking for selection of flavors, then set self.cup = respective flavor
                self.cup = arcade.Sprite("game1_images/guava_white_tea.png",scale=0.18,center_x=400,center_y=305)
                self.ice_done = False
                self.complete = True
                pass
            self.check_complete()

        elif self.drink == "Frappuccino":
            if arcade.check_for_collision(self.you,self.syrup_station) and self.cup_empty == True:
                self.cup = arcade.Sprite("game1_images/syrup.png", scale=0.18, center_x=400, center_y=305)
                self.syrup_done = True
                self.cup_empty = False
            if arcade.check_for_collision(self.you,self.ice_station) and self.syrup_done == True:
                self.cup = arcade.Sprite("game1_images/syrup_ice.png", scale=0.18, center_x=400, center_y=305)
                self.ice_done = True
                self.syrup_done = False
            if arcade.check_for_collision(self.you,self.coffee_station) and self.ice_done == True:
                self.cup = arcade.Sprite("game1_images/frap_ice.png",scale=0.18,center_x=400,center_y=305)
                self.coffee_done = True
                self.ice_done = False
            if arcade.check_for_collision(self.you,self.whipped_cream) and self.coffee_done == True:
                self.cup = arcade.Sprite("game1_images/frap_cream.png",scale=0.18,center_x=400,center_y=305)
                self.coffee_done = False
                self.complete = True
            self.check_complete()

        #trash can to clear
        if arcade.check_for_collision(self.you,self.trash):
            #start fresh
            self.syrup_done = False
            self.ice_done = False
            self.coffee_done = False
            self.complete = False
            self.cup_empty = True
            self.cup = arcade.Sprite("game1_images/cup.png", scale=0.18, center_x=400, center_y=305)


        #show level
        arcade.draw_text(f"Level: {self.level}",500,100,arcade.color.BLACK,anchor_x="center",
                         anchor_y="center",align="center",font_name="Comic Sans MS",font_size=15)

        #end failure popup
        if self.failed == True:
            arcade.draw_rectangle_filled(400,300,200,100,arcade.color.BANANA_MANIA)
            arcade.draw_text("You failed!",400,300,arcade.color.BLACK,20,anchor_x="center",
                             anchor_y="center",align="center")

    def on_update(self, delta_time):
        self.you.update()
        if self.game_start == True:
            if self.time > 0:
                self.time -= delta_time
            self.order = ["Iced Coffee!\nYou need: ice, coffee, and milk.",
                      "Frappuccino!\nYou need: syrup, ice, espresso, and whipped cream.",
                      "Matcha Iced Tea!\nYou need: ice and a matcha flavor shot.",
                      "Passion Tango Iced Tea!\nYou need: ice and a passion tango flavor shot.",
                      "Guava White Iced Tea Lemonade!\nYou need: ice and a guava white flavor shot."]

            self.instructions = f"Order {self.order_num}: {self.order[(self.order_num) // len(self.order)]}"
            self.drink_check()

            if self.time < 0:
                self.failed = True

    def check_complete(self):
        if arcade.check_for_collision(self.you, self.boss) and self.complete == True:
            self.levels_completed += 1
            self.complete = False
            self.order_num += 1
            self.cup = arcade.Sprite("game1_images/cup.png", scale=0.18, center_x=400, center_y=305)
            self.cup_empty = True
            if self.levels_completed <= 2:
                self.time = 35
                self.level = 1
            elif self.levels_completed > 2 and self.levels_completed <= 5:
                self.time = 20
                self.level = 2
            elif self.levels_completed > 5 and self.levels_completed <= 10:
                self.time = 15
                self.level = 3
            elif self.levels_completed > 10:
                self.time = 10
                self.level = 4


    def drink_check(self):
        if "Iced Coffee" in self.instructions:
            self.drink = "Iced Coffee"
        elif "Iced Tea" in self.instructions:
            self.drink = "Iced Tea"
        elif "Frappuccino" in self.instructions:
            self.drink = "Frappuccino"

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.space_count == 0:
            self.press_space = ""
            self.instructions = "I'll handle the customer transactions and tell\n" \
                                "you what drinks to make. This cup icon will\n" \
                                "indicate what ingredients you've added."
            self.space_count += 1
        elif key == arcade.key.SPACE and self.space_count == 1:
            self.instructions = "If you mess up, you can start over by\n" \
                                "using the trash can. Be cognizant of how\n" \
                                "long you take!"
            self.space_count += 1
        elif key == arcade.key.SPACE and self.space_count == 2:
            self.instructions = "...It's finals week, so students won't like\n" \
                                "to wait too long. Ready? Good luck!"
            self.space_count += 1
        elif key == arcade.key.SPACE and self.space_count == 3:
            self.game_start = True
            self.space_count += 1


        #control player movement
        if self.space_count > 0:
            if key == arcade.key.LEFT:
                self.you.change_x = -SPEED
            elif key == arcade.key.RIGHT:
                self.you.change_x = +SPEED
            elif key == arcade.key.DOWN:
                self.you.change_y = -SPEED
            elif key == arcade.key.UP:
                self.you.change_y = +SPEED

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.you.change_x = 0
        elif key == arcade.key.RIGHT:
            self.you.change_x = 0
        elif key == arcade.key.DOWN:
            self.you.change_y = 0
        elif key == arcade.key.UP:
            self.you.change_y = 0


def main():
        """ Main method """

        """ This is the actual game main() """
        window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        start_view = InstructionView()
        window.show_view(start_view)
        arcade.run()

        """ This is the original game main() that I wanted to save. """
        # game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # # arcade.set_background_color(arcade.color.ANTIQUE_WHITE)
        # # arcade.start_render()
        # # arcade.finish_render()
        # game.setup()
        # arcade.run()

if __name__ == "__main__":
        main()
