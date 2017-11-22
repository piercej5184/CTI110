#CTI 110 M5T1 Turtle Lab
#Jamire Pierce
#10/11/17


def main():
    
    
    import turtle
    wn = turtle.Screen() 
    t = turtle.Turtle()

    # add some display options
    t.pensize(5)            # increase pensize (takes integer)
    t.pencolor("lightgrey")     # set pencolor (takes string)
    t.shape("turtle")
    

    #J
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(80)
    '''
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    '''
    for i in range(18):
        t.right(10)
        t.forward(5)
    t.forward(5)

    #t.forward
    #J is done

    #Next letter
    t.penup()
    t.right(180)
    t.forward(30)
    t.left(90)
    t.forward(125)
    t.pendown()
    #done

    #P
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(25)
    #t.forward(50)
    '''
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    '''
    #t.right(180)
    for i in range(18):
        t.right(10)
        t.forward(5)

    t.forward(20)
        
    #P is done
    
    
    
    
    wn.mainloop()

main()




