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


class Opening(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_SALMON)
        #DARK_SALMON or LAVENDER_BLUE

        self.eyes = None
        self.arrows = None

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("OPUS MANIA",340, SCREEN_HEIGHT / 2 + 100, arcade.color.WHITE, font_size=60,
                         anchor_x="center",align="center",font_name="Comic Sans MS")
        arcade.draw_text("Use the four arrow keys to move around and speak\n to friends. "
                         "Walk into Opus to start working!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40,
                         arcade.color.WHITE,font_size=20,align="center",anchor_x="center",font_name="Comic Sans MS")
        arcade.draw_text("Press any key to advance",SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 210,
                         arcade.color.WHITE, font_size=17, align="center",anchor_x="center",font_name="Comic Sans MS")
        self.eyes = arcade.Sprite("game1_images/eyes.png",scale=0.12,center_x=660,center_y=445)
        self.arrows = arcade.Sprite("game1_images/arrows.png",scale=0.4,center_x=SCREEN_WIDTH / 2, center_y=SCREEN_HEIGHT / 2 - 70)

        self.eyes.draw()
        self.arrows.draw()

    def on_key_press(self, symbol, modifiers):
        """ When user presses key, enter next screen. """
        atrium_view = MyGame()
        # atrium_view.setup()
        # self.window.show_view(atrium_view)
        game_view = OpusView(atrium_view)
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
            pause = PauseView(self)
            self.window.show_view(pause)


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


class PauseView(arcade.View):
    def __init__(self, atrium_view):
        super().__init__()
        """ atrium_view is flawed because the character got too far into the OPUS sign that
        every time I escape here, it'll re-enter the atrium screen already on top of OPUS so 
        it'll perpetually stay paused. smh. """
        self.atrium_view = atrium_view
        self.you = None
        self.escape = False

    def on_show(self):
        arcade.set_background_color(arcade.color.ANTIQUE_WHITE)

    def on_draw(self):
        arcade.start_render()

        #redraw sprite lists
        self.atrium_view.tree_list.draw()
        self.atrium_view.chair_list.draw()
        self.atrium_view.table_list.draw()
        arcade.draw_rectangle_filled(745, 350, 95, 400, arcade.color.BANANA_MANIA)
        self.atrium_view.opus.draw()

        #redraw characters
        self.atrium_view.char1.draw()
        self.atrium_view.char2.draw()
        self.atrium_view.char3.draw()
        self.atrium_view.char4.draw()
        you = self.atrium_view.char5
        you.draw()

        #draw popup
        arcade.draw_lrtb_rectangle_filled(left=you.left,right=you.right,top=you.top,bottom=you.bottom,
                                          color = arcade.color.ORANGE + (200,))
        arcade.draw_rectangle_filled(400,300,500,300,arcade.color.LIGHT_STEEL_BLUE)
        arcade.draw_text("YOU ARE ABOUT TO ENTER OPUS",400,340,arcade.color.BLACK,20,
                         anchor_x="center",align="center",font_name="Comic Sans MS")
        arcade.draw_text("Press ENTER to continue\nPress ESCAPE to return to atrium",
                         400,250,arcade.color.BLACK,13,anchor_x="center",align="center",
                         font_name="Comic Sans MS")

    def on_update(self, delta_time):
        if self.escape == True:
            if arcade.check_for_collision(self.atrium_view.char5, self.atrium_view.opus):
                self.atrium_view.char5.update()
                self.atrium_view.char5.change_x = -1
                self.atrium_view.char5.change_y = -1
            elif arcade.check_for_collision(self.atrium_view.char5, self.atrium_view.opus) == False:
                self.escape = False
                atrium = self.atrium_view
                self.window.show_view(atrium)
                self.atrium_view.char5.change_x = 0
                self.atrium_view.char5.change_y = 0

    def on_key_press(self, key, mod):
        if key == arcade.key.ENTER:
            opus_view = OpusView(self.atrium_view)
            opus_view.setup()
            self.window.show_view(opus_view)
        if key == arcade.key.ESCAPE:
            self.escape = True


