# SoC
Summer of Code 2020
Project 1: Opus Mania

## **Questions**
1. Why does it give me this error: 'NoneType' object has no attribute 'draw' for my Sprite self.you.draw()? I initialized the sprite in the initializer, set it up in setup(), and called .draw() on it... but it is still apparently NoneType? What does that mean? 
2. Is there any way to make a “get” function that gets the center of a Sprite? (Even while it moves?) Can't seem to find any online. 
3. How to change text to Bold, change the font, or center the text? Whenever I write bold=True in creating text, it doesn't actually bold it.. 
4. Relating to Question3, is there a way to update text, like a set_text() function? That way, you don't have to re-create text in the same location repeatedly? 
5. How do you prevent the character from running over a table/chair/tree? I know you can check for collision...and then call stop() on the character? 
6. I have a vision of doing this: on the opening screen, the player can choose which character they want to be. Then that changes which characters are stationary in the atrium. But then that means when creating the Sprites, I need to make the image file's name a variable... how would I do that? Maybe store all the characters in a list, and remove the character that the player chooses from the list...?? Want a more solid idea
7. [This is just a note to myself:] Maybe during the game, the character can earn money. Then, when they're done playing the Opus game, they can go back to the Science Center atrium to buy something from a friend! Kind of like an easter egg surprise at the end.


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
