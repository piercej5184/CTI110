# CTI 110
# M5T2
# Jamire
# 10/29

def main():

    

    runningtotal = 0
    keepGoing = True

    while keepGoing:
        number = int(input("Enter a number? "))
        

        if number < 0:
            keepGoing = False

        else:
            runningtotal += number
    print("Total is:", runningtotal)

main()