class OpusView(arcade.View):

    def __init__(self,atrium_view):
        super().__init__()
        self.atrium_view = atrium_view
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
        self.money_png = None
        self.money = 0

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
        self.order = ["Iced Coffee!\nYou need: ice, coffee, and milk.",
                      "Frappuccino!\nYou need: syrup, ice, espresso, and whipped cream.",
                      "Matcha Iced Tea!\nYou need: ice and a matcha flavor shot.",
                      "Passion Tango Iced Tea!\nYou need: ice and a passion tango flavor shot.",
                      "Guava White Iced Tea Lemonade!\nYou need: ice and a guava white flavor shot."]
        self.new_order = random.choice(self.order)

        #popup logic
        self.proceed = False
        self.popup_text = ""
        self.tea_popup = False
        self.tea_list = None
        self.curr_tea = None
        self.tea_list_increment = 0
        self.matcha = None
        self.passion_tango = None
        self.guava_white = None
        self.indicator = ""

    def setup(self):
        self.you = arcade.Sprite("game1_images/you.png", scale=0.45, center_x=500, center_y=305)
        self.boss = arcade.Sprite("game1_images/boss.png", scale=0.19, center_x=100, center_y=460)
        self.cup = arcade.Sprite("game1_images/cup.png",scale=0.18,center_x=400,center_y=305)
        self.money_png = arcade.Sprite("game1_images/money_png.png",scale=0.05,center_x=670,center_y=50)

        #stations
        self.trash = arcade.Sprite("game1_images/trash.png",scale=0.15,center_x=730,center_y=410)
        self.coffee_station = arcade.Sprite("game1_images/coffee_station.jpg",scale=0.15,center_x=80,center_y=250)
        self.milk_station = arcade.Sprite("game1_images/milk.png",scale=0.08,center_x=80,center_y=80)
        self.syrup_station = arcade.Sprite("game1_images/syrup_station.png",scale=0.15,center_x=370,center_y=70)
        self.ice_station = arcade.Sprite("game1_images/ice.jpg",scale=0.15,center_x=490,center_y=70)
        self.whipped_cream = arcade.Sprite("game1_images/whipped_cream.png",scale=0.15,center_x=580,center_y=70)
        self.iced_tea = arcade.Sprite("game1_images/iced_tea.png",scale=0.15,center_x=730,center_y=230)

    def add_ice(self):
        if self.drink != "Frappuccino":
            if arcade.check_for_collision(self.you, self.ice_station) and self.cup_empty == True:
                self.cup = arcade.Sprite("game1_images/ice_cup.png", scale=0.18, center_x=400, center_y=305)
                self.ice_done = True
                self.cup_empty = False
        elif self.drink == "Frappuccino":
            if arcade.check_for_collision(self.you, self.ice_station) and self.syrup_done == True:
                self.cup = arcade.Sprite("game1_images/syrup_ice.png", scale=0.18, center_x=400, center_y=305)
                self.ice_done = True
                self.syrup_done = False

    def add_coffee(self):
        if arcade.check_for_collision(self.you, self.coffee_station) and self.ice_done == True:
            self.coffee_done = True
            self.ice_done = False
            if self.drink == "Frappuccino":
                self.cup = arcade.Sprite("game1_images/frap_ice.png", scale=0.18, center_x=400, center_y=305)
            elif self.drink == "Iced Coffee":
                self.cup = arcade.Sprite("game1_images/ice_coffee1.png", scale=0.18, center_x=400, center_y=305)

    def add_milk(self):
        if arcade.check_for_collision(self.you, self.milk_station) and self.coffee_done == True:
            self.cup = arcade.Sprite("game1_images/ice_coffee2.png", scale=0.18, center_x=400, center_y=305)
            self.coffee_done = False
            self.complete = True

    def add_tea(self):
        if arcade.check_for_collision(self.you, self.iced_tea) and self.ice_done == True and self.indicator == "":
            self.tea_popup = True

        elif arcade.check_for_collision(self.you,self.boss):
            if self.indicator == "Matcha Done" and "Matcha" in self.instructions:
                self.indicator = ""
                self.complete = True
            if self.indicator == "Passion Tango Done" and "Passion Tango" in self.instructions:
                self.indicator = ""
                self.complete = True
            if self.indicator == "Guava White Done" and "Guava White" in self.instructions:
                self.indicator = ""
                self.complete = True
            self.ice_done = False

    def add_syrup(self):
        if arcade.check_for_collision(self.you, self.syrup_station) and self.cup_empty == True:
            self.cup = arcade.Sprite("game1_images/syrup.png", scale=0.18, center_x=400, center_y=305)
            self.syrup_done = True
            self.cup_empty = False

    def add_whipped_cream(self):
        if arcade.check_for_collision(self.you, self.whipped_cream) and self.coffee_done == True:
            self.cup = arcade.Sprite("game1_images/frap_cream.png", scale=0.18, center_x=400, center_y=305)
            self.coffee_done = False
            self.complete = True


    def on_draw(self):
        #setup
        arcade.start_render()
        self.boss.draw()
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, 520, 600, 100, arcade.color.LIGHT_STEEL_BLUE)
        arcade.draw_text(self.instructions, self.pos_x, self.pos_y, arcade.color.BLACK, 16,font_name="Comic Sans MS",
                         anchor_x="center",anchor_y="center",align="center")
        arcade.draw_text(self.press_space, 320, 480, arcade.color.BLACK, 10)

        #monitor start of game
        if self.space_count > 0:
            self.cup.draw()
        if self.game_start == True:
            arcade.draw_text(f"Time remaining: {self.time:.0f}", 400,456,arcade.color.BLACK,anchor_x="center",
                             anchor_y="center",align="center",font_name="Comic Sans MS",font_size=15)

        #draw stations
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
            self.add_ice()
            self.add_coffee()
            self.add_milk()
            self.check_complete()

        elif self.drink == "Iced Tea":
            self.add_ice()
            self.add_tea()
            self.check_complete()

        elif self.drink == "Frappuccino":
            self.add_syrup()
            self.add_ice()
            self.add_coffee()
            self.add_whipped_cream()
            self.check_complete()

        #trash can to clear
        if arcade.check_for_collision(self.you,self.trash):
            #start fresh
            self.syrup_done = False
            self.ice_done = False
            self.coffee_done = False
            self.indicator = ""
            self.complete = False
            self.cup_empty = True
            self.cup = arcade.Sprite("game1_images/cup.png", scale=0.18, center_x=400, center_y=305)


        #show level
        if self.game_start == True:
            arcade.draw_text(f"Level: {self.level}",710,100,arcade.color.BLACK,anchor_x="center",
                             anchor_y="center",align="center",font_name="Comic Sans MS",font_size=25)
            self.money_png.draw()
            arcade.draw_text(f" = ${self.money:.2f}",740,50,arcade.color.BLACK,anchor_x="center",anchor_y="center",
                             align="center",font_name="Comic Sans MS",font_size=18)

        #instructions popup
        if self.proceed == False and self.tea_popup == False:
            arcade.draw_rectangle_filled(400,300,450,250,arcade.color.LIGHT_PINK + (200,))
            self.popup_text = "INSERT INSTRUCTIONS,\npress ENTER to play"
            arcade.draw_text(self.popup_text,400,300,arcade.color.BLACK,17,anchor_x="center",
                            anchor_y="center",align="center",font_name="Comic Sans MS")

        #tea selection popup
        if self.tea_popup == True:
            arcade.draw_rectangle_filled(400,300,580,270,arcade.color.LIGHT_GRAY)
            arcade.draw_text("Press the RIGHT & LEFT arrows to toggle flavors,\npress ENTER to select.",400,380,
                             arcade.color.BLACK,17,anchor_x="center",anchor_y="center",align="center",
                             font_name="Comic Sans MS")
            self.tea_list = arcade.SpriteList()
            self.matcha = arcade.Sprite("game1_images/matcha.png",scale=0.12,center_x=300,center_y=230)
            self.passion_tango = arcade.Sprite("game1_images/passion_tango.png",scale=0.12,center_x=400,center_y=230)
            self.guava_white = arcade.Sprite("game1_images/guava_white_tea.png", scale=0.12, center_x=500, center_y=230)
            self.tea_list.append(self.matcha)
            self.tea_list.append(self.passion_tango)
            self.tea_list.append(self.guava_white)
            self.tea_list.draw()
            arcade.draw_text("Matcha",300,200,arcade.color.BLACK,10,anchor_x="center",anchor_y="center",
                             align="center",font_name="Comic Sans MS")
            arcade.draw_text("Passion\nTango",400,200,arcade.color.BLACK,10,anchor_x="center",anchor_y="center",
                             align="center",font_name="Comic Sans MS")
            arcade.draw_text("Guava White",500,200,arcade.color.BLACK,10,anchor_x="center",anchor_y="center",
                             align="center",font_name="Comic Sans MS")

            self.curr_tea = self.tea_list[(self.tea_list_increment) % 3]
            arcade.draw_lrtb_rectangle_filled(left=self.curr_tea.left, right=self.curr_tea.right,
                                                top=self.curr_tea.top, bottom=self.curr_tea.bottom,
                                                color=arcade.color.WHITE + (200,))

        #"game over" popup
        if self.failed == True:
            self.proceed = False
            arcade.draw_rectangle_filled(400,300,600,400,arcade.color.BANANA_MANIA)
            self.popup_text = "Game Over"
            arcade.draw_text(self.popup_text,400,360,arcade.color.BLACK,20,anchor_x="center",
                            anchor_y="center",align="center",font_name="Comic Sans MS")
            #play again button
            arcade.draw_rectangle_filled(400,250,200,100,arcade.color.LIGHT_PINK)
            arcade.draw_text("Play Again",400,250, arcade.color.BLACK,15,
                             anchor_x="center",anchor_y="center",align="center", font_name="Comic Sans MS")
            #return to atrium button
            arcade.draw_rectangle_filled(400,150,100,50,arcade.color.LIGHT_PINK)
            arcade.draw_text("Return to atrium",400,150,arcade.color.BLACK,anchor_x="center",
                             anchor_y="center",align="center",font_size=10)


    def on_update(self, delta_time):
        if self.proceed == True:
            self.you.update()
            if self.game_start == True:
                if self.time > 0:
                    self.time -= delta_time
                self.instructions = f"Order {self.order_num}: {self.new_order}"
                self.drink_check()

                if self.time < 0:
                    self.failed = True

    def increment_money(self):
        if self.drink == "Frappuccino" and self.complete == True:
            self.money += 3.95
        elif self.drink == "Iced Coffee" and self.complete == True:
            self.money += 2.65
        elif self.drink == "Iced Tea" and self.complete == True:
            self.money += 2.25

    def check_complete(self):
        if arcade.check_for_collision(self.you, self.boss) and self.complete == True:
            self.increment_money()
            self.complete = False
            self.levels_completed += 1
            self.order_num += 1
            self.new_order = random.choice(self.order)
            self.cup = arcade.Sprite("game1_images/cup.png", scale=0.18, center_x=400, center_y=305)
            self.cup_empty = True

            #increasing levels of difficulty
            if self.levels_completed <= 2:
                self.time = 35
                self.level = 1
            elif self.levels_completed > 2 and self.levels_completed <= 5:
                self.time = 20
                self.level = 2
            elif self.levels_completed > 5 and self.levels_completed <= 9:
                self.time = 15
                self.level = 3
            elif self.levels_completed > 9 and self.levels_completed <= 14:
                self.time = 10
                self.level = 4
            elif self.levels_completed > 14 and self.levels_completed <= 20:
                self.time = 9
                self.level = 5
            elif self.levels_completed > 20 and self.levels_completed <= 27:
                self.time = 7
                self.level = 6
            elif self.levels_completed > 27 and self.levels_completed <= 35:
                self.time = 5
                self.level = "Impossible"


    def drink_check(self):
        if "Iced Coffee" in self.instructions:
            self.drink = "Iced Coffee"
        elif "Iced Tea" in self.instructions:
            self.drink = "Iced Tea"
        elif "Frappuccino" in self.instructions:
            self.drink = "Frappuccino"

    def on_key_press(self, key, modifiers):
        #get rid of popup by pressing ENTER
        if key == arcade.key.ENTER:
            self.proceed = True

        if self.proceed == True:
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

        #tea station popup
        if self.tea_popup == True:
            self.proceed = False
            if key == arcade.key.LEFT:
                self.tea_list_increment -= 1
            if key == arcade.key.RIGHT:
                self.tea_list_increment += 1
            if key == arcade.key.ENTER:
                self.tea_popup = False
                self.proceed = True
                self.tea_list_increment = 0

                if self.curr_tea == self.matcha:
                    self.cup = arcade.Sprite("game1_images/matcha.png", scale=0.18, center_x=400, center_y=305)
                    self.indicator = "Matcha Done"
                if self.curr_tea == self.passion_tango:
                    self.cup = arcade.Sprite("game1_images/passion_tango.png", scale=0.18, center_x=400,
                                                 center_y=305)
                    self.indicator = "Passion Tango Done"
                if self.curr_tea == self.guava_white:
                    self.cup = arcade.Sprite("game1_images/guava_white_tea.png", scale=0.18, center_x=400,
                                                 center_y=305)
                    self.indicator = "Guava White Done"


    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.you.change_x = 0
        elif key == arcade.key.RIGHT:
            self.you.change_x = 0
        elif key == arcade.key.DOWN:
            self.you.change_y = 0
        elif key == arcade.key.UP:
            self.you.change_y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if self.failed == True and x>=300 and x<=500 and y>=200 and y<= 300:
            opus_view = OpusView(self.atrium_view)
            opus_view.setup()
            self.window.show_view(opus_view)

        if self.failed == True and x >= 350 and x <= 450 and y >= 100 and y <= 200:
            atrium_view = self.atrium_view
            atrium_view.setup()
            self.window.show_view(atrium_view)


def main():
        """ Main method """

        """ This is the actual game main() """
        window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        start_view = Opening()
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
