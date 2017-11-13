#CTI 110
#M5HW3
#Jamire Pierce
#10/29

def main():
    factorial = 1

    running = True

    while running:
        number = int(input("Whats the number you wish to enter? "))

        if number < 0:
            running = False
            print("Number can not be a negative number.")

        else:
            for x in range(1,number + 1):
                factorial = factorial*x
            print("The factorial of",number,"is",factorial)



            '''
            start = 1;
            numberstop = range(1,number)
            for x in numberstop:
                stepone = start - number
                start *= number
            print("The factorial of", number, end="")
            print(" is", stepone)
            '''
                   
               

main()
