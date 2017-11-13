import turtle# Allows us to use turtles

def main():
    
    wn = turtle.Screen()      
    t = turtle.Turtle()
    t.speed(10)
    t.color("gold")
    t.pensize(10)

    #___________________

    for i in range(1):
        t.right(90)
        t.forward(45)
        for j in range(8):
            t.forward(100)
            t.right(45)
            t.forward(1)
            t.right(180)
            t.forward(200)

    t.right(45)
            

main()



