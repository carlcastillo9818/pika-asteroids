import turtle # import all methods and attributes from turtle module (Turtle class)
import random
import math
import winsound

# set up screen
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("Simple Python Turtle Graphics game (class version)") # name of the game at the top of the window
wn.bgpic("spacetimee.gif") # set a cool space background for the game
wn.register_shape("pikachu1.gif") # register a new shape (custom icon for your characters)

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white") # color of text
        self.goto(-290, 310) # position of the score board
        self.score = 0 # attribute called score is set to 0 at start of game

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align = "left", font =("Arial", 14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()

    def play_sound(self):
        winsound.Beep(2000, 2)
        
class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self) # initialize parent class inside Border init
        self.penup() # raises pen while drawing
        self.hideturtle() # hides turtle icon
        self.speed(0) # this speed is a method.  controls animation speed (0 means draw as fast as possible)
        self.color("white") # changes color of border
        self.pensize(5) # width of the border (5 pixels)
    
    def draw_border(self):
        self.penup()
        self.goto(-300,-300)
        self.pendown()
        self.goto(-300,300)
        self.goto(300, 300)
        self.goto (300, -300)
        self.goto(-300, -300)


class Player(turtle.Turtle): # player is subclass of the Turtle class
    
    def __init__(self): # class constructor 
        turtle.Turtle.__init__(self) # initialize the parent class inside the Player init
        self.penup() # raises pen
        self.speed(0) # this speed is a method.  controls animation speed (0 means draw as fast as possible)
        self.shape("triangle")  # changes shape
        self.color("white") # changes color
        self.speed = 1 # how fast player will move (attribute)
        
    def move(self): # Player class method (must include self)
        self.forward(self.speed) # built in method of Turtle class (moves turtle forward at the speed of current Turtle = 1)

        if (self.xcor() > 290 or self.xcor() < -290): # border checking
            self.left(60)
        if (self.ycor() > 290 or self.ycor() < -290):
            self.left(60)
            
    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def increasespeed(self):
        self.speed += 1


class Goal(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("pikachu1.gif")
        self.speed = 3
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360))

    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360))

    def move(self): # Player class method (must include self)
        self.forward(self.speed) # built in method of Turtle class (moves turtle forward at the speed of current Turtle = 1)

        # border checking
        if (self.xcor() > 290 or self.xcor() < -290): 
            self.left(60)
        if (self.ycor() > 290 or self.ycor() < -290):
            self.left(60)

# collision checking function
# uses pythagorean theorem to measure distance between two objects
def isCollision(t1, t2):
    a = t1.xcor() - t2.xcor()
    b = t1.ycor() - t2.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))

    if (distance < 20):
        return True
    else:
        return False

# create class instances
player = Player() # created a class instance called player
border = Border() # border instance
game = Game() # game score instance

# draw border
border.draw_border() # draw the border around screen

# create multiple goals
goals = []
for count in range(6):
    goals.append(Goal())
    
# set keyboard bindings
turtle.listen()
turtle.onkey(player.turnleft, "Left")
turtle.onkey(player.turnright, "Right")
turtle.onkey(player.increasespeed, "Up")

# speed up game
wn.tracer(2) # the speed for updating the screen
 

# main loop
while True:
    wn.update() # updates the screen 
    player.move()
    
    for goal in goals: # loop through list of goals
        goal.move() # moves the next goal
        
        if isCollision(player, goal): # checks each goal if its colliding with the player
            goal.jump() # moves the next goal to a random location if it collides with player
            game.change_score(10)
            game.play_sound()
