# SoC
Summer of Code 2020
Project 1: Opus Mania

## **Questions**
1. Why does it take so long for my screens to load? 
2. In line 285, I called self.cup.draw() but it isn't drawing the image. I know you're supposed to call draw() under the on_draw() function, but I only want this image to be called in this one particular instance. How should I go about that? ...Also, somehow, self.cup.draw() placed under on_key_press() worked in a previous version I had...but I don't understand why. 
3. Is there a way to overlap pictures so that you can see both on top of one another??? 
4. How do you update text more than once?? (I have a variable self.space_count, so under on_key_press() every time the user presses the space bar, I do self.space_count +=1. Then in the next if statement I say if key == arcade.key.SPACE and self.space_count == [a specific count], then show the next text. But I am still trying to debug this. 
5. (Less important) How do you prevent the character from running over a table/chair/tree? I know you can check for collision...and then call stop() on the character? 
6. I have a vision of doing this: on the opening screen, the player can choose which character they want to be. Then that changes which characters are stationary in the atrium. But then that means when creating the Sprites, I need to make the image file's name a variable... how would I do that? Maybe store all the characters in a list, and remove the character that the player chooses from the list...?? Want a more solid idea
7. [This is just a note to myself:] Maybe during the game, the character can earn money. Then, when they're done playing the Opus game, they can go back to the Science Center atrium to buy something from a friend! Kind of like an easter egg surprise at the end.

#### **Jiin's Tips**
**1. "Get" function that gets center of a sprite... even while it moves?:** self.player.get_position()

**2. Can't bold or italicize text,** but you can do font_name="Comic Sans MS" or any other system fonts, like from Microsoft Word. Also, anchor_x="center" and align="center" do different things but both are useful. 

**3. To update text:** you can totally pass a variable when calling draw_text(). You can also do an f-string which allows you to write string words & a string variable in the same line.




### **How to run my code**
Run game.py. I have uploaded the Sprite images used in this program under the "Images" file. Make sure you have the library arcade installed.


### **Motivation**
I enjoyed working in the Science Center atrium on campus and would like to replicate it in a game. 


### **Description**
You, the player, are a Hamilton College student. As you walk into the Science Center atrium, you can talk to fellow students. You'll soon find out that you're late for work. When you walk into Opus, you make drinks to earn money! 


### **Keys/Buttons**
Use the up/down/left/right arrow keys to move character around. Direct your character to the upper/right corner (where the Opus sign is) to enter the game! Use touchpad/mouse to play Opus game. 


### **Python Concepts Utilized**

### **Arcade Features Utilized**

### **Challenges/Lessons**

### **Future Steps**
