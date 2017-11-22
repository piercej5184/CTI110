#CTI110
#M3T1 Areas oF rectangels
#Jamire Pierce
#9/13/2017







firstWidth = int(input("Width of first rectangle?"))
firstLength = int(input("Length of first rectangle?"))

secondWidth = int(input("Width of second rectangle?"))
secondLength = int(input("Length of second rectangle?"))

firstArea = firstWidth * firstLength
secondArea = secondWidth * secondLength
print("First Rectangle is:", (firstArea))
print("Second Rectangle is:", (secondArea))

if firstArea > secondArea:
    print("First rectangle is bigger")
else:
        if firstArea < secondArea:
            print("Second rectangle is bigger")
        else:
                #equal
                print("They are equal size")
    
