# CTI-110 
# M3HW2 - Software Sales 
# Jamire Pierce
# 9/22/2017

def main():

    qnt10_19 = 10
    qnt20_49 = 20
    qnt50_99 = 30
    qnt100 = 40
    #start = raw_input("Testing loop are you ready? [yes/no].")

    #if start  yes
        #print( packages_purchased )

    packages_purchased = int(input("Enter the number of how many packages purchased:", ))

    if packages_purchased > 10 and packages_purchased <= 19:
        print("The discount is 10%.")
            
    elif packages_purchased > 20 and packages_purchased <= 49:
        print("The discount is 20%.")

    elif packages_purchased > 50 and packages_purchased <= 99:
        print("This discount is 30%.")

    elif packages_purchased >= 100:
        print("This discount is 40%.")
                
    else:
        print("No discount.")

    #else:
        #print("Good bye")


main()
