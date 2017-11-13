# Feet to inches
# 11/1/17
# CTI-110 M6T2_FeetToInches 
# Jamire Pierce
#
foot = 12

def main():
    
    feet = int(input("Enter a number of feet: "))
    
    print(feet, "equals", feet_to_inches(feet), "inches.")
                   


def feet_to_inches(feet):
    
    return feet * foot


main()
