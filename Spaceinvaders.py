#Space Invaders
#Pycharm 3.0 on Windows
# My first programming code
import turtle
import winsound
import math
import random


#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("bgstars.gif")

# Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-270, -270)
border_pen.pendown()
border_pen.pensize(1)
for side in range(4):
    border_pen.fd(540)
    border_pen.lt(90)
border_pen.hideturtle()

# Set score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-260,250)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -200)
player.setheading(90)
player_speed = 15

# Choose a number of enemies
number_of_enemies = 5

# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y= random.randint (100, 250)
    enemy.setposition (x, y)
enemyspeed = 2

# Create the player´s bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet_speed = 20

#Define bullet state
#ready- ready to fire
#fire - bullet firing
bullet_state = "ready"

#Move the player left and right
def move_left():
    x = player.xcor()
    x-= player_speed
    if x < -260:
         x = - 260
    player.setx(x)
def move_right():
    x = player.xcor()
    x += player_speed
    if x > 260:
         x =  260
    player.setx(x)
def fire_bullet():
    #Declare global state if needs to change
    global bullet_state
    if bullet_state is "ready":
        winsound.PlaySound("laser", winsound.SND_ASYNC)
        bullet_state = "fire"
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition (x, y)
        bullet.showturtle()
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
         return True
    else:
         return False
# Create Keyboard bindings
turtle.listen ()
turtle.onkeypress (move_left, "Left")
turtle.listen ()
turtle.onkeypress (move_right, "Right")
turtle.listen ()
turtle.onkey (fire_bullet, "space")
 #Main game loop
while True:
     for enemy in enemies:
         # Move the enemy
         x = enemy.xcor()
         x += enemyspeed
         enemy.setx(x)
         # Move the enemy back an down
         if enemy.xcor() > 260:
             # Move all enemies down when right
             for e in enemies:
                 y = e.ycor()
                 y -= 40
                 e.sety(y)
            # Change enemies direction when right
             enemyspeed *= -1
         if enemy.xcor() < -260:
             # Move all enemies down when left
             for e in enemies:
                 y = e.ycor()
                 y -= 40
                 e.sety(y)
             # Change enemies direction when left
             enemyspeed *= -1
         # Check for collision between the bullet and the enemy
         if isCollision(bullet, enemy):
             winsound.PlaySound("explosion", winsound.SND_ASYNC)
             # Reset the bullet
             bullet.hideturtle()
             bullet_state = "ready"
             bullet.setposition(0, -400)
             # Reset the enemy
             x = random.randint(-200, 200)
             y = random.randint(100, 250)
             enemy.setposition(x, y)
             # Update the score
             score += 10
             scorestring = "Score: %s" %score
             score_pen.clear()
             score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

         if isCollision(player, enemy):
             winsound.PlaySound("explosion", winsound.SND_ASYNC)
             player.hideturtle()
             enemy.hideturtle()
             print("Game Over")
             break

     # Move the bullet
     if bullet_state == "fire":
         y = bullet.ycor()
         y += bullet_speed
         bullet.sety(y)

     # Check to see if the bullet has gone to the top
     if bullet.ycor() > 260:
         bullet.hideturtle()
         bullet_state = "ready"



wn.mainloop()
